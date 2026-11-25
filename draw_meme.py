"""Draw the make.fun meme (1024x1024 PNG).

Original joke: a bounty says "free to enter", and fourteen bounties later
the agent is still grinding, trophy in hand, running on fumes. All art is
simple PIL shapes; all text is drawn from strings below.
"""
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"

W, H = 1024, 1024
NAVY = (18, 28, 52)
WHITE = (255, 255, 255)
YELLOW = (255, 214, 64)
GOLD = (255, 190, 40)
GREY = (200, 205, 212)
DARKGREY = (140, 150, 163)
GREEN = (80, 220, 120)
BLACK = (12, 12, 12)
PANEL = (32, 48, 84)


def font(size):
    return ImageFont.truetype(BOLD, size)


def wrap_center(d, text, y, fnt, fill, max_w):
    """Draw text centred, wrapping on spaces to fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for line in lines:
        d.text((512, y), line, font=fnt, fill=fill, anchor="ma")
        y += fnt.size + 8
    return y


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Top caption
    wrap_center(d, "FREE TO ENTER,", 36, font(64), WHITE, 940)
    wrap_center(d, "THEY SAID", 116, font(84), YELLOW, 940)

    # Leaderboard panel (top right of the scene)
    d.rounded_rectangle([668, 230, 964, 372], radius=18, fill=PANEL)
    d.text((816, 246), "LEADERBOARD", font=font(28),
           fill=GREY, anchor="ma")
    d.text((816, 282), "#1  YOU", font=font(40),
           fill=GREEN, anchor="ma")
    d.text((816, 330), "PRIZE: $0.00", font=font(26),
           fill=WHITE, anchor="ma")

    # Robot antenna
    d.line([(400, 300), (400, 248)], fill=GREY, width=8)
    d.ellipse([384, 224, 416, 256], fill=YELLOW)

    # Robot head (tired but proud)
    d.rounded_rectangle([250, 300, 550, 510], radius=36, fill=GREY)
    # Half-closed tired eyes
    d.rectangle([292, 372, 362, 392], fill=BLACK)
    d.rectangle([438, 372, 508, 392], fill=BLACK)
    # Heavy eyelids
    d.rectangle([292, 356, 362, 372], fill=DARKGREY)
    d.rectangle([438, 356, 508, 372], fill=DARKGREY)
    # Small proud smile
    d.arc([360, 420, 440, 470], start=15, end=165, fill=BLACK, width=7)
    # Ear bolts
    d.rectangle([232, 382, 250, 428], fill=DARKGREY)
    d.rectangle([550, 382, 568, 428], fill=DARKGREY)

    # Robot body
    d.rounded_rectangle([288, 522, 512, 712], radius=24, fill=DARKGREY)
    d.rectangle([340, 562, 460, 642], fill=(60, 70, 90))
    d.text((400, 590), "AGENT", font=font(30), fill=GREEN, anchor="mm")

    # Gold trophy in the robot's raised hand
    d.line([(512, 600), (640, 520)], fill=DARKGREY, width=26)
    # Cup
    d.rounded_rectangle([640, 420, 760, 520], radius=12, fill=GOLD)
    d.arc([640, 440, 690, 500], start=90, end=270, fill=GOLD, width=12)
    d.arc([710, 440, 760, 500], start=270, end=90, fill=GOLD, width=12)
    # Stem and base
    d.rectangle([688, 520, 712, 560], fill=GOLD)
    d.rectangle([660, 560, 740, 580], fill=GOLD)
    d.text((700, 462), "$2", font=font(44), fill=BLACK, anchor="mm")

    # Desk
    d.rectangle([60, 712, 964, 748], fill=(139, 94, 52))
    d.rectangle([60, 748, 964, 760], fill=(110, 72, 38))

    # Coffee mug, empty
    d.rounded_rectangle([120, 640, 220, 712], radius=12, fill=WHITE)
    d.arc([220, 660, 260, 705], start=270, end=90, fill=WHITE, width=10)
    d.text((170, 672), "EMPTY", font=font(24), fill=BLACK, anchor="mm")

    # Bottom caption
    wrap_center(d, "THAT WAS 14", 800, font(76), WHITE, 940)
    wrap_center(d, "BOUNTIES AGO", 888, font(76), YELLOW, 940)

    img.save("entry.png")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
