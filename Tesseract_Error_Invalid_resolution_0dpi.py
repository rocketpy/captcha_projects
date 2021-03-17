#  How to solve :  Warning: Invalid resolution 0 dpi. Using 70 instead.

# Try using --dpi 300
# C:\Users\username\Desktop> tesseract image.jpg stdout -l rus

#  Output to be stored in a text file. 
# tesseract image.png output.txt

# custom_config = r'-l eng --psm 6'
# pytesseract.image_to_string(img, config=custom_config)


# this not working , lol ...
#  mogrify -set units PixelsPerInch -density 300 image.jpg
# or
# mogrify -set density 300 image.jpg


# be cause this , can be wrong ...
# tesseract dpi_issue.png - --dpi 300 --psm 0

#  image_to_osd()
