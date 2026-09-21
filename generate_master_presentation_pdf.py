import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

brain_dir = r"C:\Users\TIFFANY\.gemini\antigravity\brain\a955b62b-b7a3-4c3d-8c6e-8419c9471b6b"
workspace = r"F:\Antigravity\Illustrator Work"
out_pdf = r"F:\Antigravity\Illustrator Work\Bolivar_2D_Complete_Master_Presentation.pdf"


doc = SimpleDocTemplate(
    out_pdf,
    pagesize=landscape(letter),
    leftMargin=36,
    rightMargin=36,
    topMargin=24,
    bottomMargin=24
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#1A2530'),
    spaceAfter=2
)

desc_style = ParagraphStyle(
    'DescStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=colors.HexColor('#4A5568'),
    spaceAfter=5
)

cover_h1 = ParagraphStyle(
    'CoverH1',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=colors.HexColor('#1A365D')
)

cover_sub = ParagraphStyle(
    'CoverSub',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#2B6CB0')
)

cover_meta = ParagraphStyle(
    'CoverMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13.5,
    textColor=colors.HexColor('#2D3748')
)

story = []

# --- PAGE 1: COVER & EXECUTIVE MILESTONE SUMMARY ---
cover_img_path = os.path.join(brain_dir, "cover_2d_powder_blue_locked_v3.jpg")
cover_img = RLImage(cover_img_path, width=285, height=425)

left_info = [
    Paragraph('<b>BOLÍVAR AND HIS TREASURE</b>', cover_h1),
    Spacer(1, 6),
    Paragraph('<b>Official 2D Storybook Master Reference Presentation</b><br/>Classic Hand-Drawn Watercolor & Ink Style (<i>Curious George</i> & <i>Babar</i> Tradition)', cover_sub),
    Spacer(1, 10),
    Paragraph('<b>Client / Project Lead:</b> Eusebio Landrum (Eusebio L.)<br/>'
              '<b>Author:</b> Benjamin Kiamco<br/>'
              '<b>Illustrator:</b> Hector Sanchez<br/>'
              '<b>Task ID:</b> RemoteGenies RGT6805 (40 hrs base + multi-language scale)', cover_meta),
    Spacer(1, 10),
    Paragraph('<b>Stage 1 & Stage 2 Milestones 100% Completed:</b><br/>'
              '• <b>Official Front Cover:</b> Powder blue park scene, arched "Bolívar" title with acute accent, author "Benjamin Kiamco" (strictly no "by"), calm pond (no boats).<br/>'
              '• <b>Big Papa Model Sheet:</b> 5\'10" slim build, clean-shaven, light warm tan skin, Lotus cap, plaid shirt with NO white undershirt (open collar).<br/>'
              '• <b>Bolívar Model Sheet:</b> 185 lbs English Mastiff, creamy honey-fawn coat, chocolate brown leather collar, red bone tag, right cheek mole, slobber droplets.<br/>'
              '• <b>Friends & Props Sheet:</b> Odin the Saint Bernard (+30 lbs heavier, reddish-brown brindle, freckled muzzle), Laila Great Dane, Lop Bunny, Tiger, WOOF jar.<br/>'
              '• <b>Master Environment Sets (7 Complete Plates):</b> Townhouse Interior, Stoop & Exterior, Avenue Cultural Matrix, The Great Park (with Playground), Streets Near Big Park, Street Views Closer to Home, and Urban High-Rise Corridor.<br/>'
              '• <b>Fidelity Standard:</b> 100% pure native image generation (Zero artificial compositing).', cover_meta),
    Spacer(1, 10),
    Paragraph('<i>Ready for Sequential Story Scene Illustration: Batch 1 (Scenes 1 to 5).</i>', cover_sub)
]

page1_table = Table([[left_info, cover_img]], colWidths=[415, 305])
page1_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))

story.append(page1_table)
story.append(PageBreak())

