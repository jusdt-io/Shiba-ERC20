from PIL import Image, ImageDraw

try:
    logo = Image.open("logo.png").convert("RGBA")
    badge = Image.open("verified_badge.png").resize((20, 20))
    
    img = Image.new("RGB", (400, 400), "#f5f5f5")
    draw = ImageDraw.Draw(img)
    
    # Browser UI
    draw.rectangle([(0, 0), (400, 40)], fill="#e0e0e0")
    url = "your-site.com"
    draw.rounded_rectangle([(100, 10), (380, 30)], radius=15, fill="white")
    draw.text((120, 15), url, fill="black")
    
    # Add badge
    text_width = draw.textlength(url)
    img.paste(badge, (120 + int(text_width) + 5, 15), badge)
    
    # Add logo
    logo = logo.resize((200, 200))
    img.paste(logo, (100, 100), logo)
    
    img.save("profile.png")
    print("🚀 Profile created!")
    
except FileNotFoundError as e:
    print(f"Error: {e}\nFirst run: python make_badge.py")
