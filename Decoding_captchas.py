from PIL import Image
from operator import itemgetter


#  opens the image, converts it to GIF, because it has only 255 colors !!!
im = Image.open("captcha.gif")
im = im.convert("P")
print(im.histogram())

# And we get the following data: Color and Number of pixels
values = {}

for i in range(256):
    values[i] = his[i]

for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
    print(j, k)

#  change red color letters to black
"""
from PIL import Image


im = Image.open("captcha.gif")
im = im.convert("P")
im2 = Image.new("P", im.size, 255)
im = im.convert("P")
temp = {}
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        temp[pix] = pix
        if pix == 220or pix == 227:
            im2.putpixel((y, x), 0)
            
inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range:             
        if foundletter == Falseand inletter == True:
            foundletter = True
            start = y

        if foundletter == Trueand inletter == False:
            foundletter = False
            end = y
            letters.append((start,end))

        inletter=False
print(letters)  #  result is horizontal positions of the beginning and end of each character

# im2.save("output.gif")
"""