# --- PAGES 2-11: LANDSCAPE MASTER SHEETS ---
sheets = [
    {
        'id': '2D_MS_01',
        'title': '2D_MS_01: Big Papa Master Character Model Sheet (Clean-Shaven & No Undershirt)',
        'desc': '<b>Locked Features:</b> 5 ft 10 in Normal Build | Clean-Shaven (Smooth Face, No Facial Hair) | Lighter Warm Tan Skin Tone | Small Friendly Eyes | Light Blue Lotus Cap | Coral-Red & Slate-Blue Plaid Western Shirt (<b>NO White Undershirt, Open Collar</b>) | Dark Denim Jeans | Outdoor Boots vs. House Slippers',
        'file': '2d_ms_01_big_papa_master_model_sheet_v2.jpg'
    },
    {
        'id': '2D_MS_02',
        'title': '2D_MS_02: Bolívar Master Character Model Sheet (Creamy Honey-Fawn & Chocolate Brown Collar)',
        'desc': '<b>Locked Features:</b> 185 lbs English Mastiff | <b>Creamy Warm Honey-Fawn Coat</b> (Matched to Swatch) | <b>Dark Chocolate Brown Leather Collar</b> with Red Bone Tag ("Bolívar") | <b>Mole on Anatomical Right Cheek</b> | Charcoal Wrinkled Muzzle Mask | Slobber Dynamics',
        'file': '2d_ms_02_bolivar_master_model_sheet_updated.jpg'
    },
    {
        'id': '2D_MS_03',
        'title': '2D_MS_03: Supporting Friends & Key Props Master Sheet (Odin Refined & Props)',
        'desc': '<b>Locked Features:</b> <b>Odin the Saint Bernard</b> (+30 lbs heavier stockier build, reddish-brown brindle coat, <b>freckles on white muzzle blaze</b>) | Laila the Great Dane | Honey-Brown Lop Bunny | Red Raggedy Stuffed Tiger | Ceramic "WOOF" Cookie Jar & Round Golden Cookies',
        'file': '2d_ms_03_friends_props_master_model_sheet_v2.jpg'
    },
    {
        'id': '2D_ENV_01',
        'title': '2D_ENV_01: Townhouse Interior Master Environment Reference Plate (4-Location Set)',
        'desc': '<b>Master Locations:</b> 1. Living Room & Navy Plush Sofa (Coffee Table & Mug) | 2. Mahogany Open Stairs & White Pantry Door | 3. Center Kitchen Island & "WOOF" Cookie Jar Counter | 4. Master Bedroom with Navy Bedding & Framed Lotus Painting',
        'file': '2d_vis_env_01_townhouse_interior_locked.jpg'
    },
    {
        'id': '2D_ENV_02',
        'title': '2D_ENV_02: Townhouse Exterior & Front Stoop Master Reference Plate',
        'desc': '<b>Master Locations:</b> 1. Front Stoop with 4 Concrete Steps, Black Wrought-Iron Handrails, Dark Entry Door & Lantern | 2. Red Brick Townhouse Facade with Modern Slate-Grey Top Floor & Balcony | 3. Tree-Lined Sidewalk & Street Approach',
        'file': '2d_vis_env_02_townhouse_exterior_stoop_locked.jpg'
    },
    {
        'id': '2D_ENV_03',
        'title': '2D_ENV_03: Neighborhood Avenue & Cultural Matrix Master Reference Plate',
        'desc': '<b>Master Locations:</b> 1. Corner Pizzeria with Striped Awning & Clean "PIZZERIA" Sign (No Flags) | 2. Sports Courts Matrix (Sand Volleyball for EN/ES/ID vs. Basketball for TL) | 3. Cultural Landmarks: <b>Monolithic Tall Building with Neat Window Grid Columns & Rows</b> and Flat Emblems (Shamrock, Butterfly, Sampaguita)',
        'file': '2d_vis_env_03_avenue_and_cultural_matrix_locked_v6.jpg'
    },
    {
        'id': '2D_ENV_04',
        'title': '2D_ENV_04: The Great Park Master Reference Plate (Meadow, Fields & Playground)',
        'desc': '<b>Master Locations:</b> 1. The Great Park Meadow & Calm Blue Pond (Zero Boats) with Shade Trees | 2. Playing Fields Matrix (Baseball Diamond for EN/TL vs. Soccer Pitch for ES/ID) | 3. <b>Children\'s Playground</b> with Red/Green Play Structures, Tubular Slides, Swings & Benches',
        'file': '2d_vis_env_04_great_park_and_downtown_locked.jpg'
    },
    {
        'id': '2D_ENV_05',
        'title': '2D_ENV_05: Streets Near the Big Park Master Reference Plate (Transitional Neighborhood)',
        'desc': '<b>Master Locations:</b> 1. Park Entrance & Flowering Curve (Blooming Wildflower Berm & Low Streetlamps) | 2. Parkside Avenue & Townhouses (Green Park Lawn on Left, Slate-Blue Townhouses on Right) | 3. Crosswalk Intersection & Utility Poles (Wooden Poles, Power Lines, Red Stop Sign & Stone Townhouse)',
        'file': '2d_vis_env_05_streets_near_big_park_locked.jpg'
    },
    {
        'id': '2D_ENV_06',
        'title': '2D_ENV_06: Street Views to Big Park (Closer to Home) Master Reference Plate',
        'desc': '<b>Master Locations:</b> 1. Commercial Glass Frontage & Flags (Limestone Facade, Entry Driveway Ramp, Flower Planters & Mounted Flags) | 2. Avenue Approach to Downtown Skyline (Perspective View with Utility Poles & Cloudscape) | 3. Commercial Storefront & Street Corner with Diagonal Parking',
        'file': '2d_vis_env_06_street_views_closer_to_home_locked.jpg'
    },
    {
        'id': '2D_ENV_07',
        'title': '2D_ENV_07: Urban Corridor & High-Rise Avenue Master Reference Plate',
        'desc': '<b>Master Locations:</b> 1. Bryan St Approach & Park Stone Wall (Stone Retaining Wall, Iron Fence & Columnar Italian Cypress Trees) | 2. Trolley Tracks & Mid-Rise Plaza (Curved Light-Rail Tracks, Circular Tree Planter & Apartment Shops) | 3. Downtown High-Rise Boulevard with Traffic Gantry & Curved Skyscraper Towers',
        'file': '2d_vis_env_07_urban_corridor_highrise_avenue_locked.jpg'
    }
]

