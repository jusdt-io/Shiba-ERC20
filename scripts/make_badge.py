from PIL import Image, ImageDraw, ImageFont

size = 32
badge = Image.new('RGBA', (size, size))
draw = ImageDraw.Draw(badge)
draw.ellipse([(0, 0), (size-1, size-1)], fill='#1DA1F2')

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 24)
except:
    font = ImageFont.load_default(size=24)
    
draw.text((8, 4), "✓", fill="white", font=font)
badge.save('verified_badge.png')
print("✅ Badge created!")
