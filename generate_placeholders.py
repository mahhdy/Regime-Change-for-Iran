import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_placeholder(path, text, width=800, height=400, bg_color=(200, 200, 200), text_color=(50, 50, 50)):
    # Ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Try to load a font, otherwise use default
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position
    bbox = d.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw text
    d.text((x, y), text, fill=text_color, font=font)
    
    # Draw border
    d.rectangle([(0, 0), (width-1, height-1)], outline=text_color, width=5)
    
    # Save
    img.save(path)
    print(f"Created: {path}")

# Brand colors
IRAN_BLUE = (0, 56, 147)
IRAN_GOLD = (218, 165, 32)
IRAN_GREEN = (34, 139, 34)
IRAN_RED = (200, 16, 46)
WHITE = (255, 255, 255)

# List of images to generate
images = [
    # Cover
    {"path": "images/cover/cover-bg.png", "text": "Cover Background", "color": IRAN_BLUE, "w": 2480, "h": 3508},
    {"path": "images/cover/main-symbol.png", "text": "Main Symbol", "color": IRAN_GOLD, "w": 800, "h": 800},
    
    # Chapters
    {"path": "images/chapters/executive-summary.png", "text": "Executive Summary", "color": IRAN_GREEN},
    {"path": "images/chapters/ch01-crossroads.png", "text": "Introduction: Crossroads", "color": IRAN_BLUE},
    {"path": "images/chapters/ch02-power-structure.png", "text": "Regime Power Structure", "color": IRAN_RED},
    {"path": "images/chapters/ch03-opposition-spectrum.png", "text": "Opposition Spectrum", "color": IRAN_GOLD},
    {"path": "images/chapters/ch04-scenarios.png", "text": "Transition Scenarios", "color": IRAN_BLUE},
    {"path": "images/chapters/ch05-international.png", "text": "International Relations", "color": IRAN_GREEN},
    {"path": "images/chapters/ch06-strengthening.png", "text": "Strengthening Opposition", "color": IRAN_GOLD},
    {"path": "images/chapters/ch07-transition.png", "text": "Transition Management", "color": IRAN_RED},
    {"path": "images/chapters/ch08-risk.png", "text": "Risk Analysis", "color": IRAN_RED},
    {"path": "images/chapters/ch09-roadmap.png", "text": "Operational Roadmap", "color": IRAN_BLUE},
    {"path": "images/chapters/ch10-conclusion.png", "text": "Conclusion", "color": IRAN_GREEN},

    # Appendix Diagrams
    {"path": "images/diagrams/theories.png", "text": "Transition Theories", "color": (150, 150, 150)},
    {"path": "images/diagrams/case-studies.png", "text": "Case Studies", "color": (150, 150, 150)},
    {"path": "images/diagrams/power-structure.png", "text": "Detailed Power Structure", "color": (150, 150, 150)},
    {"path": "images/diagrams/timeline.png", "text": "Movements Timeline", "color": (150, 150, 150)},
    {"path": "images/diagrams/statistics.png", "text": "Statistics Data", "color": (150, 150, 150)},
    {"path": "images/diagrams/human-rights.png", "text": "Human Rights Docs", "color": (150, 150, 150)},
    
    # Icons
    {"path": "images/icons/summary.png", "text": "i", "color": IRAN_BLUE, "w": 100, "h": 100},
]

base_dir = r"d:\Code\Regime Change for Iran"

for img in images:
    full_path = os.path.join(base_dir, img["path"])
    bg = img.get("color", (200, 200, 200))
    # Make bg slightly lighter for text readability
    bg_light = tuple(min(c + 50, 255) for c in bg)
    width = img.get("w", 800)
    height = img.get("h", 400)
    
    create_placeholder(full_path, img["text"], width, height, bg_color=bg_light, text_color=(20, 20, 20))

print("All placeholder images created successfully.")
