# utils/helpers.py
import json
import os
from datetime import datetime
from config import USER_DATA_FILE

def get_default_user_data(user_id: int):
    """
    Mengembalikan skema default data pengguna baru (Free tier).
    """
    return {
        "user_id": user_id,
        "plan": "Free",
        "daily_limit": 10,
        "usage_today": 0,
        "premium_until": None,
        "referrals": 0,
        "referred_by": None,
        "history": [] # Berisi maksimal 10 pengerjaan terakhir
    }

def load_all_users() -> dict:
    """
    Membaca database JSON secara aman.
    """
    if not os.path.exists(USER_DATA_FILE):
        return {}
    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_all_users(data: dict):
    """
    Menyimpan modifikasi database ke file JSON.
    """
    try:
        with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception:
        pass

def get_user_data(user_id: int) -> dict:
    """
    Mengambil data spesifik user. Jika belum ada, otomatis mendaftarkannya dengan skema default.
    """
    users = load_all_users()
    str_id = str(user_id)
    if str_id not in users:
        users[str_id] = get_default_user_data(user_id)
        save_all_users(users)
    
    # Tambahkan sisa kredit (kalkulasi dinamis)
    user_data = users[str_id]
    user_data["remaining_credits"] = max(0, user_data.get("daily_limit", 10) - user_data.get("usage_today", 0))
    
    return user_data

def update_user_data(user_id: int, key: str, value):
    """
    Memperbarui atribut spesifik dari data pengguna.
    """
    users = load_all_users()
    str_id = str(user_id)
    if str_id not in users:
        users[str_id] = get_default_user_data(user_id)
    users[str_id][key] = value
    save_all_users(users)

def add_user_history(user_id: int, tool: str, text_input: str, text_output: str, style: str):
    """
    Menyimpan hasil pengerjaan AI ke list histori (maksimal 10 item terbaru), 
    sekaligus menambah count limit pemakaian harian.
    """
    users = load_all_users()
    str_id = str(user_id)
    if str_id not in users:
        users[str_id] = get_default_user_data(user_id)
    
    history_list = users[str_id].get("history", [])
    
    # Format item riwayat baru
    new_item = {
        "tool": tool,
        "input": text_input[:65] + "..." if len(text_input) > 65 else text_input,
        "output": text_output[:65] + "..." if len(text_output) > 65 else text_output,
        "style": style,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Masukkan di awal (data paling baru di atas)
    history_list.insert(0, new_item)
    
    # Batasi agar size history stabil (maksimal 10)
    users[str_id]["history"] = history_list[:10]
    
    # Tambah counter penggunaan harian
    users[str_id]["usage_today"] = users[str_id].get("usage_today", 0) + 1
    
    save_all_users(users)
