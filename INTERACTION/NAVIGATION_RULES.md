# NAVIGATION_RULES.md

## PURPOSE

Dokumen ini mengatur prinsip navigation dalam ecosystem PRODUCTIVITY_AI.

Tujuan utama:
- menjaga flow tetap jelas
- mengurangi user tersesat
- menjaga momentum interaction
- membuat movement user terasa ringan dan natural

Dokumen ini digunakan oleh:
- INTERACTION_DESIGNER
- UX_RETENTION
- MANAGER_ORCHESTRATOR

---

# CORE PRINCIPLE

Good navigation membuat user:
- tahu mereka sedang dimana
- tahu harus kemana
- tahu cara kembali

Navigation buruk:
= user kehilangan arah.

---

# NAVIGATION PRIORITIES

Urutan prioritas navigation:

1. Clarity
2. Recoverability
3. Speed
4. Simplicity
5. Visual Polish

Jika navigation terlihat keren tapi membingungkan:
pilih clarity.

---

# MAIN NAVIGATION RULES

## 1. User Harus Selalu Bisa Kembali

Setiap flow harus memiliki:
- back navigation
- home/menu access
- recovery path

User tidak boleh:
- terjebak
- bingung keluar
- dipaksa restart flow

---

## 2. Hindari Deep Navigation

Telegram bukan aplikasi multi-page.

Hindari:
- terlalu banyak layer menu
- nested callback berlebihan
- flow terlalu panjang

Ideal:
maksimal 2-3 layer navigation.

Jika lebih:
pertimbangkan:
- simplifikasi flow
- grouping ulang
- shortcut access

---

## 3. Navigation Harus Konsisten

Button:
- Home
- Kembali
- Tutup
- Menu

harus:
- konsisten posisi
- konsisten wording
- konsisten behavior

Jangan:
kadang "Back"
kadang "Kembali"
kadang "←"

tanpa pola jelas.

---

## 4. Jangan Putus Momentum User

Setelah user menyelesaikan action:
jangan biarkan flow kosong.

Selalu berikan:
- next step
- CTA lanjutan
- arah berikutnya

Contoh:
setelah generate selesai:
- Regenerate
- Edit Prompt
- Gunakan Style Lain

Bukan:
interaction selesai lalu kosong.

---

## 5. Home/Menu Harus Mudah Diakses

Main menu adalah:
safe zone user.

User harus bisa:
- kembali cepat
- reset flow
- pindah fitur

tanpa kebingungan.

---

# TELEGRAM-SPECIFIC RULES

## 1. Minim Message Chaos

Hindari:
- spam message baru
- navigation yang memenuhi chat
- flow yang membuat chat berantakan

Gunakan:
- edit message jika cocok
- inline keyboard
- compact flow

---

## 2. Callback Flow Harus Ringan

Jangan membuat callback:
- terlalu panjang
- terlalu bercabang
- sulit dipahami

Flow harus:
- predictable
- ringan
- mudah di-debug

---

## 3. Navigation ≠ Web App

Telegram interaction bersifat:
- cepat
- conversational
- lightweight

Jangan memaksa:
- dashboard mentality
- complex menu tree
- desktop app navigation

---

# RECOVERY PRINCIPLES

## 1. User Error Harus Mudah Dipulihkan

Jika user:
- salah klik
- salah input
- keluar flow

system harus:
- mudah dipulihkan
- tidak menghukum user

---

## 2. Jangan Paksa Restart Total

Jika memungkinkan:
- simpan momentum
- simpan posisi flow
- berikan shortcut kembali

Restart total hanya jika memang perlu.

---

# FLOW STRUCTURE PRINCIPLES

## 1. Main Flow Harus Pendek

Semakin panjang flow:
semakin tinggi kemungkinan drop.

Prioritaskan:
- quick completion
- minim langkah
- fast interaction

---

## 2. Secondary Flow Jangan Mengganggu Main Goal

Contoh:
user ingin generate caption.

Jangan:
terlalu banyak:
- promo
- setting
- submenu tambahan

yang mengganggu objective utama.

---

# ANTI-PATTERNS

Hindari:
- dead-end navigation
- nested menu berlebihan
- callback chaos
- inconsistent back button
- spam message navigation
- user kehilangan arah
- terlalu banyak branching
- flow panjang tanpa progress feeling
- forced restart flow

---

# FINAL DOCTRINE

Good navigation terasa:
- ringan
- natural
- jelas
- cepat

User tidak perlu berpikir keras untuk bergerak di dalam bot.

Navigation terbaik adalah navigation yang hampir tidak terasa.