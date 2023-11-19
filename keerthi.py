import pytesseract
import os
from PIL import Image

# Set the path to the Tesseract executable (modify this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.3.3/bin/tesseract'


def convert():
    #img = Image.open('/Users/keerthi/Desktop/hello.png')
    #img = Image.open('/Users/keerthi/Desktop/cutie.jpg')
    #img = Image.open('/Users/keerthi/Desktop/3 4.png')
    #img = Image.open('/Users/keerthi/Desktop/3.png')
    img = Image.open('/Users/keerthi/Desktop/11.png')

    #for single number:
    #text = pytesseract.image_to_string(img, config='--psm 6')

    #for more numbers:
    text = pytesseract.image_to_string(img, lang='eng+equ')

    print(text)
   # file1 = open("output.txt","a")
   # file1.write(text)
   # file1.write("\n")
   # file1.close()

convert()
