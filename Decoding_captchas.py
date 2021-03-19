from PIL import Image


#  opens the image, converts it to GIF
im = Image.open("captcha.gif")
im = im.convert("P")
print(im.histogram())
