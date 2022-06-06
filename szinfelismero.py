
import cv2
import numpy as np

import os
import time
from PIL import Image, ImageFilter, ImageEnhance

from matplotlib.colors import cnames
import pandas


#

fileName = "b.png"

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

# image = cv2.circle(img_base, (int(x / 2), int(y / 2)), int(x / 6), (225, 225, 225), 8)
# image = cv2.circle(img_base, (int(x / 2), int(y / 2)), int(x / 6), (255, 255, 255), -1)
# cv2.imshow("Dominans szin", img_base)
# cv2.waitKey(0)

#

#cv2.destroyAllWindows()
#time.sleep(.5)
#os.remove(f"temp\\_{fileName}")

#

###

#

color_ALAP = ["Piros", "Zold", "Kek", "Ismeretlen"]
text_ALAP = ["Piros", "Zöld", "Kék", "Ismeretlen"]
color_RAKTAR = ["Piros: ez a csomag egy torekeny termeket tartalmaz", "Zold: ez a csomag egy romlando termeket tartalmaz", "Kek: ez a csomag egy aeroszolos termeket tartalmaz", "Ismeretlen: nem ismerheto fel megfelelo szin"]
text_RAKTAR = ["Piros: ez a csomag egy törékeny terméket tartalmaz", "Zöld: ez a csomag egy romlandó terméket tartalmaz", "Kék: ez a csomag egy aeroszolos terméket tartalmaz", "Ismeretlen: nem ismerhető fel megfelelő szín"]

print("\nINDUSTRIA PERITIA ©\nSzínfelismerő Program")

image = img_base
index = ["color","color_name","hex","R","G","B"]
dataset = pandas.read_csv("dataset_new.txt", names=index, header=None, encoding="utf-8")
#print(dataset)

clickstate = False

r = 0
g = 0
b = 0

position_x = 0
position_y = 0

def recognizer(R,G,B):
  minimum = 1000
  for i in range(len(dataset)):
    d = abs(R - int(dataset.loc[i, "R"])) + abs(G - int(dataset.loc[i, "G"])) + abs(B - int(dataset.loc[i, "B"]))
    if (d <= minimum):
      minimum = d
      cname = dataset.loc[i, "color_name"]
  return cname

def clickhandler(event, x, y, f, p):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    global b, g, r, position_x, position_y, clickstate
    clickstate = True
    position_x = x
    position_y = y
    b, g, r = image[y, x]
    b = int(b)
    g = int(g)
    r = int(r)


cv2.namedWindow('Szinfelismero Program')
cv2.setMouseCallback('Szinfelismero Program', clickhandler)


while (1):
    cv2.imshow("Szinfelismero Program", image)
    if (clickstate):
        cv2.rectangle(image, (20, 20), (500, 48), (b * 1.2, g * 1.2, r * 1.2), 4)
        cv2.rectangle(image, (20, 20), (500, 48), (b, g, r), -1)

        if recognizer(r, g, b) == "Piros":
          text = color_RAKTAR[0]
          print("\n> " + str(text_RAKTAR[0]))
        elif recognizer(r, g, b) == "Zöld":
          text = color_RAKTAR[1]
          print("\n> " + str(text_RAKTAR[1]))
        elif recognizer(r, g, b) == "Kék":
          text = color_RAKTAR[2]
          print("\n> " + str(text_RAKTAR[2]))
        else:
          text = color_RAKTAR[3]
          print("\n> " + str(text_RAKTAR[3]))

        lighten = .5 # 1 az 0%, 0 meg 100%
        if recognizer(r, g, b) == "Ismeretlen":
          lighten = .1
        elif r < 100 and g < 100 and b < 100:
          lighten = .25
        cv2.putText(image, text, (25, 40), cv2.FONT_HERSHEY_DUPLEX, .5, (abs(255 - r * lighten), abs(255 - g * lighten), abs(255 - b * lighten)), 1, cv2.LINE_AA)

        if (r + g + b >= 600):
            cv2.putText(image, text, (25, 40), cv2.FONT_HERSHEY_DUPLEX, .5, (0, 0, 0), 1, cv2.LINE_AA)
        
        clickstate = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()


