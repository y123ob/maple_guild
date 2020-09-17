import cv2
from pytesseract import *

img = cv2.imread('test.png')
text = pytesseract.image_to_string(img, lang='kor')
print(text)