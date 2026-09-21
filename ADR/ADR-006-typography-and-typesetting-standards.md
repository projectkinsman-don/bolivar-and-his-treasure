# ADR-006: Book Typography & Interior Typesetting Standards

## Status
**Accepted & Mandatory** (2026-09-05)

## Context
Client feedback from Eusebio (`media_1788618720028.png` / `Feedback.Art.2.pdf`) established strict rules for cover and interior narration fonts to ensure brand coherence, maximum readability for young readers, and consistent visual polish across all English and multilingual book editions.

---

## Decisions

### 1. Interior Story Narration Font: Quicksand Bold
* **Primary Narration Font:** All narrative text throughout the interior book pages must strictly use **Quicksand Bold**.
* **Uniform Font Size:** Font size must remain consistent and uniform across all pages and paragraphs.
* **Italicization Rule:** When sentences or words are italicized (e.g., *They are going for a walk to the Big Park.*), the font size **must remain identical** to the non-italicized body text (no size scaling or shrinkage).
* **Sample Text Baseline:**
  > "He is a **BIG** dog.  
  > **BIG** dogs eat **BIG** meals,  
  > give **BIG** sloppy kisses,  
  > give **BIG** hugs,  
  > and love **BIG**.  
  > He loves his Big Papa to the moon and back.  
  > Bolívar races down..."

### 2. Cover Title Typography: Baloo 2 Extra Bold
* **Title Font:** **Baloo 2 Extra Bold** (rounded, friendly storybook display font).
* **Title Color:** Solid warm golden-yellow (`#FFD700`) with clean dark outline.
* **Exact Title Spelling:** Must strictly include the Spanish acute accent: **"Bolívar and His Treasure"** (never unaccented "Bolivar").
* **Curvature:** Arched cleanly along the upper arc of the compass rose vignette.

### 3. Author Name Credit
* **Text Format:** Strictly **"Benjamin Kiamco"** (do **NOT** prefix with "by").
* **Placement:** Centered horizontally at the bottom center of the front cover.

---

## Consequences
* Guarantees consistent typographical hierarchy and reader legibility across all pages.
* Prevents font discrepancies between different scenes and language editions.
* Locks font rules permanently in the project memory architecture for any future page rendering and PDF compilation.
