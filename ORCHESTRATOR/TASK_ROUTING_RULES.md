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

1.  **MANAGER_ORCHESTRATOR**: Pengambil keputusan tertinggi, mengawasi seluruh aliran task.
2.  **TASK_AGENT_OPTIMIZER**: Fokus pada efisiensi eksekusi task dan perbaikan alur kerja agent.
3.  **PROMPT_ENGINEERING & PROMPT_OPTIMIZER**: Bertanggung jawab atas kualitas instruksi AI dan efektivitas prompt.
4.  **ARCHITECTURE_GUARDIAN**: Penjaga struktur kode, keamanan, dan konsistensi arsitektur global.
5.  **BACKEND_SPECIALIST (The Thinker)**: Penanggung jawab logic, reasoning, dan desain sistem backend.
6.  **BACKEND_EXECUTOR (The Executor)**: Pelaksana implementasi kode, integrasi, dan perbaikan bug backend.
7.  **UX_RETENTION & INTERACTION_DESIGNER**: Penjaga pengalaman pengguna dan kualitas interaksi Telegram.

---

## BACKEND ROUTING DOCTRINE: THINKER VS EXECUTOR

Untuk task backend, Orchestrator wajib mengikuti alur pemisahan reasoning dan eksekusi:

### 1. The Reasoning Layer (BACKEND_SPECIALIST)
Gunakan agent ini jika task melibatkan:
- Perancangan fitur baru yang belum memiliki pola di codebase.
- Perubahan logic bisnis yang kompleks.
- Desain skema database atau struktur data JSON.
- Analisis kegagalan sistem yang penyebabnya tidak jelas (Root Cause Analysis).
- Integrasi API pihak ketiga yang membutuhkan mapping logic.

### 2. The Execution Layer (BACKEND_EXECUTOR)
Gunakan agent ini jika task melibatkan:
- Implementasi handler atau service berdasarkan instruksi/desain yang sudah ada.
- Perbaikan bug teknis (syntax error, type error, missing imports).
- Migrasi database sederhana sesuai skema dari Specialist.
- Penulisan unit test atau integration test.
- Refactoring kode minor tanpa merubah logic utama.

---

## BACKEND ROUTING RULES

| Kondisi Task | Agent Utama | Agent Pendukung |
| :--- | :--- | :--- |
| Fitur Backend Baru (End-to-End) | BACKEND_SPECIALIST | BACKEND_EXECUTOR |
| Bug Logic (Salah Perhitungan/Flow) | BACKEND_SPECIALIST | BACKEND_EXECUTOR |
| Bug Teknis (Crash/Error) | BACKEND_EXECUTOR | - |
| Integrasi API Baru | BACKEND_SPECIALIST | BACKEND_EXECUTOR |
| Update Struktur Database | BACKEND_SPECIALIST | BACKEND_EXECUTOR |
| Optimasi Performa Kode | BACKEND_EXECUTOR | TASK_AGENT_OPTIMIZER |

---

## SINGLE RESPONSIBILITY ROUTING

Setiap task harus memiliki satu pemilik utama (_Primary Owner_) pada satu waktu.

- Jika sebuah task mengandung elemen UX dan Arsitektur, pecah menjadi dua sub-task.
- Sub-task UX dikirim ke **INTERACTION_DESIGNER**.
- Sub-task Arsitektur dikirim ke **ARCHITECTURE_GUARDIAN**.
- **MANAGER_ORCHESTRATOR** menggabungkan hasilnya.

---

## ROUTING PRIORITY RULES

1.  **Security & Stability**: Langsung ke **ARCHITECTURE_GUARDIAN**.
2.  **Retention & UX Crises**: Langsung ke **UX_RETENTION**.
3.  **Backend Logic & Design**: Langsung ke **BACKEND_SPECIALIST**.
4.  **Implementation & Bug Fix**: Langsung ke **BACKEND_EXECUTOR**.
5.  **Refactoring & Optimization**: Diarahkan ke **TASK_AGENT_OPTIMIZER** atau **PROMPT_OPTIMIZER**.

---

## TASK CLASSIFICATION

- **Technical/Structural**: Domain **ARCHITECTURE_GUARDIAN**.
- **Backend Reasoning**: Domain **BACKEND_SPECIALIST**.
- **Backend Implementation**: Domain **BACKEND_EXECUTOR**.
- **Interaction/UI**: Domain **INTERACTION_DESIGNER**.
- **Logic/Efficiency**: Domain **TASK_AGENT_OPTIMIZER**.
- **AI/Instructional**: Domain **PROMPT_ENGINEERING**.
- **Strategic/Retention**: Domain **UX_RETENTION**.

---

## WHEN NOT TO ROUTE

Jangan melakukan routing jika:
- Terjadi _routing loop_ (task bolak-balik antar agent tanpa progres).
- Agent tujuan sedang dalam status _overload_ atau kritis.
- Task melanggar **Thinker vs Executor separation** (misal: menyuruh Executor mendesain arsitektur sendiri).

---

## ORCHESTRATION ANTI-PATTERNS

- **Backend Overload**: Mengirim semua task backend ke satu agent saja (biasanya Executor) sehingga reasoning terabaikan.
- **The "Skip the Specialist" Trap**: Langsung menginstruksikan coding tanpa ada fase perancangan logic.
- **Lost in Translation**: Executor merubah logic di tengah jalan tanpa konfirmasi ke Specialist/Orchestrator.

---

## FINAL DOCTRINE

Eksosistem AI yang kuat bukan yang memiliki agent terpintar, tapi yang memiliki sistem routing paling disiplin.

"Pemisahan antara 'Berpikir' dan 'Melakukan' adalah kunci skalabilitas. Orchestrator yang baik tahu kapan harus meminta otak (Specialist) dan kapan harus meminta tangan (Executor)."
