# handlers/status.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.helpers import get_user_data
from utils.cleanup import safe_delete_message
from services.service_analytics import save_events

router = Router()

@router.callback_query(F.data == "btn_status")
async def process_status(callback: CallbackQuery):
    """
    Menampilkan status akun user, batas harian, status premium, dan referral.
    """
    user_id = callback.from_user.id
    user_data = get_user_data(user_id)
    
    plan = user_data.get("plan", "Free")
    usage = user_data.get("usage_today", 0)
    limit = user_data.get("daily_limit", 5)
    referrals = user_data.get("referrals", 0)
    
    status_symbol = "💎 Premium" if plan != "Free" else "🆓 Free Plan"
    
    status_text = (
        f"📊 <b>STATUS AKUN</b>\n"
        f"<blockquote>\n"
        f"👤 <b>ID:</b> <code>{user_id}</code>\n"
        f"🌟 <b>Plan:</b> {status_symbol}\n"
        f"📈 <b>Limit:</b> <code>{usage} / {limit}</code> digunakan hari ini\n"
        f"👥 <b>Referral:</b> <code>{referrals}</code> orang\n"
        f"</blockquote>\n\n"
        f"✨ <i>Ingin request tanpa batas? Tingkatkan keanggotaan kamu ke Premium sekarang.</i>"
    )
    
    # Keyboard khusus halaman status
    buttons = [
        [
            InlineKeyboardButton(text="💎 Upgrade ke Premium", callback_data="btn_premium")
        ],
        [
            InlineKeyboardButton(text="🏠 Menu Utama", callback_data="back_home")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    
    try:
        await callback.message.edit_text(
            text=status_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    except Exception:
        await safe_delete_message(callback.bot, callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=status_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    save_events(callback.from_user.id, "btn_status")
    
    await callback.answer()
