# AGENTS.md — Illustrator Work Memory & Navigation Index

Welcome! This repository manages a **50+ Page Children's Book Illustration Project** featuring a large dog and his owner in the classic *Curious George* 2D hand-drawn watercolor art style.

To ensure **absolute character consistency, art style coherence, and project memory** across sessions, follow this Memory Architecture.

---

## 🧠 Memory Layer Structure

| Layer | File / Directory | Purpose |
|---|---|---|
| **1. Master Document** | [`MASTER.md`](file:///f:/Antigravity/Illustrator%20Work/MASTER.md) | Single Source of Truth. Overwritten with latest project state, full page tracker (Pages 1–54+), asset links, and locked specifications. |
| **2. Daily Sessions** | [`DAILY_SESSIONS/`](file:///f:/Antigravity/Illustrator%20Work/DAILY_SESSIONS) | Log of changes happening every day (e.g., `2026-08-08.md`). |
| **3. ADR (Artistic & Architectural Decision Records)** | [`ADR/`](file:///f:/Antigravity/Illustrator%20Work/ADR) | Records capturing key art style, character design, and layout decisions with rationale and trade-offs. |
| **4. Board (Spine)** | [`BOARD.md`](file:///f:/Antigravity/Illustrator%20Work/BOARD.md) | 150 one-liner recent updates & state log. When line count exceeds 150, older items move to [`RIBS.md`](file:///f:/Antigravity/Illustrator%20Work/RIBS.md). |
| **5. Readmes & Guidelines** | [`READMES/`](file:///f:/Antigravity/Illustrator%20Work/READMES) | Master specifications: Character Model Sheets, Art Style Guides, Page Production Pipelines. |

---

## ⚡ Session Checklist for AI / Illustrator
1. **Always read `BOARD.md` and `MASTER.md` first** upon starting a session to catch up on latest project state.
2. **Consult `READMES/character_model_sheet.md`** before generating or approving any artwork to enforce strict character feature matching (eye style, outfit, line weight, dog features).
3. **Log major decisions in `ADR/`** and update `BOARD.md` with one-liner summary.
4. **Log session activities** in `DAILY_SESSIONS/YYYY-MM-DD.md`.
