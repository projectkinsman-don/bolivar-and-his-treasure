# ADR-008: Decoupled Environment & Character Generation Pipeline

## Status
Accepted

## Context
Generating complex storybook scenes containing both architecture/environment and active characters in a single AI prompt frequently introduces unintended drift across consecutive pages:
1. **Environment Hallucination:** Minor architectural details (kitchen island width, cabinet recess styles, stairs orientation, window count, lighting fixtures) warp when characters move or change poses.
2. **Character Proportion & Anatomy Shift:** Character heights (e.g., Big Papa's 5'10" scale relative to countertops), clothing details (undershirts appearing, collar styles shifting), and Bolívar's strict mole rules become harder to control when the AI model tries to balance lighting, environment, and complex multi-character anatomy all at once.
3. **High Revision Cost:** Addressing simple client feedback (e.g., "remove plant on counter" or "make Big Papa 10% taller") requires regenerating and re-auditing the entire monolithic image.

## Decision
From Page 15 onwards, we adopt a **Decoupled 3-Stage Layered Generation & Assembly Pipeline** for all sequential story scenes:

### 1. Stage 1: Clean Background Plate Generation / Reuse
- Generate or crop clean, unpopulated environmental background plates directly from locked Master Environment Sheets (`2D_ENV_01` to `2D_ENV_07`).
- Guarantee 100% architectural, perspective, and lighting continuity across all sequential pages in the same room or outdoor avenue.
- Pre-plan 20–30% negative space dedicated to multi-language narration text boxes.

### 2. Stage 2: Character Sprite & Action Isolation
- Generate Big Papa, Bolívar, secondary pets (Odin, Laila, Bunny), and key props (Red Tiger, WOOF jar) individually or in tight character clusters with clean background isolation.
- Rigorously audit character model sheets before compositing:
  - **Big Papa:** 5'10" proportion check, clean-shaven face, Lotus cap, open-collar plaid shirt with **NO white undershirt**.
  - **Bolívar:** 185-lb scale, creamy honey-fawn coat, chocolate collar with red bone tag, and **Strict Directional Mole Rule** (Facing Left = 0% mole; Facing Right = mole visible on right cheek).
  - **Props:** Red raggedy tiger with stitched stripes, correct bone-handled ceramic jar, etc.

### 3. Stage 3: Scale-Accurate Compositing & Blending
- Composite the character layers onto the locked background plate using precise pixel scale anchoring.
- Ground the characters into the scene with watercolor contact shadows and ambient rim lighting matching the environment plate's light source.

## Consequences
- **Absolute Environmental Consistency:** Backgrounds never warp or lose details between consecutive scenes.
- **Flawless Character Anatomy & Scale:** Full control over character heights, postures, and specific facial/clothing requirements.
- **Fast, Modular Edits:** Adjusting a single character's pose, expression, or scale can be done without affecting the environment background.
