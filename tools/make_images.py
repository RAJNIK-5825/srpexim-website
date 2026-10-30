"""Generates the SVG illustrations in /images (used because no photo files were supplied).
Run:  python3 tools/make_images.py   (optional - the SVG files are already included)"""
import math, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'images')

DEFS = '''<defs>
<radialGradient id="pg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#e5546a"/><stop offset=".55" stop-color="#b3202f"/><stop offset="1" stop-color="#7e111e"/></radialGradient>
<linearGradient id="leaf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f9a5f"/><stop offset="1" stop-color="#1b5e3f"/></linearGradient>
</defs>'''

def pom(cx, cy, r):
    c = f'M{cx-.22*r:.1f},{cy-.86*r:.1f} L{cx-.22*r:.1f},{cy-1.13*r:.1f} L{cx-.09*r:.1f},{cy-1.0*r:.1f} L{cx},{cy-1.2*r:.1f} L{cx+.09*r:.1f},{cy-1.0*r:.1f} L{cx+.22*r:.1f},{cy-1.13*r:.1f} L{cx+.22*r:.1f},{cy-.86*r:.1f} Z'
    return (f'<ellipse cx="{cx}" cy="{cy+r*1.0:.1f}" rx="{r*.85:.1f}" ry="{r*.11:.1f}" fill="#000" opacity=".16"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#pg)"/>'
            f'<path d="{c}" fill="#8a1220"/>'
            f'<ellipse cx="{cx-.35*r:.1f}" cy="{cy-.38*r:.1f}" rx="{.2*r:.1f}" ry="{.32*r:.1f}" fill="#fff" opacity=".22" transform="rotate(35 {cx-.35*r:.1f} {cy-.38*r:.1f})"/>')

def half(cx, cy, r):
    s = (f'<ellipse cx="{cx}" cy="{cy+r:.1f}" rx="{r*.85:.1f}" ry="{r*.11:.1f}" fill="#000" opacity=".16"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#a51d2d"/><circle cx="{cx}" cy="{cy}" r="{r*.91:.1f}" fill="#f7e6d6"/>')
    for rad, n, ar in ((.72, 12, .105), (.47, 8, .1), (.2, 3, .09)):
        for i in range(n):
            a = 2*math.pi*i/n + rad
            x = cx + r*rad*math.cos(a); y = cy + r*rad*math.sin(a)
            s += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*ar:.1f}" fill="#c4283d"/>'
                  f'<circle cx="{x-r*.03:.1f}" cy="{y-r*.03:.1f}" r="{r*ar*.35:.1f}" fill="#ff9aa8" opacity=".8"/>')
    return s

def leaf(x, y, w, h, rot):
    return f'<ellipse cx="{x}" cy="{y}" rx="{w}" ry="{h}" fill="url(#leaf)" transform="rotate({rot} {x} {y})"/>'

def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">'
            + DEFS + body + '</svg>')

def salt_field(w, y0, h, heap=True):
    s = (f'<linearGradient id="pan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe0e6"/><stop offset="1" stop-color="#f6f9fa"/></linearGradient>'
         f'<rect x="0" y="{y0}" width="{w}" height="{h}" fill="url(#pan)"/>')
    for i in range(-6, 15):
        s += f'<line x1="{w/2}" y1="{y0-40}" x2="{i*w/8}" y2="{y0+h}" stroke="#fff" stroke-width="3" opacity=".85"/>'
    for k in range(1, 6):
        y = y0 + h*(k/6)**1.7
        s += f'<line x1="0" y1="{y:.0f}" x2="{w}" y2="{y:.0f}" stroke="#fff" stroke-width="{1+k}" opacity=".8"/>'
    if heap:
        s += (f'<polygon points="{w*.58},{y0+8} {w*.74},{y0-70} {w*.9},{y0+8}" fill="#eef3f5"/>'
              f'<polygon points="{w*.74},{y0-70} {w*.9},{y0+8} {w*.78},{y0+8}" fill="#c9d6dc"/>'
              f'<polygon points="{w*.82},{y0+8} {w*.92},{y0-38} {w*1.02},{y0+8}" fill="#f7fafb"/>'
              f'<polygon points="{w*.92},{y0-38} {w*1.02},{y0+8} {w*.9},{y0+8}" fill="#cfdbe0"/>')
    return s

def write(name, content):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(content)

# ---- hero
b = ('<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe0cd"/><stop offset="1" stop-color="#f8f5ee"/></linearGradient>'
     '<rect width="800" height="640" fill="url(#sky)"/><circle cx="640" cy="110" r="62" fill="#fbd98a" opacity=".9"/>'
     + salt_field(800, 330, 310) +
     leaf(110, 430, 70, 24, -30) + leaf(150, 395, 60, 20, 20)
     + pom(235, 450, 125) + leaf(235, 318, 42, 15, -35) +
     half(500, 500, 100) + pom(655, 540, 64) + leaf(560, 585, 40, 14, 15))
write('hero.svg', svg(800, 640, b, 'Illustration of fresh Bhagwa pomegranates in front of white salt pans'))

