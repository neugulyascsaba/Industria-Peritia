
import cv2
import numpy as np

import os
import time
from PIL import Image, ImageFilter, ImageEnhance
import PIL

import time


#

fileName = "kontener_1.png"

#

img_base = cv2.imread(fileName)
cv2.imshow("Eredeti kep", img_base)

#

importedImage = Image.open(fileName)
importedImage.filter(ImageFilter.GaussianBlur(8)).save("temp\\" + "_" + fileName)
importedImage.filter(ImageFilter.MedianFilter(size = 11)).save("temp\\" + "_" + fileName)
enhancer = ImageEnhance.Contrast(Image.open("temp\\" + "_" + fileName))
enhancer.enhance(1.25).save("temp\\" + "_" + fileName)

newImage = Image.open("temp\\" + "_" + fileName)

#

cv2.waitKey(0)
cv2.destroyAllWindows()

#

img_base = cv2.imread("temp\\" + "_" + fileName)
cv2.imshow("Feljavitott kep", img_base)

#

cv2.waitKey(0)
cv2.destroyAllWindows()

#

x = img_base.shape[1]
y = img_base.shape[0]

#

image = cv2.circle(img_base, (int(x / 2), int(y / 2)), int(x / 6), (225, 225, 225), 8)
image = cv2.circle(img_base, (int(x / 2), int(y / 2)), int(x / 6), (255, 255, 255), -1)
cv2.imshow("Feljavitott kep", img_base)
cv2.waitKey(0)

#

#cv2.destroyAllWindows()
#time.sleep(.5)
#os.remove(f"temp\\_{fileName}")













#height = 512
#width = 512
#img = np.zeros((height,width,3), np.uint8)
#img[:,:] = (255,0,0)
#
#img = np.array(newImage.convert('RGB'))
#cv2.imshow('image',img)
#cv2.waitKey(0)
#
#
#
#
#pil_image = PIL.Image.open('Image.jpg').convert('RGB') 
#open_cv_image = np.array(pil_image) 
## Convert RGB to BGR 
#open_cv_image = open_cv_image[:, :, ::-1].copy() 




