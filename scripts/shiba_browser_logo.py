from PIL import Image, ImageDraw

# Load the logo.png file that exists in your directory
shiba_logo = Image.open("logo.png").resize((150, 150))

# Create a browser frame (250x250 with URL bar)
browser_frame = Image.new('RGB', (250, 250), 'white')
draw = ImageDraw.Draw(browser_frame)

# Draw URL bar (Google Chrome style)
draw.rounded_rectangle([(20, 20), (230, 50)], radius=10, fill='#f1f3f4', outline='#dadce0')
draw.text((40, 35), "google.com", fill='#5f6368')

# Paste the logo centered below the URL bar
browser_frame.paste(shiba_logo, (50, 70))

# Save the output
browser_frame.save("shiba_browser_logo.png")
print("Success! Image saved as 'shiba_browser_logo.png'")
