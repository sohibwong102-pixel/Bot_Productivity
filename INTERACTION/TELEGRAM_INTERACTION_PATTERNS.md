# TELEGRAM_INTERACTION_PATTERNS.md

## PURPOSE

Dokumen ini berisi pattern dan prinsip interaction khusus untuk platform Telegram dalam ecosystem PRODUCTIVITY_AI.

Telegram memiliki behavior user yang berbeda dibanding:
- web app
- mobile app
- desktop software

Karena itu interaction harus mengikuti:
- kebiasaan user Telegram
- speed expectation Telegram
- conversational flow Telegram

Dokumen ini digunakan oleh:
- INTERACTION_DESIGNER
- UX_RETENTION

---

# CORE TELEGRAM MINDSET

Telegram adalah:
- cepat
- ringan
- conversational
- action-oriented

User Telegram terbiasa:
- klik cepat
- scroll cepat
- membaca singkat
- interaction instan

Interaction yang terlalu berat:
akan terasa melelahkan.

---

# MAIN TELEGRAM PATTERNS

## 1. Inline Keyboard First

Prioritaskan:
inline keyboard dibanding text command.

Karena:
- lebih cepat
- lebih natural
- mengurangi typing friction
- menjaga flow tetap ringan

Typing hanya digunakan jika memang diperlukan.

---

## 2. Minim Typing

Typing adalah friction.

Jika action bisa diselesaikan dengan:
- button
- quick choice
- selection flow

maka hindari meminta user mengetik manual.

---

## 3. Fast Interaction Feeling

Telegram user mengharapkan:
- respons cepat
- movement cepat
- minim loading feeling

Walaupun backend lambat:
interaction harus tetap terasa hidup.

Gunakan:
- acknowledgement
- loading indicator
- progress feeling

---

## 4. Compact Message Structure

User Telegram tidak suka:
- dinding text panjang
- paragraph berat
- informasi tanpa hierarchy

Gunakan:
- spacing
- hierarchy
- short blocks
- focused information

---

## 5. Edit Message Carefully

Message edit membantu:
- menjaga chat tetap clean
- mengurangi spam message

Tetapi:
jangan overuse.

Terlalu banyak edit:
- membuat user bingung
- kehilangan context
- interaction terasa aneh

Gunakan edit jika:
- masih dalam flow yang sama
- context belum berubah besar

---

## 6. Avoid Chat Pollution

Hindari:
- spam message
- message tidak penting
- duplicate notification
- callback spam

Chat yang terlalu penuh:
menurunkan kenyamanan user.

---

## 7. Navigation Harus Cepat Dipahami

Telegram interaction bersifat:
- cepat
- impulsif
- short attention

User harus langsung tahu:
- harus klik apa
- posisi mereka dimana
- next step apa

---

## 8. One Action Momentum

Setelah user klik:
jangan langsung bombardir banyak pilihan baru.

Biarkan flow:
- mengalir
- bertahap
- ringan

---

## 9. Conversational UX

Bot tidak boleh terasa seperti:
- dashboard kaku
- form panjang
- sistem enterprise dingin

Interaction harus terasa:
- natural
- ringan
- conversational
- manusiawi

---

## 10. Telegram User Tidak Sabar

Semakin lama:
- loading
- flow panjang
- langkah banyak

semakin tinggi kemungkinan user keluar.

Prioritaskan:
- quick win
- fast completion
- instant usefulness

---

# TELEGRAM UI PRINCIPLES

## 1. Prioritaskan Readability

Gunakan:
- spacing
- hierarchy
- emoji seperlunya
- compact formatting

Hindari:
- visual noise
- emoji berlebihan
- text terlalu padat

---

## 2. CTA Harus Obvious

Button penting harus:
- jelas
- singkat
- mudah dipahami

Telegram user tidak suka:
menebak fungsi button.

---

## 3. Jangan Paksa User Belajar Sistem

Flow harus:
- intuitif
- predictable
- natural

User tidak boleh perlu:
“mempelajari cara menggunakan bot.”

---

# RETENTION IMPACT

Telegram interaction yang baik:
- terasa ringan
- terasa cepat
- terasa nyaman
- terasa hidup

Dan itu meningkatkan:
- user comeback
- interaction frequency
- engagement
- retention

---

# ANTI-PATTERNS

Hindari:
- typing berlebihan
- spam message
- callback chaos
- nested navigation terlalu dalam
- text terlalu panjang
- button overload
- dashboard mentality
- flow lambat
- interaction dingin
- visual terlalu ramai

---

# FINAL DOCTRINE

Telegram bukan platform untuk interaction berat.

Good Telegram interaction adalah:
- cepat
- ringan
- jelas
- natural
- conversational

Semakin kecil effort user untuk bergerak:
semakin baik experience Telegram bot.