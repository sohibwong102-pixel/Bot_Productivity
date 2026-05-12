# keyboards/tools_menu.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_tools_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Membuat inline keyboard untuk memilih 1 dari 6 AI Core Tools.
    """
    buttons = [
        [
            InlineKeyboardButton(text="Rewrite", callback_data="tool_rewrite"),
            InlineKeyboardButton(text="Customer Reply", callback_data="tool_customer_reply")
        ],
        [
            InlineKeyboardButton(text="Caption", callback_data="tool_caption")
        ],
        [
            InlineKeyboardButton(text="Translate", callback_data="tool_translate"),
            InlineKeyboardButton(text="Summarize", callback_data="tool_summarize")
        ],
        [
            InlineKeyboardButton(text="Email Writer", callback_data="tool_email_writer")
        ],
        [
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
