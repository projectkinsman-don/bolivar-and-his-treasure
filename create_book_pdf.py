import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

brain_dir = r"C:\Users\TIFFANY\.gemini\antigravity\brain\a955b62b-b7a3-4c3d-8c6e-8419c9471b6b"
output_pdf = r"F:\Antigravity\Illustrator Work\Bolivar_and_His_Treasure_Complete_Book.pdf"

# Landscape Letter: 11 x 8.5 inches (792 x 612 pt)
PAGE_WIDTH, PAGE_HEIGHT = landscape(letter)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        # Skip header/footer on cover page (page 1)
        if self._pageNumber > 1:
            self.saveState()
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#7A6B5D"))
            # Top header
            self.drawString(54, PAGE_HEIGHT - 30, "BOLÍVAR AND HIS TREASURE")
            self.drawRightString(PAGE_WIDTH - 54, PAGE_HEIGHT - 30, "Story by Eusebio L. • Illustrated by Hector")
            
            # Header line
            self.setStrokeColor(colors.HexColor("#D4C7B5"))
            self.setLineWidth(0.75)
            self.line(54, PAGE_HEIGHT - 35, PAGE_WIDTH - 54, PAGE_HEIGHT - 35)
            
            # Bottom footer
            self.setFont("Helvetica", 9)
            self.drawRightString(PAGE_WIDTH - 54, 25, f"Page {self._pageNumber - 1}")
            self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=landscape(letter),
        leftMargin=40,
        rightMargin=40,
        topMargin=45,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=colors.HexColor("#3D2B1F"),
        alignment=1
    )
    
    author_style = ParagraphStyle(
        'CoverAuthor',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#6B5B4D"),
        alignment=1
    )

    story_heading_style = ParagraphStyle(
        'StoryHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#8B4513"),
        spaceAfter=12
    )

    story_body_style = ParagraphStyle(
        'StoryBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=21,
        textColor=colors.HexColor("#2C2621"),
        spaceAfter=12
    )

    story = []

    # ==========================
    # 1. FRONT COVER SPREAD
    # ==========================
    cover_img_path = os.path.join(brain_dir, 'cover_bolivar_and_his_treasure_fresh_1787232645719.jpg')
    cover_img = RLImage(cover_img_path, width=330, height=440)
    
    cover_text = [
        Spacer(1, 20),
        Paragraph("BOLÍVAR AND HIS TREASURE", title_style),
        Spacer(1, 15),
        Paragraph("Written by <b>Eusebio L.</b>", author_style),
        Spacer(1, 6),
        Paragraph("Illustrated by <b>Hector</b>", author_style),
        Spacer(1, 25),
        Paragraph("<i>In the classic Curious George 2D Watercolor Animation Style</i>", ParagraphStyle('Sub', parent=author_style, fontSize=11, fontName='Helvetica-Oblique', textColor=colors.HexColor("#8A7968")))
    ]
    
    cover_table = Table([[cover_img, cover_text]], colWidths=[350, 360])
    cover_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'CENTER'),
        ('LEFTPADDING', (1,0), (1,0), 20),
    ]))
    story.append(cover_table)
    story.append(PageBreak())

    # ==========================
    # 2. STORY SPREADS (PAGES 1 - 9)
    # ==========================
    pages_data = [
        {
            'num': 1,
            'title': 'Scene 1: Introducing Bolívar & BIG Love',
            'image': os.path.join(brain_dir, 'page1_introducing_bolivar_fresh_1787232695950.jpg'),
            'paragraphs': [
                "<b>Bolívar is an English Mastiff.</b> He is a BIG dog.",
                "BIG dogs eat BIG meals, give BIG sloppy kisses, share BIG hugs, and love BIG.",
                "He loves his Big Papa to the moon and back."
            ]
        },
        {
            'num': 2,
            'title': 'Scene 2: Morning Cuddles & The Pantry Race',
            'image': os.path.join(brain_dir, 'page2_pantry_race_fresh_1787233040850.jpg'),
            'paragraphs': [
                "Every morning, after cuddles and kisses, Bolívar races down the stairs to the pantry.",
                "He barks,<br/><b>“Woof! Open the door!”</b>",
                "His paws patter eagerly against the hallway floor."
            ]
        },
        {
            'num': 3,
            'title': 'Scene 3: The “WOOF” Cookie Jar Routine',
            'image': os.path.join(brain_dir, 'page3_cookie_jar_routine_fresh_1787233089338.jpg'),
            'paragraphs': [
                "His eyes sparkle as he watches Big Papa reach for the cookie jar—his treasure chest of yumminess!",
                "By now, Bolívar knows the routine. He sits patiently—well, as patiently as a big, excited dog can—with his tail wagging, jaws drooling, and eyes fixed on the cookie jar."
            ]
        },
        {
            'num': 4,
            'title': 'Scene 4: The First Cookie Toss (Plop!)',
            'image': os.path.join(brain_dir, 'page4_first_cookie_toss_fresh_1787233131900.jpg'),
            'paragraphs': [
                "<b>“Here you go!”</b> Big Papa says.",
                "He tosses a cookie across the kitchen.",
                "<b>Plop!</b> It lands on the rug. Bolívar leaps and snatches it in one bite."
            ]
        },
        {
            'num': 5,
            'title': 'Scene 5: Mid-Air Catch & Gobble! (Whoosh!)',
            'image': os.path.join(brain_dir, 'page5_midair_cookie_catch_fresh_1787233174646.jpg'),
            'paragraphs': [
                "Another cookie flies through the air.",
                "<b>Whoosh!</b> Bolívar sprints to catch it.",
                "<b>Gobble! Gobble! Gulp! Gulp!</b> All gone!"
            ]
        },
        {
            'num': 6,
            'title': 'Scene 6: Turning the Volleyball Court Corner',
            'image': os.path.join(brain_dir, 'page6_volleyball_strict_match_1787235172451.jpg'),
            'paragraphs': [
                "He turns the corner past the volleyball court.",
                "Then he smells something else drifting through the air—<b>sweet coconut coffee</b>.",
                "And there, just a few steps ahead, stands the brick townhouse—home."
            ]
        },
        {
            'num': 7,
            'title': 'Scene 7: Spotting the Brick Townhouse',
            'image': os.path.join(brain_dir, 'page7_spotting_townhouse_strict_match_1787235396033.jpg'),
            'paragraphs': [
                "Bolívar’s eyes grow wide. His long tail lifts high and wags faster and faster.",
                "Big Papa stands at the door holding a large cup of sweet-smelling coffee.",
                "<b>“Bolívar! Bolívar! Come to Papa! I thought I lost you!”</b> Big Papa shouts."
            ]
        },
        {
            'num': 8,
            'title': 'Scene 8: The BIG Mastiff Reunion Hug',
            'image': os.path.join(brain_dir, 'page8_reunion_hug_strict_match_1787235695145.jpg'),
            'paragraphs': [
                "Bolívar races forward and leaps into Big Papa’s arms, giving him the biggest hug and the sloppiest kisses only a BIG English Mastiff can give.",
                "<b>Slurp! Smack! Slurp!</b>",
                "<b>“Woof! Woof! I missed you so much!”</b> Bolívar barks joyfully."
            ]
        },
        {
            'num': 9,
            'title': 'Scene 9: His Greatest Treasure is Home',
            'image': os.path.join(brain_dir, 'page9_greatest_treasure_home_fresh_1787236261386.jpg'),
            'paragraphs': [
                "Only a BIG dog like Bolívar can give such BIG love!",
                "Bolívar once thought treasures were cookies, stuffed toys, or adventures at the Big Park.",
                "But as Big Papa hugs him tightly, Bolívar finally understands.",
                "<b>His greatest treasure—is home.</b>"
            ]
        }
    ]

    for p in pages_data:
        # Illustration on Left (440x330 pt), Text on Right
        img = RLImage(p['image'], width=440, height=330)
        
        text_elements = [
            Paragraph(p['title'], story_heading_style),
            Spacer(1, 10)
        ]
        for para in p['paragraphs']:
            text_elements.append(Paragraph(para, story_body_style))
            text_elements.append(Spacer(1, 4))
        
        table = Table([[img, text_elements]], colWidths=[455, 255])
        table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 18),
            ('RIGHTPADDING', (0,0), (0,0), 5),
        ]))
        story.append(table)
        story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully regenerated storybook PDF: {output_pdf}")

if __name__ == '__main__':
    build_pdf()
