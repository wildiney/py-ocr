import pytesseract as ocr
import numpy as np
import cv2
import os
import shutil

from PIL import Image


def convert(file, debug=False):
    try:
        imagem = Image.open(file).convert('RGB')

        npimagem = np.asarray(imagem).astype(np.uint8)

        npimagem[:, :, 0] = 0
        npimagem[:, :, 2] = 0

        im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

        ret, thresh = cv2.threshold(
            im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        binimagem = Image.fromarray(thresh)
        if debug == True:
            binimagem.show()

        phrase = ocr.image_to_string(binimagem, lang="por")
        if len(phrase) > 0:
            shutil.move(file, file+".bak")
            f = open("codes.txt", "a+")
            f.write(phrase+"\r")
            f.close()
            return phrase
        else:
            return "File " + file + " is unreadable"
    except FileNotFoundError:
        return "File " + file + " not found"


print(convert("images/2.jpg"))
print(convert("images/IMG_6915.jpg"))
print(convert("images/IMG_6916.jpg"))
print(convert("images/IMG_6917.jpg"))
print(convert("images/IMG_6919.jpg"))
print(convert("images/IMG_6920.jpg"))
