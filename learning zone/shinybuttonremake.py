def textwizard(text):
    import os
    from PIL import Image, ImageDraw, ImageFont

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

    font, width, height, padding, text_height = generateText(text)

    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((padding, height - text_height - 3), text, font=font, fill=(255, 255, 255))

    image.show()

