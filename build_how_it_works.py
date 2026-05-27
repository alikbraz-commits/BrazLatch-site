"""Compose the 5 BrazLatch mechanism frames into one self-explanatory image."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# --- config ---
SRC = Path("src/assets/renders/mechanism")
FRAMES = [SRC / f"{i}.jpg" for i in range(1, 6)]
OUT = Path("how-it-works-composite.png")

# brand
BG = (10, 10, 10)              # brand.black #0a0a0a
WHITE = (255, 255, 255)
GREEN = (126, 217, 87)         # brand.green #7ED957
GREEN_DEEP = (91, 178, 55)     # brand.green-deep #5BB237
MUTED = (165, 165, 165)

FONT_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FONT_MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
FONT_REG = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf"

# layout — 5 frames horizontally
FRAME_W = 520
FRAME_H = 370  # crop so the latch fills the frame more
PAD = 36
GUTTER = 12
HEADER_H = 200
FOOTER_H = 130
LABEL_H = 150

TOTAL_W = PAD * 2 + FRAME_W * 5 + GUTTER * 4
TOTAL_H = HEADER_H + FRAME_H + LABEL_H + FOOTER_H

print(f"Canvas: {TOTAL_W} x {TOTAL_H}")

# --- captions for each step ---
STEPS = [
    ("01", "LOCKED",  "Spring holds the bolt\ninto the staple."),
    ("02", "PUSH",    "Slide the bolt back\nagainst the spring."),
    ("03", "HOLD",    "Pin reaches the\nrelease zone."),
    ("04", "ROTATE",  "Turn the handle\n90° upward."),
    ("05", "OPEN",    "Slide the bolt free.\nGate opens."),
]

# --- build canvas ---
canvas = Image.new("RGB", (TOTAL_W, TOTAL_H), BG)
draw = ImageDraw.Draw(canvas)

# fonts
f_title = ImageFont.truetype(FONT_BOLD, 64)
f_subtitle = ImageFont.truetype(FONT_LIGHT, 26)
f_step_num = ImageFont.truetype(FONT_BOLD, 44)
f_step_label = ImageFont.truetype(FONT_BOLD, 30)
f_step_desc = ImageFont.truetype(FONT_REG, 19)
f_footer = ImageFont.truetype(FONT_MED, 22)
f_footer_small = ImageFont.truetype(FONT_LIGHT, 18)

# --- header ---
title = "HOW BRAZLATCH WORKS"
subtitle = "Patented triple-action mechanism — sequential opening prevents accidental release"
title_bbox = draw.textbbox((0, 0), title, font=f_title)
title_w = title_bbox[2] - title_bbox[0]
sub_bbox = draw.textbbox((0, 0), subtitle, font=f_subtitle)
sub_w = sub_bbox[2] - sub_bbox[0]

draw.text(((TOTAL_W - title_w) / 2, 56), title, fill=WHITE, font=f_title)
draw.text(((TOTAL_W - sub_w) / 2, 138), subtitle, fill=MUTED, font=f_subtitle)

# accent line under header
line_w = 80
draw.rectangle(
    [((TOTAL_W - line_w) / 2, 178), ((TOTAL_W + line_w) / 2, 182)],
    fill=GREEN,
)

# --- frames + labels ---
frame_y = HEADER_H + 10

for i, (frame_path, (num, label, desc)) in enumerate(zip(FRAMES, STEPS)):
    x = PAD + i * (FRAME_W + GUTTER)

    # load frame, crop white space (center crop), resize
    img = Image.open(frame_path).convert("RGB")
    # the latch sits roughly centered; crop a band ~1100w x 450h around the center
    iw, ih = img.size
    # center crop a wider, shorter region to keep the latch visible
    crop_h = int(ih * 0.55)
    top = (ih - crop_h) // 2 + int(ih * 0.05)  # nudge down slightly to center on latch
    crop = img.crop((0, top, iw, top + crop_h))
    # resize to fit
    crop.thumbnail((FRAME_W, FRAME_H), Image.LANCZOS)
    cw, ch = crop.size
    ox = x + (FRAME_W - cw) // 2
    oy = frame_y + (FRAME_H - ch) // 2
    canvas.paste(crop, (ox, oy))

    # --- label area below frame ---
    label_y = frame_y + FRAME_H + 18

    # step number in green
    draw.text((x + 20, label_y), num, fill=GREEN, font=f_step_num)

    # step label (e.g. LOCKED) in white
    num_bbox = draw.textbbox((0, 0), num, font=f_step_num)
    num_w = num_bbox[2] - num_bbox[0]
    draw.text(
        (x + 20 + num_w + 14, label_y + 6),
        label,
        fill=WHITE,
        font=f_step_label,
    )

    # description (two lines)
    desc_y = label_y + 56
    for line in desc.split("\n"):
        draw.text((x + 20, desc_y), line, fill=MUTED, font=f_step_desc)
        desc_y += 24

# --- arrows between frames ---
arrow_y = frame_y + FRAME_H // 2
for i in range(4):
    arrow_x = PAD + (i + 1) * FRAME_W + i * GUTTER + GUTTER // 2
    # simple chevron
    s = 14
    pts = [
        (arrow_x - s // 2, arrow_y - s),
        (arrow_x + s // 2, arrow_y),
        (arrow_x - s // 2, arrow_y + s),
    ]
    draw.line([pts[0], pts[1]], fill=GREEN, width=4)
    draw.line([pts[1], pts[2]], fill=GREEN, width=4)

# --- footer ---
footer_y = TOTAL_H - FOOTER_H + 28
footer_main = "PATENTED IN 7 MARKETS · USA · AUSTRALIA · CANADA · EUROPE · CHINA · INDIA · MEXICO"
footer_url = "BrazLatch™ by Braz Innovation   ·   brazlatch.com   ·   US 10,934,749"

fm_bbox = draw.textbbox((0, 0), footer_main, font=f_footer_small)
fm_w = fm_bbox[2] - fm_bbox[0]
fu_bbox = draw.textbbox((0, 0), footer_url, font=f_footer)
fu_w = fu_bbox[2] - fu_bbox[0]

draw.text(((TOTAL_W - fm_w) / 2, footer_y), footer_main, fill=MUTED, font=f_footer_small)
draw.text(((TOTAL_W - fu_w) / 2, footer_y + 36), footer_url, fill=WHITE, font=f_footer)

# subtle bottom accent
draw.rectangle([(0, TOTAL_H - 6), (TOTAL_W, TOTAL_H)], fill=GREEN_DEEP)

canvas.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({canvas.size[0]}x{canvas.size[1]})")
