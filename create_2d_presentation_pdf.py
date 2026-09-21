import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

brain_dir = r"C:\Users\TIFFANY\.gemini\antigravity\brain\a955b62b-b7a3-4c3d-8c6e-8419c9471b6b"
out_pdf = r"F:\Antigravity\Illustrator Work\Bolivar_2D_Illustrated_Master_Model_Sheets_Presentation.pdf"

f_papa = os.path.join(brain_dir, "2d_ms_01_big_papa_master_model_sheet_1788533377168.jpg")
f_bolivar = os.path.join(brain_dir, "2d_ms_02_bolivar_master_model_sheet_locked.jpg")
f_friends = os.path.join(brain_dir, "2d_ms_03_friends_props_master_model_sheet_1788533455487.jpg")
f_cover = os.path.join(brain_dir, "cover_2d_bolivar_solo_yellow_locked.jpg")

doc = SimpleDocTemplate(out_pdf, pagesize=landscape(letter), leftMargin=36, rightMargin=36, topMargin=25, bottomMargin=25)
styles = getSampleStyleSheet()

cap_title = ParagraphStyle(
    'CapTitle',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=15,
    leading=19,
    textColor=colors.HexColor('#1A2530'),
    alignment=0
)

cap_desc = ParagraphStyle(
    'CapDesc',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13,
    textColor=colors.HexColor('#4A5568'),
    alignment=0
)

story = []

# Page 1: Official Solo Cover (Lighter Fawn & Chocolate Brown Collar)
story.append(Paragraph('2D_COVER: Official 2D Solo Book Cover (Yellow Circle Master)', cap_title))
story.append(Paragraph('<b>Locked Cover Specifications:</b> Bolivar Solo in Center White Circle on Bright Yellow Background (#FFD700) | <b>Lighter Honey-Fawn Coat</b> | <b>Chocolate Brown Collar</b> + Red Tag | Mole on Right Cheek | Slobber Droplets', cap_desc))
story.append(Spacer(1, 8))
story.append(RLImage(f_cover, width=270, height=402))
story.append(PageBreak())

# Page 2: Big Papa 2D Model Sheet
story.append(Paragraph('2D_MS_01: Big Papa Master Character Model Sheet (Clean-Shaven & Normal Build)', cap_title))
story.append(Paragraph('<b>Locked Features:</b> 5 ft 10 in Normal Build | Clean-Shaven (No Facial Hair) | Lighter Warm Tan Skin | Lotus Cap | Plaid Shirt | Boots vs Slippers', cap_desc))
story.append(Spacer(1, 8))
story.append(RLImage(f_papa, width=720, height=402))
story.append(PageBreak())

# Page 3: Bolívar 2D Model Sheet (Lighter Fawn & Chocolate Brown Collar)
story.append(Paragraph('2D_MS_02: Bolivar Master Character Model Sheet (Lighter Fawn & Chocolate Brown Collar)', cap_title))
story.append(Paragraph('<b>Locked Features (Slide 5 Feedback):</b> <b>Tint Lighter Honey-Fawn Coat</b> | <b>Chocolate Brown Leather Collar</b> & Red Bone Tag ("Bolivar") | <b>Mole on Right Cheek</b> | Drooling Slobber Dynamics', cap_desc))
story.append(Spacer(1, 8))
story.append(RLImage(f_bolivar, width=720, height=405))
story.append(PageBreak())

# Page 4: Supporting Friends & Props 2D Sheet
story.append(Paragraph('2D_MS_03: Supporting Friends & Props Master Sheet (Lighter Lop Bunny Match)', cap_title))
story.append(Paragraph('<b>Locked Features:</b> Lighter Caramel Lop Bunny | Harlequin Great Dane Laila | Brindle Saint Bernard Odin | Red Raggedy Tiger | Bone-Handle WOOF Jar', cap_desc))
story.append(Spacer(1, 8))
story.append(RLImage(f_friends, width=720, height=402))

doc.build(story)
print("Rebuilt presentation PDF successfully at:", out_pdf)
