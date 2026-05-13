# BUTTON_HIERARCHY.md

## PURPOSE

Dokumen ini mengatur hierarchy dan struktur button dalam ecosystem PRODUCTIVITY_AI.

Tujuan utama:
- mempermudah decision user
- memperjelas CTA utama
- menjaga navigation tetap ringan
- mengurangi friction interaction

Dokumen ini digunakan oleh:
- INTERACTION_DESIGNER
- UX_RETENTION

---

# CORE PRINCIPLE

Button bukan dekorasi.

Button adalah:
- direction
- navigation
- momentum controller

Terlalu banyak button:
= user lelah memilih.

---

# BUTTON PRIORITY SYSTEM

## 1. Primary Button

Button utama.

Tujuan:
mengarahkan user ke action paling penting.

Karakteristik:
- paling jelas
- paling menonjol
- wording singkat
- mudah dipahami

Contoh:
- Generate
- Lanjutkan
- Upgrade Premium
- Coba Lagi

Rule:
Dalam 1 screen/message:
usahakan hanya ada 1 primary action utama.

---

## 2. Secondary Button

Action pendukung.

Digunakan untuk:
- alternatif ringan
- optional flow
- helper action

Contoh:
- Edit
- Ganti Style
- Lihat Contoh
- Bantuan

Secondary tidak boleh:
- lebih menarik dari primary
- membuat user bingung memilih

---

## 3. Navigation Button

Digunakan untuk movement/navigation.

Contoh:
- Kembali
- Home
- Tutup
- Menu

Navigation harus:
- konsisten
- mudah ditemukan
- predictable

---

# BUTTON LAYOUT PRINCIPLES

## 1. Jangan Overload Row

Hindari:
- terlalu banyak button dalam 1 row
- layout terlalu padat
- button kecil berdesakan

Ideal:
2 button per row.

Maksimal:
3 jika memang ringan dibaca.

---

## 2. CTA Utama Harus Mudah Terlihat

Primary action:
- jangan tenggelam
- jangan bercampur dengan action kecil
- jangan diletakkan terlalu random

User harus langsung tahu:
“ini tombol utama.”

---

## 3. Navigation Dipisah

Button navigation:
- jangan campur dengan CTA utama
- lebih baik di row bawah

Contoh baik:

[ Generate ]
[ Ganti Style ]
[ ← Kembali ]

---

## 4. Hindari Button Spam

Jangan:
- 10+ button sekaligus
- semua fitur dilempar sekaligus
- menu terlalu penuh

Jika fitur banyak:
gunakan:
- pagination
- submenu
- grouping

---

# BUTTON WORDING RULES

## 1. Gunakan Kata yang Natural

Hindari:
- terlalu technical
- terlalu panjang
- ambigu

Gunakan:
- jelas
- pendek
- mudah dipahami

Contoh:
GOOD:
- Coba Lagi
- Ringkas
- Translate
- Upgrade

BAD:
- Execute Prompt Transformation
- Generate Enhanced Output

---

## 2. CTA Harus Action-Oriented

Gunakan kata kerja.

Contoh:
- Buat Caption
- Generate Lagi
- Lihat Premium

Bukan:
- Caption
- Premium Feature

---

## 3. Hindari Ambiguous Labels

User tidak boleh menebak fungsi button.

BAD:
- Lanjut
- Proses
- Jalankan

GOOD:
- Generate Caption
- Kirim Bukti
- Kembali ke Menu

---

# TELEGRAM-SPECIFIC PRINCIPLES

## 1. Inline Keyboard First

Prioritaskan inline keyboard.

Karena:
- lebih cepat
- lebih natural di Telegram
- menjaga chat tetap clean

---

## 2. Jangan Paksa Typing

Jika bisa klik:
jangan suruh user mengetik.

Typing:
= friction tambahan.

---

## 3. Hindari Deep Navigation

Terlalu banyak layer menu:
= user kehilangan arah.

Usahakan:
- flow pendek
- navigation recoverable
- minim nested menu

---

# RETENTION IMPACT

Button hierarchy mempengaruhi:
- comfort
- speed feeling
- user confidence
- momentum
- retention

Button chaos:
= user cepat lelah.

Button jelas:
= user lebih nyaman kembali menggunakan bot.

---

# ANTI-PATTERNS

Hindari:
- terlalu banyak CTA utama
- button ambigu
- row terlalu penuh
- navigation tersembunyi
- CTA bercampur navigation
- wording terlalu technical
- button spam
- menu terlalu dalam
- action penting tenggelam

---

# FINAL DOCTRINE

Good button hierarchy membuat user:
- cepat mengerti
- cepat bergerak
- tidak bingung
- tidak lelah memilih
- tetap nyaman menggunakan bot