for idx, item in enumerate(sheets):
    story.append(Paragraph(item['title'], title_style))
    story.append(Paragraph(item['desc'], desc_style))
    story.append(Spacer(1, 4))
    img_path = os.path.join(brain_dir, item['file'])
    story.append(RLImage(img_path, width=720, height=405))
    if idx < len(sheets) - 1:
        story.append(PageBreak())

story.append(PageBreak())

# --- SCENE PAGES: Batch 1 (Scenes 1–6a) ---
scene_divider_style = ParagraphStyle(
    'SceneDivider',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#1A365D'),
    spaceAfter=6
)

story.append(Paragraph('BATCH 1 SEQUENTIAL STORY SCENES — LOCKED ILLUSTRATIONS', scene_divider_style))
story.append(Paragraph(
    'Pages 7–15 | Scenes 01–06a | Classic 2D Watercolor &amp; Ink Style | Art 4 Feedback Fully Addressed',
    desc_style
))
story.append(Spacer(1, 8))
story.append(PageBreak())

scene_pages = [
    {
        'page': 'Page 7',
        'scene': 'Scene 01a — The Big Morning Hug',
        'desc': '<b>Scene:</b> Big Papa stoops down for a warm morning hug with Bolívar in the living room. '
                '<b>Locked:</b> Mole on anatomical right cheek only (facing left = clean), no white undershirt, lotus cap, plaid shirt.',
        'file': 'page_07_scene_01a_morning_hug_locked.jpg',
        'source': 'workspace',
        'spread': False
    },
    {
        'page': 'Page 8',
        'scene': 'Scene 01b — The Big Sloppy Kiss',
        'desc': '<b>Scene:</b> Bolívar delivers an enthusiastic slobbery kiss to Big Papa\'s face. '
                '<b>Locked:</b> Drool dynamics, honey-fawn coat, dark chocolate collar with red bone tag.',
        'file': 'page_08_scene_01b_the_big_sloppy_kiss_locked.jpg',
        'source': 'workspace',
        'spread': False
    },
    {
        'page': 'Page 9',
        'scene': 'Scene 02 — Morning Pantry Race',
        'desc': '<b>Scene:</b> Big Papa and Bolívar race each other down the hallway toward the pantry in the morning rush. '
                '<b>Locked:</b> Mahogany stairs, white pantry door, plaid shirt (no undershirt).',
        'file': 'page_09_scene_02_v6_1788889089723.jpg',
        'source': 'workspace',
        'spread': False
    },
    {
        'page': 'Page 10',
        'scene': 'Scene 03 — WOOF Cookie Jar',
        'desc': '<b>Scene:</b> Big Papa opens the WOOF cookie jar on the kitchen island while Bolívar sits attentively beside his engraved "Bolívar" food bowl. '
                '<b>Art 4 Feedback Addressed:</b> Plant removed from counter, recessed cabinet squares removed, Big Papa proportions corrected to 5\'10".',
        'file': 'page_10_scene_03_woof_cookie_jar_locked.jpg',
        'source': 'workspace',
        'spread': False
    },
    {
        'page': 'Page 11',
        'scene': 'Scene 04 — First Cookie Toss',
        'desc': '<b>Scene:</b> Big Papa tosses the first cookie into the air toward Bolívar who eagerly leaps for it. '
                '<b>Locked:</b> WOOF jar visible, correct kitchen environment, Bolívar mid-jump.',
        'file': 'page_11_scene_04_first_cookie_toss_locked.jpg',
        'source': 'workspace',
        'spread': False
    },
    {
        'page': 'Pages 12–13 (TWO-PAGE SPREAD)',
        'scene': 'Scene 05 — Mid-Air Cookie Catch (2-Page Widescreen Spread)',
        'desc': '<b>Scene:</b> The dramatic mid-air moment — Bolívar leaps and catches the cookie while Big Papa cheers. Full widescreen 16:9 spread. '
                '<b>Art 4 Feedback Addressed:</b> Big Papa\'s scale corrected to 5\'10".',
        'file': 'pages_12_13_scene_05_spread_locked.jpg',
        'source': 'workspace',
        'spread': True
    },
    {
        'page': 'Page 14',
        'scene': 'Scene 06a — Water Bowl Slurp',
        'desc': '<b>Scene:</b> After the cookie-catch excitement, Bolívar goes to his water bowl for a big satisfying slurp. '
                '<b>Locked:</b> "Bolívar" engraved bowl, kitchen floor level angle, correct environment.',
        'file': 'page_14_scene_06a_water_bowl_slurp_locked.jpg',
        'source': 'workspace',
        'spread': False
    },
]

for idx, sp in enumerate(scene_pages):
    story.append(Paragraph(f'{sp["page"]} | {sp["scene"]}', title_style))
    story.append(Paragraph(sp['desc'], desc_style))
    story.append(Spacer(1, 4))
    img_path = os.path.join(workspace if sp['source'] == 'workspace' else brain_dir, sp['file'])
    # Spreads get wider treatment, single pages fit standard landscape width
    if sp['spread']:
        story.append(RLImage(img_path, width=720, height=405))
    else:
        story.append(RLImage(img_path, width=640, height=480))
    if idx < len(scene_pages) - 1:
        story.append(PageBreak())

doc.build(story)
print("Successfully generated updated master presentation PDF at:", out_pdf)
print("File size (bytes):", os.path.getsize(out_pdf))
