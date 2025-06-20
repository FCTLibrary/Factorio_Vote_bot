from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from .config import API_ID, API_HASH, USER_SESSION
from .handlers import on_reaction, on_callback

app = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=USER_SESSION,
    workdir="."
)

@app.on_message(filters.group & filters.reaction)
async def reaction_update_handler(client, message: Message):
    await on_reaction(client, message)

@app.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    await on_callback(client, callback_query)

if __name__ == "__main__":
    app.run()
