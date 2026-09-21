# ADR-005: Art Generation Fidelity, Pure Illustration Standards, and Zero Artificial Code Compositing

## Status
**Accepted & Mandatory** (2026-09-05)

## Context
During character and model sheet revisions based on client feedback (`Feedback.Art.2.pdf`), an attempt was made to programmatically paste text cards and cropped boxes over artwork using Python/PIL. This created artificial white boxes, broken layout aesthetics, and compromised the organic hand-drawn watercolor quality expected for a professional children's picture book.

## Decision
1. **Zero Artificial Code Compositing Rule:**
   - AI assistant must **NEVER** programmatically paste text boxes, artificial borders, or stitched cards over illustration artwork.
   - All character model sheets, covers, and narrative scenes must be rendered as **100% pure, full-bleed, organic illustrations** matching the classic 2D hand-drawn watercolor and ink storybook style (*Curious George* / *Babar* / *Paddington Bear*).

2. **Immutable User Asset Hierarchy:**
   - Any artwork edited or provided directly by the user (Hector) is the **highest priority ground truth** and must be locked natively in full resolution without alterations or compression.

3. **Strict Scene Consistency Locks (Scenes 1–20):**
   - **Bolívar:** 185 lbs English Mastiff, small mole on anatomical right cheek, chocolate brown collar with red bone tag (*"Bolívar"*), golden-fawn coat, and drool droplets.
   - **Big Papa:** 5'10" normal build, clean-shaven (no facial hair), light blue Lotus cap, plaid shirt with NO white undershirt (natural open collar), brown boots (outdoors) vs slippers (indoors).
   - **Supporting Animals & Props:** Lighter caramel Lop bunny with floppy ears, Odin (+30 lbs with freckles on muzzle), Harlequin Laila, red raggedy tiger, and bone-handle "WOOF" cookie jar.
   - **Narration Typography:** All book narration text must strictly use **Quicksand Bold** at uniform sizing.

4. **Publisher-Grade Visual Quality Control:**
   - Every generated asset must be evaluated through the lens of a professional children's book art director for warmth, seamless textures, correct lighting, and emotional storytelling appeal.

## Consequences
- Guarantees clean, authentic, publisher-ready illustrations across all 20 story scenes.
- Eliminates clunky programmatic visual artifacts.
- Enforces strict character and environmental consistency across all 4 language editions.
