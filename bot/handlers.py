from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from .config import GROUP1_ID, GROUP2_ID, MODERATOR_IDS
from .storage import add_message, get_original_id, remove_message
from .keyboards import action_keyboard

# Сохраняем сообщения, которые уже были пересланы
forwarded_cache = set()

async def on_reaction(client: Client, message: Message):
    # Проверяем, что это нужная группа и нужная реакция
    if message.chat.id != GROUP1_ID:
        return
    if not hasattr(message, "reactions") or not message.reactions:
        return
    for reaction in message.reactions:
        if getattr(reaction, "emoji", None) == "👎":
            # Пересылаем только если еще не пересылали
            if message.id in forwarded_cache:
                return
            fwd = await message.forward(GROUP2_ID)
            await fwd.reply(
                "Модерация: удалить сообщение в основной группе?",
                reply_markup=action_keyboard()
            )
            add_message(message.id, fwd.id)
            forwarded_cache.add(message.id)
            break

async def on_callback(client: Client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in MODERATOR_IDS:
        await callback_query.answer("Нет прав.", show_alert=True)
        return

    forwarded_msg_id = callback_query.message.id
    original_msg_id = get_original_id(forwarded_msg_id)

    if callback_query.data == "delete":
        if original_msg_id:
            try:
                await client.delete_messages(GROUP1_ID, original_msg_id)
            except Exception as e:
                await callback_query.answer("Ошибка при удалении!", show_alert=True)
                return
        await callback_query.edit_message_text("Сообщение удалено в основной группе.")
        remove_message(forwarded_msg_id)

    elif callback_query.data == "cancel":
        await callback_query.message.delete()
        remove_message(forwarded_msg_id)