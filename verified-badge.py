from PIL import Image, ImageDraw, ImageFont

# Create verification badge from scratch
badge_size = 32
badge = Image.new('RGBA', (badge_size, badge_size), (0, 0, 0, 0))
draw = ImageDraw.Draw(badge)

# Draw blue circle
draw.ellipse([(0, 0), (badge_size-1, badge_size-1)], fill='#1da1f2')

# Draw checkmark (✓)
try:
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()
draw.text((8, 4), "✓", fill='white', font=font)

badge.save('verified_badge.png')
print("Verification badge created: verified_badge.png")
