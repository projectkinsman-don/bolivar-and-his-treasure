# ADR 0003: Reference Photo Adaptation & Scenery Replication Pipeline

- **Status:** Approved
- **Date:** 2026-08-09
- **Context:** Client Eusebio L. requested using custom reference photos for the main characters (owner & dog) and specific scenery locations, asking to replicate them accurately into the Curious George watercolor illustration style.
- **Decision:** Establish a 3-Step Photo-to-Illustration Workflow:
  1. **Character Feature Extraction:** Extract distinguishing features (dog breed, fur markings, ear shape, owner's age/hair/glasses/outfits) and create a updated custom Master Character Model Sheet.
  2. **Scenery Stylization:** Translate real-life landmark/scenery photos into 2D hand-drawn watercolor backgrounds maintaining key architectural and landscape landmarks.
  3. **Consistency Lock:** Feed reference photos and custom model sheets as image inputs into all page generations to guarantee 100% resemblance and consistency.
- **Consequences:** Client gets personalized characters and recognizable real-world scenery, while strictly preserving the requested Curious George art aesthetic.
