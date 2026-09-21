# ADR 0002: Project Memory Layer Architecture

- **Status:** Approved
- **Date:** 2026-08-08
- **Context:** Managing 50+ pages of illustrations across multiple working sessions requires a robust multi-tiered memory architecture to prevent loss of context, broken state, or style deviations between sessions.
- **Decision:** Implement 6-Tier Memory Layer System:
  1. `MASTER.md`: Main memory layer (Single Source of Truth, full page tracker).
  2. `DAILY_SESSIONS/`: Daily progress tracking.
  3. `ADR/`: Artistic & architectural decision records.
  4. `BOARD.md` & `RIBS.md`: Rolling 150-line update log & overflow archive.
  5. `READMES/`: Style, character, and pipeline documentation.
  6. `AGENTS.md`: Entry point for all AI sessions.
- **Consequences:** Ensures seamlessly coherent illustrations, clear tracking from page 1 to page 54+, and instant onboarding for any AI session.
