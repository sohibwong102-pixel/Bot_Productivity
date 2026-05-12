# handlers/history.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.helpers import get_user_data
from utils.cleanup import safe_delete_message
from services.service_analytics import save_events

router = Router()

@router.callback_query(F.data == "btn_history")
async def process_history(callback: CallbackQuery):
    """
    Menampilkan riwayat kerja (5-10 pengerjaan terakhir).
    """
    user_id = callback.from_user.id
    user_data = get_user_data(user_id)
    
    history_list = user_data.get("history", [])
    
    history_text = "📜 <b>RIWAYAT KERJA</b>\n\n"
    
    if not history_list:
        history_text += (
            "Belum ada aktivitas nih di data kamu..😅\n"
            "Yuk mulai dengan memilih menu <b>Tools</b>."
        )
    else:
        history_text += f"Berikut adalah {len(history_list)} aktivitas terakhir Anda:\n\n"
        for idx, item in enumerate(history_list, 1):
            tool_name = item.get("tool", "AI Work").capitalize()
            style_name = item.get("style", "Standard").capitalize()
            time_str = item.get("timestamp", "-")
            text_in = item.get("input", "")
            text_out = item.get("output", "")
            
            # Format rapih & ringkas
            history_text += (
                f"<b>{idx}. {tool_name} ({style_name})</b> ⏰ <i>{time_str}</i>\n"
                f"📥 <b>In:</b> {text_in}\n"
                f"📤 <b>Out:</b> {text_out}\n"
                f"────────────────────────────\n"
            )
            
    buttons = [
        [
            InlineKeyboardButton(text="Gunakan Tools", callback_data="menu_tools")
        ],
        [
            InlineKeyboardButton(text="🔙 Menu Utama", callback_data="back_home")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    
    try:
        await callback.message.edit_text(
            text=history_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    except Exception:
        await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=history_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    save_events(callback.from_user.id, "btn_history")
        
    await callback.answer()
