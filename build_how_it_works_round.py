"""
Round/triangular BrazLatch how-it-works diagram (v2 — clean arrows).

Three action nodes in a triangle (PUSH at top, ROTATE bottom-right, OPEN bottom-left)
with curved arrows on the OUTSIDE flowing clockwise, plus a dashed amber AUTO-RESET arc
returning from OPEN back to the start. Central circle shows the auto-lock behaviour.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

# --- config ---
SRC = Path("src/assets/renders/mechanism")
OUT = Path("how-it-works-round.png")

# brand
BG = (10, 10, 10)
WHITE = (255, 255, 255)
GREEN = (126, 217, 87)
GREEN_DEEP = (91, 178, 55)
AMBER = (245, 158, 11)
MUTED = (165, 165, 165)
PANEL = (22, 22, 22)

FONT_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FONT_MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
FONT_REG = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf"

# canvas — square for circular layout
W = H = 1500
canvas = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(canvas)

# fonts
f_title = ImageFont.truetype(FONT_BOLD, 56)
f_subtitle = ImageFont.truetype(FONT_LIGHT, 24)
f_action_num = ImageFont.truetype(FONT_MED, 17)
f_action_label = ImageFont.truetype(FONT_BOLD, 42)
f_action_desc = ImageFont.truetype(FONT_REG, 18)
f_reset_kicker = ImageFont.truetype(FONT_MED, 18)
f_reset_label = ImageFont.truetype(FONT_BOLD, 40)
f_reset_desc = ImageFont.truetype(FONT_REG, 16)
f_arrow_label = ImageFont.truetype(FONT_MED, 20)
f_arrow_label_sub = ImageFont.truetype(FONT_REG, 16)
f_footer = ImageFont.truetype(FONT_MED, 20)
f_footer_small = ImageFont.truetype(FONT_LIGHT, 16)

# --- header ---
title = "HOW BRAZLATCH WORKS"
subtitle = "Three deliberate actions to open. One automatic action to lock."
tb = draw.textbbox((0, 0), title, font=f_title)
draw.text(((W - (tb[2] - tb[0])) / 2, 60), title, fill=WHITE, font=f_title)
sb = draw.textbbox((0, 0), subtitle, font=f_subtitle)
draw.text(((W - (sb[2] - sb[0])) / 2, 130), subtitle, fill=MUTED, font=f_subtitle)
draw.rectangle([(W // 2 - 40, 170), (W // 2 + 40, 174)], fill=GREEN)

# --- node positions (equilateral triangle around center) ---
cx, cy = W // 2, 830
radius = 380
node_centers = [
    (cx, cy - radius),                                                                                  # PUSH (top)
    (cx + int(radius * math.sin(math.radians(120))), cy + int(radius * math.cos(math.radians(60)))),  # ROTATE (bottom-right)
    (cx - int(radius * math.sin(math.radians(120))), cy + int(radius * math.cos(math.radians(60)))),  # OPEN (bottom-left)
]

# --- node panels ---
NODE_W = 360
NODE_H = 310
IMG_H = 160
PANEL_RADIUS = 14

actions = [
    ("ACTION 01", "PUSH",   "Slide the bolt back against\nthe spring force.",   SRC / "3.jpg"),
    ("ACTION 02", "ROTATE", "Turn the handle 90°\nclear of the channel.",       SRC / "4.jpg"),
    ("ACTION 03", "OPEN",   "Slide the bolt free.\nGate opens.",                SRC / "5.jpg"),
]

def draw_panel(d, x1, y1, x2, y2, fill, border=None, border_w=2, r=14):
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill)
    if border:
        d.rounded_rectangle([x1, y1, x2, y2], radius=r, outline=border, width=border_w)


# ------ Arrow helpers ------

def quad_bezier_pts(p1, ctrl, p2, n=80):
    pts = []
    for s in range(n + 1):
        t = s / n
        x = (1 - t) ** 2 * p1[0] + 2 * (1 - t) * t * ctrl[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p1[1] + 2 * (1 - t) * t * ctrl[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

def draw_solid_curve(d, pts, color, width=6):
    d.line(pts, fill=color, width=width, joint="curve")

def draw_dashed_curve(d, pts, color, width=4, dash=14, gap=10):
    accumulated = 0
    drawing = True
    seg = [pts[0]]
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        step = math.hypot(dx, dy)
        accumulated += step
        if drawing:
            seg.append(pts[i + 1])
        target = dash if drawing else gap
        if accumulated >= target:
            if drawing and len(seg) > 1:
                d.line(seg, fill=color, width=width, joint="curve")
            seg = [pts[i + 1]]
            drawing = not drawing
            accumulated = 0
    if drawing and len(seg) > 1:
        d.line(seg, fill=color, width=width, joint="curve")

def draw_arrowhead(d, tip, prev_pt, color, size=22):
    angle = math.atan2(tip[1] - prev_pt[1], tip[0] - prev_pt[0])
    h1 = (tip[0] - size * math.cos(angle - math.pi / 7),
          tip[1] - size * math.sin(angle - math.pi / 7))
    h2 = (tip[0] - size * math.cos(angle + math.pi / 7),
          tip[1] - size * math.sin(angle + math.pi / 7))
    d.polygon([tip, h1, h2], fill=color)

def edge_offset(from_node, to_node, offset=NODE_W // 2 + 24):
    """Point on the line from from_node toward to_node, just outside the from_node panel."""
    fx, fy = from_node
    tx, ty = to_node
    dx, dy = tx - fx, ty - fy
    dist = math.hypot(dx, dy) or 1
    return (fx + dx / dist * offset, fy + dy / dist * offset)

def perpendicular_outward(p1, p2, center, magnitude):
    """Unit perpendicular pointing AWAY from center."""
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    # decide which side is away from center
    if (mx + nx - center[0]) ** 2 + (my + ny - center[1]) ** 2 < (mx - nx - center[0]) ** 2 + (my - ny - center[1]) ** 2:
        nx, ny = -nx, -ny
    return mx + nx * magnitude, my + ny * magnitude


# ------ Forward arrows: PUSH -> ROTATE -> OPEN (solid green, curved outward) ------
center = (cx, cy)
bow_out = 90  # how far the curve bows outward from the straight line

forward_pairs = [
    (0, 1),  # PUSH -> ROTATE
    (1, 2),  # ROTATE -> OPEN
]
for i, (a_idx, b_idx) in enumerate(forward_pairs):
    a = node_centers[a_idx]
    b = node_centers[b_idx]
    p1 = edge_offset(a, b, offset=NODE_W // 2 + 30)
    p2 = edge_offset(b, a, offset=NODE_W // 2 + 30)
    ctrl = perpendicular_outward(p1, p2, center, bow_out)
    pts = quad_bezier_pts(p1, ctrl, p2)
    draw_solid_curve(draw, pts, GREEN, width=6)
    draw_arrowhead(draw, pts[-1], pts[-5], GREEN, size=22)

# ------ Reset arrow: OPEN -> PUSH (dashed amber, big bow on the LEFT side) ------
a = node_centers[2]  # OPEN
b = node_centers[0]  # PUSH
p1 = edge_offset(a, b, offset=NODE_W // 2 + 30)
p2 = edge_offset(b, a, offset=NODE_W // 2 + 30)
ctrl = perpendicular_outward(p1, p2, center, 130)
pts = quad_bezier_pts(p1, ctrl, p2)
draw_dashed_curve(draw, pts, AMBER, width=5, dash=16, gap=10)
draw_arrowhead(draw, pts[-1], pts[-5], AMBER, size=22)

# AUTO-RESET label on the dashed curve (midpoint)
mid_idx = len(pts) // 2
mx, my = pts[mid_idx]
label_main = "AUTO-RESET"
label_sub = "stop mid-sequence — spring locks"
lm_w = draw.textbbox((0, 0), label_main, font=f_arrow_label)[2]
ls_w = draw.textbbox((0, 0), label_sub, font=f_arrow_label_sub)[2]
box_w = max(lm_w, ls_w) + 32
box_h = 64
# place label box just to the left of the curve midpoint
bx1 = int(mx) - box_w - 24
by1 = int(my) - box_h // 2
draw.rounded_rectangle([bx1, by1, bx1 + box_w, by1 + box_h], radius=10, fill=(35, 25, 10), outline=AMBER, width=1)
draw.text((bx1 + 16, by1 + 6), label_main, fill=AMBER, font=f_arrow_label)
draw.text((bx1 + 16, by1 + 34), label_sub, fill=MUTED, font=f_arrow_label_sub)


# ------ Draw the 3 action nodes (on top of arrows) ------
for (label_num, label, desc, frame_path), (nx, ny) in zip(actions, node_centers):
    x1, y1 = nx - NODE_W // 2, ny - NODE_H // 2
    x2, y2 = nx + NODE_W // 2, ny + NODE_H // 2

    draw_panel(draw, x1, y1, x2, y2, fill=PANEL, border=GREEN, border_w=2, r=PANEL_RADIUS)

    img = Image.open(frame_path).convert("RGB")
    iw, ih = img.size
    crop_h = int(ih * 0.55)
    top = (ih - crop_h) // 2 + int(ih * 0.05)
    crop = img.crop((0, top, iw, top + crop_h))
    target_w = NODE_W - 30
    target_h = IMG_H
    crop.thumbnail((target_w, target_h), Image.LANCZOS)
    cw, ch = crop.size
    ox = x1 + (NODE_W - cw) // 2
    oy = y1 + 12
    canvas.paste(crop, (ox, oy))

    text_y = y1 + IMG_H + 22
    nb = draw.textbbox((0, 0), label_num, font=f_action_num)
    nw = nb[2] - nb[0]
    draw.text((nx - nw // 2, text_y), label_num, fill=GREEN, font=f_action_num)

    lb = draw.textbbox((0, 0), label, font=f_action_label)
    lw = lb[2] - lb[0]
    draw.text((nx - lw // 2, text_y + 22), label, fill=WHITE, font=f_action_label)

    desc_y = text_y + 80
    for line in desc.split("\n"):
        db = draw.textbbox((0, 0), line, font=f_action_desc)
        dw = db[2] - db[0]
        draw.text((nx - dw // 2, desc_y), line, fill=MUTED, font=f_action_desc)
        desc_y += 22

# ------ Central RESET circle (on top of everything) ------
center_r = 145
draw.ellipse(
    [cx - center_r - 8, cy - center_r - 8, cx + center_r + 8, cy + center_r + 8],
    outline=GREEN_DEEP, width=2,
)
draw.ellipse(
    [cx - center_r, cy - center_r, cx + center_r, cy + center_r],
    fill=PANEL, outline=GREEN, width=3,
)

kicker = "ANY ORDER · ANY PAUSE"
big = "AUTO-LOCK"
desc1 = "Spring drives the bolt"
desc2 = "back to locked, every time."

kb = draw.textbbox((0, 0), kicker, font=f_reset_kicker)
bb = draw.textbbox((0, 0), big, font=f_reset_label)
d1b = draw.textbbox((0, 0), desc1, font=f_reset_desc)
d2b = draw.textbbox((0, 0), desc2, font=f_reset_desc)

spacing_after_kicker = 10
spacing_after_big = 12
total_h = (
    (kb[3] - kb[1]) + spacing_after_kicker
    + (bb[3] - bb[1]) + spacing_after_big
    + (d1b[3] - d1b[1]) + 4 + (d2b[3] - d2b[1])
)
ty = cy - total_h // 2

draw.text((cx - (kb[2] - kb[0]) // 2, ty), kicker, fill=GREEN, font=f_reset_kicker)
ty += (kb[3] - kb[1]) + spacing_after_kicker
draw.text((cx - (bb[2] - bb[0]) // 2, ty), big, fill=WHITE, font=f_reset_label)
ty += (bb[3] - bb[1]) + spacing_after_big
draw.text((cx - (d1b[2] - d1b[0]) // 2, ty), desc1, fill=MUTED, font=f_reset_desc)
ty += (d1b[3] - d1b[1]) + 4
draw.text((cx - (d2b[2] - d2b[0]) // 2, ty), desc2, fill=MUTED, font=f_reset_desc)

# ------ Footer ------
footer_y = H - 100
footer_main = "PATENTED IN 7 MARKETS · USA · AUSTRALIA · CANADA · EUROPE · CHINA · INDIA · MEXICO"
footer_url = "BrazLatch™ by Braz Innovation   ·   brazlatch.com   ·   US 10,934,749"

fmb = draw.textbbox((0, 0), footer_main, font=f_footer_small)
fub = draw.textbbox((0, 0), footer_url, font=f_footer)
draw.text(((W - (fmb[2] - fmb[0])) / 2, footer_y), footer_main, fill=MUTED, font=f_footer_small)
draw.text(((W - (fub[2] - fub[0])) / 2, footer_y + 30), footer_url, fill=WHITE, font=f_footer)
draw.rectangle([(0, H - 6), (W, H)], fill=GREEN_DEEP)

canvas.save(OUT, "PNG", optimize=True)
print(f"Saved {OUT} ({canvas.size[0]}x{canvas.size[1]})")
