from PIL import Image
import pytesseract

img = 'IMG_6915.JPG'
img2 = '1.jpg'
img3 = 'code01.jpg'

print(pytesseract.image_to_string(Image.open(img3)))
