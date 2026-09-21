import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"F:\Antigravity\Illustrator Work\2d_master_model_sheets"
brain_dir = r"C:\Users\TIFFANY\.gemini\antigravity\brain\a955b62b-b7a3-4c3d-8c6e-8419c9471b6b"
os.makedirs(out_dir, exist_ok=True)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 36)
    font_sub = ImageFont.truetype("arialbd.ttf", 18)
    font_card_title = ImageFont.truetype("arialbd.ttf", 20)
    font_bold = ImageFont.truetype("arialbd.ttf", 15)
    font_desc = ImageFont.truetype("arial.ttf", 14)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_card_title = font_title
    font_bold = font_title
    font_desc = font_title

def draw_header(draw, width, title, subtitle):
    draw.rectangle([(0, 0), (width, 95)], fill=(28, 40, 60))
    draw.text((30, 18), title, fill=(255, 255, 255), font=font_title)
    draw.text((30, 62), subtitle, fill=(160, 200, 250), font=font_sub)
    draw.line([(0, 95), (width, 95)], fill=(80, 110, 150), width=2)

def draw_section_card(draw, box, title, lines, fill_col=(255, 255, 255), border_col=(210, 215, 225)):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1, y1, x2, y2], radius=8, fill=fill_col, outline=border_col, width=2)
    draw.rectangle([(x1, y1), (x2, y1 + 36)], fill=(235, 242, 250))
    draw.line([(x1, y1 + 36), (x2, y1 + 36)], fill=border_col, width=1)
    draw.text((x1 + 15, y1 + 8), title, fill=(20, 35, 65), font=font_card_title)
    
    y = y1 + 50
    for line in lines:
        is_bullet = line.startswith("•") or line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.")
        draw.text((x1 + 15, y), line, fill=(40, 50, 65), font=font_bold if is_bullet else font_desc)
        y += 24

# =========================================================================
# SHEET 1: 2D_MS_01 — Big Papa 2D Master Model Sheet (Clean-Shaven & Normal Build)
# =========================================================================
w, h = 1600, 900
s1 = Image.new("RGB", (w, h), (248, 250, 252))
d1 = ImageDraw.Draw(s1)
draw_header(d1, w, "2D_MS_01: Big Papa — 2D Master Character Model Sheet", 
            "Style: Classic 2D Vibrant Storybook (Curious George / Babar / Paddington)  |  Slide 2 Refinements")

draw_section_card(d1, (30, 115, 780, 485), "1. FACIAL FEATURES & HEAD DESIGN", [
    "• Clean-Shaven: Completely free of beard, goatee, or mustache (Slide 2).",
    "• Lighter Skin Tone: Warm light-tan/caramel complexion.",
    "• Natural Eyes: Slightly smaller, friendly expressive cartoon eyes.",
    "• Haircut: Neat short dark taper fade with clean sideburns.",
    "• Signature Cap: Light sky-blue baseball cap with salmon-orange embroidered Lotus flower logo."
])

draw_section_card(d1, (820, 115, 1570, 485), "2. PROPORTIONS & ANATOMY (NORMAL BUILD)", [
    "• Height: 5'10\" adult male proportions.",
    "• Build: Normal / Lean Athletic Build (thinner torso, natural shoulders, not bulky).",
    "• Posture: Warm, gentle, upright fatherly posture.",
    "• Hand Details: Expressive hand-drawn 2D hands for petting Bolivar and holding coffee mug."
])

draw_section_card(d1, (30, 505, 780, 875), "3. SIGNATURE OUTFIT & COLOR PALETTE", [
    "• Shirt: Coral-red (#E05A47) and slate-blue (#4A6B82) plaid checkered button-down shirt.",
    "• Trousers: Comfortable dark navy blue denim jeans (#2B3A4A).",
    "• Cap Color: Light blue (#6CA0DC) with salmon-orange lotus stitching (#FF7052).",
    "• Art Technique: Rich clean 2D ink outlines with vibrant watercolor/gouache fill."
])

draw_section_card(d1, (820, 505, 1570, 875), "4. DUAL FOOTWEAR RULES & TURNAROUND", [
    "• Outdoor Footwear: Brown rugged Timberland-style boots (Scenes 8, 9, 10, 15, 18, 19).",
    "• Indoor Footwear: Comfortable brown house slippers / flip-flops (Scenes 1, 2, 3, 4, 5, 6, 7, 20).",
    "• Turnaround Angles: Front view, 3/4 front view, profile side view, and rear view.",
    "• Strict Continuity Lock: Clean-shaven face and normal build locked for all upcoming scenes."
])

