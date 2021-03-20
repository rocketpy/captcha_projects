from PIL import Image
from operator import itemgetter


#  opens the image, converts it to GIF, because it has only 255 colors !!!
im = Image.open("captcha.gif")
im = im.convert("P")
print(im.histogram())


im = Image.open("captcha.gif")
im = im.convert("P")
his = im.histogram()

values = {}

for i in range(256):
    values[i] = his[i]

for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
    print(j, k)

