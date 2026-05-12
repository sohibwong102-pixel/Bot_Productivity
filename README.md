# 📝 DOKUMENTASI PROYEK: KERJA CEPAT WITH AI

Proyek ini adalah Telegram Bot Produktivitas berbasis AI (aiogram v3 & Gemini AI) yang dirancang dengan arsitektur sederhana (Simple-First) untuk membantu pengguna menyelesaikan tugas tulis-menulis secara instan langsung dari chat Telegram.

---

## 📂 STRUKTUR & DETAIL FILE PROYEK

Berikut adalah kegunaan dari setiap file yang ada di dalam direktori `/PRODUCTIVITY_AI/` untuk mempermudah pemahaman Anda:

### ⚙️ Root Konfigurasi
* **`main.py`** ➡️ Titik masuk utama (entry-point) aplikasi. Berfungsi untuk menyisipkan logging, mendaftarkan semua sub-router handler, membersihkan webhook lama, dan menyalakan polling Telegram secara terus menerus (looping).
* **`config.py`** ➡️ Membaca variabel sensitif dari file `.env` dan memastikan folder basis data `data/` dibuat secara otomatis ketika bot dijalankan.
* **`requirements.txt`** ➡️ Daftar pustaka (dependencies) Python yang wajib dipasang agar bot berjalan stabil (`aiogram`, `google-generativeai`, `python-dotenv`, dll).
* **`.env`** ➡️ File penyimpanan rahasia kredensial berupa `BOT_TOKEN` dan `GEMINI_API_KEY`.
* **`.gitignore`** ➡️ Berfungsi membatasi file lokal (seperti file database privat `user_data.json` dan cache python) agar tidak terunggah ke repositori publik Git.

### 🎮 Handlers (Alur Logika & Kontrol Menu)
Merupakan pusat interaksi chat (Routing System) yang mengarahkan tombol inline keyboard ke fitur tertentu:
* **`handlers/start.py`** ➡️ Mengatur respons perintah `/start`, menyambut pengguna baru, mendaftarkan profil awal ke database, dan menampilkan Menu Utama.
* **`handlers/tools.py`** ➡️ Logika utama pengolahan 6 AI Tools. Mengelola state pengiriman teks, memvalidasi limit harian, memicu proses asisten AI, dan meluncurkan Quick Action (Regenerasi/Ganti Gaya).
* **`handlers/status.py`** ➡️ Menampilkan informasi profil akun pengguna (Tipe Plan, sisa kuota harian, jumlah rujukan referral, dll).
* **`handlers/history.py`** ➡️ Menampilkan daftar ringkas 5-10 riwayat pengerjaan terakhir pengguna.
* **`handlers/premium.py`** ➡️ Mengatur alur promosi premium, pilihan paket (mingguan/bulanan), dan melacak pilihan metode transfer.

### ⌨️ Keyboards (Tampilan Tombol Interaktif)
Mengatur susunan tata letak inline keyboard Telegram agar bersih, minimalis, dan minim klik:
* **`keyboards/main_menu.py`** ➡️ Papan tombol menu navigasi utama (Tools, Riwayat, Status, Premium).
* **`keyboards/tools_menu.py`** ➡️ Daftar tombol pintas untuk memilih 1 dari 6 fitur utama (Rewrite, Reply, Caption, dll).
* **`keyboards/styles_menu.py`** ➡️ Tombol seleksi 6 Gaya Bahasa Cepat, dan tombol Quick Action (Regenerate, Gaya Lain).
* **`keyboards/premium_menu.py`** ➡️ Layout tombol pilihan durasi paket premium, pilihan e-wallet, dan tombol langsung hubungi admin kerja cepat.

### 🧠 States (Mesin Registrasi State)
* **`states/tool_states.py`** ➡️ Menyimpan state FSM (Finite State Machine) sederhana (`waiting_for_input`) guna menahan input teks pengguna saat menggunakan modul asisten AI.

### ⚡ Services (Integrasi API & Logika Eksternal)
* **`services/ai_service.py`** ➡️ Logika utama penyusun integrasi Google Gemini AI (`gemini-1.5-flash`). Berisi optimasi Prompt Engineering berdasarkan tools dan gaya bahasa yang telah dipilih user serta fallback respon simulasi jika API belum aktif.
* **`services/payment_service.py`** ➡️ Merumuskan instruksi pembayaran, rincian biaya transfer, dan pembuatan token instruksi (OVO, DANA, QRIS).

### 🛠️ Utilities & Helpers (Pembantu Sistem)
* **`utils/cleanup.py`** ➡️ Menerapkan Safe Cleanup Pattern. Berfungsi menghapus pesan secara aman (seperti teks loading/menunggu generasi AI) agar ruang chat tetap rapi tanpa resiko crash jika pesan sudah dihapus manual oleh user.
* **`utils/helpers.py`** ➡️ Fungsi dasar CRUD (Create, Read, Update, Delete) lokal ke file `user_data.json` untuk mencatat jumlah limit harian pengguna serta riwayat pengerjaan.

### 🗄️ basis data (Penyimpanan Data)
* **`data/user_data.json`** ➡️ Database berbasis flat JSON sederhana untuk menyimpan metadata pengguna, histori teks, dan status paket.

---

## 🚀 SARAN LANGKAH SELANJUTNYA UNTUK PENGEMBANGAN (NEXT STEPS)

Jika Anda ingin langsung mencoba menjalankan bot ini secara lokal di perangkat Anda, ikuti langkah mudah berikut:

### 1. Dapatkan Token Bot & API:
* Buat bot baru di Telegram lewat [@BotFather](https://t.me/BotFather) untuk mendapatkan token bot.
* Buat API Key gratis Google Gemini di Google AI Studio.

### 2. Isi Kredensial:
* Buka file `/PRODUCTIVITY_AI/.env` dan ganti nilai `YOUR_GEMINI_API_KEY_HERE` serta `BOT_TOKEN` dengan kredensial asli milik Anda.

### 3. Instalasi Dependensi:
Masuk ke folder proyek melalui terminal Anda dan jalankan perintah instalasi berikut:
```bash
cd PRODUCTIVITY_AI
pip install -r requirements.txt
```

### 4. Jalankan Bot:
Jalankan bot menggunakan perintah Python sederhana:
```bash
python main.py
```

Buka Telegram, ketik `/start` ke bot Anda, dan nikmati asisten AI super cepat siap pakai! 🚀