s1.save(os.path.join(out_dir, "2D_MS_01_Big_Papa_Clean_Shaven.jpg"), quality=95)
s1.save(os.path.join(brain_dir, "2D_MS_01_Big_Papa_Clean_Shaven.jpg"), quality=95)
print("Saved 2D_MS_01")

# =========================================================================
# SHEET 2: 2D_MS_02 — Bolívar 2D Master Model Sheet (Right Cheek Mole Lock)
# =========================================================================
s2 = Image.new("RGB", (w, h), (248, 250, 252))
d2 = ImageDraw.Draw(s2)
draw_header(d2, w, "2D_MS_02: Bolívar — 2D Master Character Model Sheet", 
            "Purebred English Mastiff (185 lbs)  |  Style: Classic 2D Vibrant Storybook  |  Slide 3 Refinements")

draw_section_card(d2, (30, 115, 780, 485), "1. ANATOMICAL RIGHT CHEEK MOLE (MANDATORY)", [
    "• Location: Distinct round black mole on his RIGHT cheek (dog's anatomical right side).",
    "• Size Refinement: Smaller, neat, natural mole per Slide 3 feedback.",
    "• Facial Landmarks: Wrinkled brow, floppy dark ears, warm brown expressive doe eyes.",
    "• Muzzle: Droopy black charcoal mask (#2A2A2A) with friendly open-mouth smile.",
    "• Slobber Physics: Cartoon drool droplets during excitement, cookie catch, and hugs."
])

draw_section_card(d2, (820, 115, 1570, 485), "2. SCALE & PROPORTIONS (MASSIVE 185 LBS)", [
    "• Weight: 185 lbs massive English Mastiff build.",
    "• Height: 32 inches at shoulder withers; 5'8\" standing up on hind legs.",
    "• Body Physics: Heavy broad chest, thick powerful legs, massive round paws.",
    "• Coat Color: Rich golden-fawn warm coat (#D8A26A) with smooth 2D shading."
])

draw_section_card(d2, (30, 505, 780, 875), "3. SIGNATURE ACCESSORIES", [
    "• Collar: Bright royal blue leather collar (#1E70BA) fitted comfortably around neck.",
    "• Name Tag: Crimson red metallic dog-bone tag (#D93829) engraved with 'Bolívar'.",
    "• Attachment: Polished silver metallic ring connecting bone tag to blue collar.",
    "• Consistency Rule: Blue collar and red bone tag present in 100% of illustrations."
])

draw_section_card(d2, (820, 505, 1570, 875), "4. ACTION POSES & EMOTIONAL RANGE", [
    "• Pose A (Hero Sitting): Proud, upright sitting pose with wagging tail and happy slobber.",
    "• Pose B (Playful Gallop): Bounding down stairs barking 'Woof!' and leaping for cookies.",
    "• Pose C (Tug-of-War): Playful crouch gripping red raggedy tiger with teeth.",
    "• Pose D (Affectionate Hug): Leaping into Big Papa's arms with giant sloppy kisses."
])

s2.save(os.path.join(out_dir, "2D_MS_02_Bolivar_Right_Mole.jpg"), quality=95)
s2.save(os.path.join(brain_dir, "2D_MS_02_Bolivar_Right_Mole.jpg"), quality=95)
print("Saved 2D_MS_02")

# =========================================================================
# SHEET 3: 2D_MS_03 — Supporting Cast & Props (Lighter Lop Bunny Match)
# =========================================================================
s3 = Image.new("RGB", (w, h), (248, 250, 252))
d3 = ImageDraw.Draw(s3)
draw_header(d3, w, "2D_MS_03: Supporting Friends & Iconic Props — 2D Master Sheet", 
            "Laila, Odin, Lighter Brown Bunny, Red Raggedy Tiger & WOOF Jar  |  Slide 4 Refinements")

draw_section_card(d3, (30, 115, 780, 485), "1. BROWN BUNNY (LIGHTER SHADE REFINEMENT)", [
    "• Color: A shade lighter warm honey/caramel brown (#B88352) per Slide 4 feedback.",
    "• Breed & Features: Holland Lop rabbit with long drooping floppy ears hanging down.",
    "• Body Shape: Chubby, round, cute fluffy body with dark button eyes.",
    "• Story Action: Leaps across baseball diamond leading Bolivar on playful chase."
])

