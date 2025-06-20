from pyrogram import Client, filters
from pyrogram.types import Message, MessageReactionUpdated, CallbackQuery
from .config import API_ID, API_HASH, USER_SESSION
from .handlers import on_reaction, on_callback

app = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=USER_SESSION,
    workdir="."
)

# Pyrogram 2.0: реакции обрабатываются через event_handler
@app.on_message(filters.group, group=1)
async def message_handler(client, message: Message):
    # Для совместимости: если в message есть реакции
    if hasattr(message, "reactions") and message.reactions:
        await on_reaction(client, message)

@app.on_message_reaction_updated()
async def reaction_update_handler(client, reaction_update: MessageReactionUpdated):
    # Триггерим обработку по обновлению реакции
    msg = await client.get_messages(reaction_update.chat.id, reaction_update.message_id)
    await on_reaction(client, msg)

@app.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    await on_callback(client, callback_query)

if __name__ == "__main__":
    app.run()