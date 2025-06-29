# chatgpt cant code to save its life so i'm dumping this here as a reference and rewriting the code from scratch
# postponed until I learn how to use Tkinter

import os
from PIL import Image, ImageDraw, ImageFont

# ✨ Hex-to-RGBA conversion (kept private)
def hex_to_rgba(hexcode):
    hexcode = hexcode.lstrip("#")
    return tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4)) + (255,)

# 🎨 Hex-only presets
gradient_presets = {
    "cotton candy": ("#ffffff", "#ff69b4"),
    "greyscale": ("#ffffff", "#646464"),
}

chosen_style = "cotton candy"
top_hex, bottom_hex = gradient_presets[chosen_style]
top_color = hex_to_rgba(top_hex)
bottom_color = hex_to_rgba(bottom_hex)

button_text = input("What shall it be? ")

def generateText(text):
    font_path = os.path.join(os.getcwd(), "upheavtt.ttf")
    font = ImageFont.truetype(font_path, size=12)
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    padding = 3
    width = text_width + 2 * padding
    height = text_height + 6
    return font, width, height, padding, text_height

def make_gradient(width, height, top_color, bottom_color, text_top=0, text_height=12):
    img = Image.new("RGBA", (width, height))
    split = text_top + text_height // 2
    for y in range(height):
        color = top_color if y < split else bottom_color
        for x in range(width):
            img.putpixel((x, y), color)
    return img

font, width, height, padding, text_height = generateText(button_text)

# Draw the text as a mask
mask = Image.new("L", (width, height), 0)
ImageDraw.Draw(mask).text((padding, 2), button_text, font=font, fill=255)

# Make the cel-style gradient
gradient = make_gradient(width, height, top_color, bottom_color, text_top=2, text_height=text_height)

# Apply the gradient only where the text is
final = Image.composite(gradient, Image.new("RGBA", (width, height)), mask)
final.show()