draw_section_card(d3, (820, 115, 1570, 485), "2. LAILA (GREAT DANE) & ODIN (SAINT BERNARD)", [
    "• Laila the Great Dane: Harlequin Great Dane with pure white body and bold irregular black patches, tall pointed ears, slender elegant stature.",
    "• Odin the Saint Bernard: Massive fluffy Saint Bernard with dark reddish-brown brindle coat, white center facial blaze, and friendly open smile."
])

draw_section_card(d3, (30, 505, 780, 875), "3. RAGGEDY STUFFED TIGER", [
    "• Color: Bright vibrant red/orange-red plush toy (#E64228) with bold black stripes.",
    "• Details: White paws and muzzle, stitched patches and button details.",
    "• Prop Role: Bolivar's favorite toy for tug-of-war on the bed with Big Papa."
])

draw_section_card(d3, (820, 505, 1570, 875), "4. 'WOOF' COOKIE JAR & ROUND COOKIES", [
    "• Jar Design: Glossy white ceramic canister with sculpted white ceramic dog-bone handle on lid.",
    "• Typography: Tall black handwritten-style 'WOOF' lettering on front.",
    "• Cookies: Round golden-brown sandwich cookies with embossed patterns."
])

s3.save(os.path.join(out_dir, "2D_MS_03_Supporting_Friends_and_Props.jpg"), quality=95)
s3.save(os.path.join(brain_dir, "2D_MS_03_Supporting_Friends_and_Props.jpg"), quality=95)
print("Saved 2D_MS_03")

# =========================================================================
# SHEET 4: 2D_HERO_COVER — Solo Bolívar Cover Layout (Curious George Format)
# =========================================================================
s4 = Image.new("RGB", (w, h), (248, 250, 252))
d4 = ImageDraw.Draw(s4)
draw_header(d4, w, "2D_HERO_COVER: Official 2D Solo Book Cover Design Sheet", 
            "Style: Classic 2D Vibrant Storybook (Curious George / Paddington)  |  Slide 1 Specifications")

draw_section_card(d4, (30, 115, 780, 485), "1. COVER COMPOSITION & HERO PLACEMENT", [
    "• Solo Hero: Bolivar is prominent and centered on the front cover.",
    "• Remove Big Papa: Big Papa removed from front cover per Slide 1 instructions.",
    "• Hero Pose: Massive Bolivar sitting happily upright, tail wagging, smiling with slobber droplets.",
    "• Accessories: Bright blue collar with red bone tag ('Bolívar'), smaller right-cheek mole."
])

draw_section_card(d4, (820, 115, 1570, 485), "2. BACKGROUND & COLOR PALETTE OPTIONS", [
    "• Background Option A: Iconic bright sunny yellow (#F7D348) classic storybook background.",
    "• Background Option B: Vibrant soft sky blue (#7AB8EB) storybook background.",
    "• Vignette Frame: Large circular white/soft-tint framing around Bolivar (classic Curious George style).",
    "• Mood: Joyful, bright, clean, instantly recognizable on bookshelf and digital stores."
])

draw_section_card(d4, (30, 505, 1570, 875), "3. COVER TITLE & TYPOGRAPHY STANDARDS", [
    "• Main Title: 'Bolívar and His Treasure' (English)  |  'Bolívar dan Harta Karunnya' (Indonesian)  |  'Si Bolívar at ang Kanyang Kayamanan' (Tagalog)  |  'Bolívar y su Tesoro' (Spanish).",
    "• Author Credit: 'by Benjamin Kiamco' (or translated per edition).",
    "• Title Font Style: Friendly, bold, rounded storybook typography with clean readability.",
    "• Publishing Alignment: Ready for print hardcover/paperback and eBook (Kindle/Apple Books)."
])

s4.save(os.path.join(out_dir, "2D_HERO_COVER_Solo_Bolivar_Design.jpg"), quality=95)
s4.save(os.path.join(brain_dir, "2D_HERO_COVER_Solo_Bolivar_Design.jpg"), quality=95)
print("Saved 2D_HERO_COVER")

print("All 4 Master 2D Model Sheets generated successfully!")
