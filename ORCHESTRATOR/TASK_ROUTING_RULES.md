# TASK_ROUTING_RULES.md

## PURPOSE

Dokumen ini mendefinisikan aturan dan logika untuk mengarahkan tugas (_routing_) ke agent yang tepat dalam ekosistem PRODUCTIVITY_AI. Tujuannya adalah memastikan setiap task ditangani oleh agent dengan spesialisasi terbaik, menghindari tumpang tindih (_overlap_), dan menjaga alur kerja tetap efisien.

Dokumen ini digunakan oleh:

- MANAGER_ORCHESTRATOR
- TASK_AGENT_OPTIMIZER
- ARCHITECTURE_GUARDIAN

---

## CORE ROUTING MINDSET

Routing bukan sekadar memindah tugas, tapi memastikan **presisi dan efisiensi**.

- **Right Agent, Right Task**: Jangan kirim task UX ke Architecture Guardian.
- **Minimal Hops**: Kurangi jumlah perpindahan tangan antar agent. Setiap perpindahan adalah potensi distorsi informasi.
- **Context Preservation**: Pastikan konteks lengkap ikut dikirim saat routing dilakukan.
- **No Agent is an Island**: Agent bekerja sendiri-sendiri, tapi hasilnya harus terintegrasi sempurna di bawah supervisi Orchestrator.

---

## ROLE SEPARATION PRINCIPLES

Pemisahan peran yang ketat untuk menjaga stabilitas sistem:

1.  **MANAGER_ORCHESTRATOR**: Pengambil keputusan tertinggi, mengawasi seluruh aliran task, dan menangani eskalasi.
2.  **TASK_AGENT_OPTIMIZER**: Fokus pada efisiensi eksekusi task dan perbaikan alur kerja agent.
3.  **PROMPT_ENGINEERING & PROMPT_OPTIMIZER**: Bertanggung jawab atas kualitas instruksi AI, struktur input/output, dan efektivitas prompt.
4.  **ARCHITECTURE_GUARDIAN & ARCHITECTURE_WORKSPACE**: Penjaga struktur kode, integritas file, dan konsistensi arsitektur global.
5.  **UX_RETENTION & INTERACTION_DESIGNER**: Penjaga pengalaman pengguna, psikologi retensi, dan kualitas interaksi Telegram.

---

## SINGLE RESPONSIBILITY ROUTING

Setiap task harus memiliki satu pemilik utama (_Primary Owner_) pada satu waktu.

- Jika sebuah task mengandung elemen UX dan Arsitektur, pecah menjadi dua sub-task.
- Sub-task UX dikirim ke **INTERACTION_DESIGNER**.
- Sub-task Arsitektur dikirim ke **ARCHITECTURE_GUARDIAN**.
- **MANAGER_ORCHESTRATOR** menggabungkan hasilnya.

---

## ROUTING PRIORITY RULES

Urutan prioritas dalam menangani task:

1.  **Security & Stability**: Dikirim langsung ke **ARCHITECTURE_GUARDIAN**.
2.  **Retention & UX Crises**: Dikirim langsung ke **UX_RETENTION**.
3.  **Feature Implementation**: Diarahkan ke agent spesifik sesuai domain fiturnya.
4.  **Refactoring & Optimization**: Diarahkan ke **TASK_AGENT_OPTIMIZER** atau **PROMPT_OPTIMIZER**.

---

## TASK CLASSIFICATION

Kategorisasi task untuk mempermudah routing:

- **Technical/Structural**: Domain **ARCHITECTURE_GUARDIAN**.
- **Interaction/UI**: Domain **INTERACTION_DESIGNER**.
- **Logic/Efficiency**: Domain **TASK_AGENT_OPTIMIZER**.
- **AI/Instructional**: Domain **PROMPT_ENGINEERING**.
- **Strategic/Retention**: Domain **UX_RETENTION**.

---

## WHEN NOT TO ROUTE

Jangan melakukan routing jika:

- Task terlalu sepele (bisa diselesaikan langsung oleh agent saat ini tanpa melanggar batas).
- Konteks tidak mencukupi untuk dipahami oleh agent penerima.
- Terjadi _routing loop_ (task bolak-balik antar agent tanpa progres).
- Agent tujuan sedang dalam status _overload_ atau kritis.

---

## MULTI-AGENT WORKFLOW PRINCIPLES

Alur kerja antar agent harus mengikuti pola:

1.  **Request**: Orchestrator mengirimkan permintaan dengan instruksi jelas.
2.  **Acceptance**: Agent mengonfirmasi pemahaman terhadap task.
3.  **Execution**: Agent bekerja sesuai batas-batasnya (Boundaries).
4.  **Validation**: Hasil divalidasi oleh agent yang meminta atau Orchestrator.
5.  **Integration**: Hasil akhir digabungkan ke dalam codebase utama.

---

## OVERLAP PREVENTION

Cara menghindari tumpang tindih tanggung jawab:

- **Boundary Check**: Setiap agent wajib memeriksa `SYSTEM_BOUNDARIES.md` sebelum memulai kerja.
- **Ownership Conflict Resolution**: Jika dua agent merasa memiliki task yang sama, **MANAGER_ORCHESTRATOR** harus memberikan keputusan final dalam 1 langkah.
- **Strict File Ownership**: Pastikan agent tidak menyentuh file yang ditandai `DO_NOT_TOUCH` atau milik domain agent lain tanpa izin.

---

## ORCHESTRATION ANTI-PATTERNS

Hindari pola-pola buruk ini:

- **Bystander Effect**: Mengirim task ke "semua agent" tanpa menunjuk penanggung jawab utama.
- **The Telepathy Trap**: Berasumsi agent penerima tahu konteks tersembunyi yang tidak tertulis.
- **Micromanagement**: Orchestrator terlalu mencampuri cara kerja internal agent.
- **Ping-Pong Routing**: Task berpindah-pindah tanpa ada penyelesaian nyata.

---

## ESCALATION RULES

Kapan task harus dikembalikan ke **MANAGER_ORCHESTRATOR**:

- Terjadi konflik antar agent yang tidak bisa diselesaikan secara mandiri.
- Task melampaui kapasitas teknis atau hak akses agent saat ini.
- Hasil pekerjaan agent terus-menerus gagal dalam tahap validasi.
- Ada perubahan mendadak pada _Core Project Philosophy_.

---

## HUMAN REVIEW PRINCIPLES

Intervensi manusia (USER) diperlukan jika:

- Terjadi _Deadlock_ pada sistem routing.
- Task menyangkut keputusan strategis tingkat tinggi yang tidak ada di dokumentasi.
- Terjadi error kritis sistemik yang mengancam integritas seluruh project.

---

## FINAL DOCTRINE

Eksosistem AI yang kuat bukan yang memiliki agent terpintar, tapi yang memiliki sistem routing paling disiplin.

"Routing yang tepat adalah jembatan antara ide dan eksekusi. Tanpa routing yang disiplin, AI hanya akan menghasilkan kebisingan, bukan produk."
