from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def action_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🗑️ Удалить", callback_data="delete"),
            InlineKeyboardButton("❌ Отменить", callback_data="cancel")
        ]
    ])