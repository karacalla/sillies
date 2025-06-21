from PIL import Image, ImageDraw, ImageFont


# Let's generate the text first to determine the length of the button
button_text= input("What will it be? ")


def generateText(button_text):
font = ImageFont.truetype("upheaval.ttf", size=12)  # example size
text = button_text
text_width, text_height = font.getsize(text)
padding = 6
width = text_width + 2 * padding
height = text_height + 6

# Create image
img = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # Transparent background
draw = ImageDraw.Draw(img)

# Draw text centered
draw.text((padding, 3), text, font=font, fill=(0, 0, 0))  # (x, y) manually adjusted for pixel accuracy

# Show image (print-style preview)
img.show()
