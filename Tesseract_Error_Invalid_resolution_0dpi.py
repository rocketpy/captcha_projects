#  How to solve :  Warning: Invalid resolution 0 dpi. Using 70 instead.

# Try using --dpi 300

# Need try to use command
#  mogrify -set units PixelsPerInch -density 300 image.jpg
# or
# mogrify -set density 300 image.jpg


# be cause this , can be wrong ...
# tesseract dpi_issue.png - --dpi 300 --psm 0

#  image_to_osd()
