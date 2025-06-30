from PIL import Image
import PIL
import os

# Save the image temporarily
im = Image.open("bergentruck_caine.ico")
im2 = Image.open("imvubutton.png").convert("RGBA")


im2 = im2.transpose(method=Image.FLIP_TOP_BOTTOM)

im = im.rotate(45, PIL.Image.NEAREST, expand = 1)

im2.paste(im, (50, 125), im)

im.show()
im2.show()
