# TASK_PRIORITY_SYSTEM.md

## PURPOSE

Dokumen ini mendefinisikan sistem prioritas tugas dalam ekosistem PRODUCTIVITY_AI. Tujuannya adalah membantu Orchestrator dalam mengambil keputusan yang tepat untuk memilih tugas mana yang harus diselesaikan terlebih dahulu guna menjaga stabilitas sistem dan momentum pertumbuhan tanpa menciptakan kekacauan operasional.

Dokumen ini digunakan oleh:

- MANAGER_ORCHESTRATOR
- TASK_AGENT_OPTIMIZER
- ARCHITECTURE_GUARDIAN

---

## CORE PRIORITIZATION MINDSET

Prioritas bukan tentang mengerjakan semuanya, tapi tentang **memilih apa yang harus dikorbankan hari ini demi keamanan esok hari**.

- **Stability is Non-Negotiable**: Keamanan dan stabilitas sistem selalu mendahului fitur baru.
- **Velocity through Clarity**: Kecepatan development hanya bisa dicapai jika prioritasnya jelas. Tanpa prioritas, kecepatan hanyalah kebisingan.
- **Ecosystem Health Over Feature Count**: Lebih baik memiliki 3 fitur yang stabil dan retensinya tinggi daripada 10 fitur yang merusak pengalaman pengguna atau integritas kode.

---

## URGENT VS IMPORTANT DOCTRINE

Membedakan antara api yang harus segera dipadamkan dan fondasi yang harus diperkuat:

- **Urgent (Mendesak)**: Masalah yang menghentikan fungsi utama bot, kebocoran data, atau error kritis di production. Harus dikerjakan sekarang.
- **Important (Penting)**: Refactoring kode untuk skalabilitas, optimasi prompt untuk retensi, dan pembersihan _technical debt_. Harus dijadwalkan secara konsisten.
- **The Trap**: Terlalu fokus pada hal mendesak akan membuat kita kehilangan arah strategis. Orchestrator harus mendedikasikan minimal 30% resource untuk hal "Penting" meskipun tidak "Mendesak".

---

## ARCHITECTURE RISK PRIORITY

Prioritas tertinggi diberikan pada tugas yang memitigasi risiko sistemik:

1.  **Security Patches**: Menutup celah akses atau kebocoran API Key.
2.  **Structural Integrity**: Memperbaiki dependensi yang melingkar (_circular dependencies_) atau file yang terlalu besar (_God files_).
3.  **Data Consistency**: Memastikan integritas database dan sinkronisasi status antar agent.

---

## UX/RETENTION PRIORITY RULES

Dari sisi pengalaman pengguna, urutan prioritasnya adalah:

1.  **Crash/Bug Fix**: Menghilangkan error yang membuat bot berhenti merespons.
2.  **Friction Reduction**: Memperbaiki alur navigasi yang membuat user bingung (berdasarkan `USER_FATIGUE_SIGNALS.md`).
3.  **New Value Implementation**: Penambahan fitur baru yang meningkatkan retensi (berdasarkan `COMEBACK_PATTERNS.md`).

---

## SCALABILITY PRIORITY

Kapan skalabilitas menjadi prioritas utama?

- Saat jumlah user meningkat drastis melebihi batas performa database saat ini.
- Saat respon AI menjadi sangat lambat karena optimasi prompt yang buruk.
- Saat orkestrasi antar agent mulai sering mengalami _deadlock_.

---

## TECHNICAL DEBT HANDLING

Hutang teknis harus dicicil secara proaktif:

- Jangan biarkan hutang teknis menumpuk hingga melumpuhkan kemampuan sistem untuk menambah fitur baru.
- Setiap implementasi fitur baru wajib menyertakan minimal 1 langkah pembersihan kode lama (_Boy Scout Rule_).

---

## DANGEROUS LONG-TERM FILES

File yang harus diawasi ketat karena risikonya terhadap prioritas:

- `main.py` atau `config.py` yang terus membengkak.
- `keyboards/` yang memiliki logika bercabang terlalu dalam.
- State management yang tidak terstandarisasi.

Tugas untuk merapikan file-file ini harus selalu masuk dalam daftar prioritas "Penting".

---

## MOMENTUM PRESERVATION

Menjaga ritme development agar tidak stagnan:

- Selesaikan tugas-tugas kecil yang memberikan _quick win_ di antara tugas besar yang berat.
- Hindari mengerjakan terlalu banyak tugas besar (Epic) secara bersamaan yang bisa menyebabkan fragmentasi fokus.

---

## ANTI-CHAOS PRIORITIZATION

Untuk mencegah kekacauan orkestrasi:

- Berhenti sejenak jika agent mulai sering melakukan routing bolak-balik tanpa hasil (_Ping-pong routing_).
- Prioritaskan perbaikan pada `TASK_ROUTING_RULES.md` jika terjadi kebingungan peran antar agent.

---

## WHEN NOT TO PRIORITIZE

Jangan memaksakan prioritas tinggi jika:

- Informasi/konteks tugas belum lengkap.
- Agent spesialis yang dibutuhkan sedang menangani tugas kritis lain yang lebih berisiko.
- Tugas tersebut hanya berdasarkan "feeling" tanpa data retensi atau analisis arsitektur yang kuat.

---

## ANTI-PATTERNS

- **Squeaky Wheel Syndrome**: Mendahulukan tugas hanya karena "paling sering dibahas", bukan karena paling berdampak.
- **Feature Hoarding**: Terus menambah fitur baru padahal fondasi sistem sedang goyah.
- **Ignoring Fatigue**: Mengabaikan sinyal kelelahan user demi mengejar deadline rilis fitur teknis.

---

## ESCALATION RULES

Naikkan prioritas ke level "Kritis" jika:

- Peningkatan silent churn yang signifikan.
- Architecture Guardian memberikan peringatan keras tentang potensi kerusakan permanen codebase.
- Interaksi bot melanggar batas-batasan keamanan dasar.

---

## FINAL DOCTRINE

Menentukan prioritas adalah seni menjaga keseimbangan antara kecepatan dan keberlanjutan.

"Tugas yang paling penting bukanlah yang paling keras berteriak, tapi yang paling dalam fondasinya bagi masa depan ekosistem."
