import os
from PIL import Image, ImageDraw, ImageFont

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

font, width, height, padding, text_height = generateText(button_text)