# ---- pomegranate
b = ('<rect width="800" height="600" fill="#fbeee8"/><circle cx="400" cy="300" r="260" fill="#f6d9d0" opacity=".6"/>'
     '<path d="M60 90 Q300 40 560 130" stroke="#6b4a2e" stroke-width="10" fill="none" stroke-linecap="round"/>'
     + leaf(140, 100, 60, 20, -15) + leaf(250, 88, 56, 18, 10) + leaf(430, 105, 60, 20, -5)
     + pom(215, 330, 130) + pom(445, 300, 110) + half(600, 400, 105) + pom(380, 470, 80)
     + leaf(300, 195, 46, 15, 30))
write('pomegranate.svg', svg(800, 600, b, 'Illustration of fresh red Bhagwa pomegranates, whole and cut open'))

# ---- box
b = ('<rect width="800" height="600" fill="#f1ece1"/><rect y="470" width="800" height="130" fill="#e3dccb"/>'
     + pom(260, 290, 78) + pom(400, 265, 82) + pom(540, 290, 78) + pom(330, 330, 72) + pom(470, 335, 72) +
     '<polygon points="140,330 660,330 700,360 100,360" fill="#a97b3f"/>'
     '<rect x="100" y="360" width="600" height="190" rx="6" fill="#c89a5b"/>'
     '<rect x="100" y="360" width="600" height="18" fill="#b0834a"/>'
     '<rect x="250" y="410" width="300" height="100" rx="8" fill="#fff"/>'
     '<text x="400" y="452" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="26" fill="#0f3d2e">BHAGWA &#183; A GRADE</text>'
     '<text x="400" y="492" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="30" fill="#b3202f">2 kg</text>')
write('pomegranate-box.svg', svg(800, 600, b, 'Illustration of a 2 kg box packed with Bhagwa A grade pomegranates'))

# ---- salt pan
b = ('<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc9e6"/><stop offset="1" stop-color="#e9f3f7"/></linearGradient>'
     '<rect width="800" height="600" fill="url(#sky)"/><circle cx="130" cy="110" r="52" fill="#fff6d6"/>'
     '<path d="M0 300 Q200 270 400 295 T800 285 V330 H0Z" fill="#b9c9b0"/>'
     + salt_field(800, 320, 280))
write('salt-pan.svg', svg(800, 600, b, 'Illustration of white salt pans and a heap of salt in Kutch'))

# ---- salt bags
def bag(x, y, w, h, big, small):
    return (f'<ellipse cx="{x+w/2}" cy="{y+h+6}" rx="{w*.55}" ry="9" fill="#000" opacity=".12"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#f6f3ea" stroke="#d6d0bf" stroke-width="2"/>'
            f'<path d="M{x+10} {y+14} H{x+w-10}" stroke="#cfc8b4" stroke-width="3" stroke-dasharray="8 6"/>'
            f'<rect x="{x}" y="{y+h*.34}" width="{w}" height="{h*.34}" fill="#1b5e3f"/>'
            f'<text x="{x+w/2}" y="{y+h*.34+h*.2}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="{w*.22:.0f}" fill="#fff">{big}</text>'
            f'<text x="{x+w/2}" y="{y+h*.84}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="{w*.12:.0f}" fill="#0f3d2e">{small}</text>')
b = ('<rect width="800" height="600" fill="#eaf1f4"/><rect y="480" width="800" height="120" fill="#d5dfe3"/>'
     '<path d="M470 130 q-22 -42 0 -66 M640 130 q22 -42 0 -66" stroke="#c89a5b" stroke-width="10" fill="none" stroke-linecap="round"/>'
     '<rect x="440" y="130" width="230" height="350" rx="10" fill="#f6f3ea" stroke="#d6d0bf" stroke-width="3"/>'
     '<rect x="440" y="225" width="230" height="110" fill="#1b5e3f"/>'
     '<text x="555" y="293" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="52" fill="#fff">1 MT</text>'
     '<text x="555" y="410" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="24" fill="#0f3d2e">JUMBO BAG</text>'
     + bag(235, 290, 180, 190, '50 kg', 'PP BAG') + bag(50, 350, 150, 130, '25 kg', 'PP BAG'))
write('salt-bags.svg', svg(800, 600, b, 'Illustration of 25 kg and 50 kg PP salt bags and a 1 MT jumbo bag'))

# ---- logo + favicon
MARK = ('<circle cx="32" cy="37" r="22" fill="url(#pg)"/>'
        '<path d="M23 20 L23 9 L28 15 L32 6 L36 15 L41 9 L41 20 Z" fill="#8a1220"/>'
        '<ellipse cx="24" cy="29" rx="4.4" ry="7" fill="#fff" opacity=".25" transform="rotate(35 24 29)"/>'
        '<path d="M32 7 Q40 -2 48 4 Q42 12 34 11Z" fill="#2f8a52"/>')
def logo(c1, c2):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 64" width="250" height="64" role="img" aria-label="SRP EXIM">'
            + DEFS + MARK +
            f'<text x="62" y="43" font-family="Montserrat,\'Segoe UI\',Arial,Helvetica,sans-serif" font-weight="800" font-size="31" letter-spacing="1.5" fill="{c1}">SRP <tspan fill="{c2}">EXIM</tspan></text></svg>')
write('logo.svg', logo('#0f3d2e', '#b3202f'))
write('logo-white.svg', logo('#ffffff', '#ff9aa6'))
write('favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64"><rect width="64" height="64" rx="14" fill="#0f3d2e"/>'
      + DEFS + '<g transform="translate(0 4)">' + MARK + '</g></svg>')
print('ok')
