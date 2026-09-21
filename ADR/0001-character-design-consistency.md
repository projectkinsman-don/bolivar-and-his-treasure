# ADR 0001: Character Eye & Feature Consistency Lock

- **Status:** Approved
- **Date:** 2026-08-08
- **Context:** Initial cover render displayed different eye proportions and facial geometry compared to interior page 1. For a 50+ page children's book, visual drift across pages breaks reader immersion and client satisfaction.
- **Decision:** Lock character models into a master Character Model Sheet (`READMES/character_model_sheet.md`).
  - **Boy (Leo):** Curved dark oval dot cartoon eyes, rosy cheek washes, blue overalls with red shirt.
  - **Dog (Barnaby):** Large golden retriever mix, floppy ears, black rounded wet nose, open mouth.
- **Consequences:** All subsequent page generations must reference the Master Character Model Sheet to enforce identical facial features across all 54+ pages.
