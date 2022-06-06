

from matplotlib.colors import cnames
import numpy
import pandas
import cv2 as opencv


color_ALAP = ["Piros", "Zold", "Kek", "Ismeretlen"]
text_ALAP = ["Piros", "Zöld", "Kék", "Ismeretlen"]
color_RAKTAR = ["Piros: ez a csomag egy torekeny termeket tartalmaz", "Zold: ez a csomag egy romlando termeket tartalmaz", "Kek: ez a csomag egy aeroszolos termeket tartalmaz", "Ismeretlen: a kepen nem ismerheto fel megfelelo szin"]
text_RAKTAR = ["Piros: ez a csomag egy törékeny terméket tartalmaz", "Zöld: ez a csomag egy romlandó terméket tartalmaz", "Kék: ez a csomag egy aeroszolos terméket tartalmaz", "Ismeretlen: a képen nem ismerhető fel megfelelő szín"]

print("INDUSTRIA PERITIA ©\nSzínfelismerő Program")

image = opencv.imread(input("\nFile neve: "))
# opencv.imshow("Wuuu", image)
# opencv.waitKey(0)

#defining column names
index = ["color","color_name","hex","R","G","B"]

#reading dataset file and structuring it
dataset = pandas.read_csv("dataset_new.txt", names=index, header=None, encoding="utf-8")
# print(dataset)

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
  if event == opencv.EVENT_LBUTTONDBLCLK:
    global b, g, r, position_x, position_y, clickstate
    clickstate = True
    position_x = x
    position_y = y
    b, g, r = image[y, x]
    b = int(b)
    g = int(g)
    r = int(r)


opencv.namedWindow('Szinfelismero Program')
opencv.setMouseCallback('Szinfelismero Program', clickhandler)


while (1):
    opencv.imshow("Szinfelismero Program", image)
    if (clickstate):
        #opencv.rectangle(image, startpoint, endpoint, color, thickness)-1. It fills entire rectangle
        opencv.rectangle(image, (20, 20), (800, 64), (b * 1.1, g * 1.1, r * 1.1), 4)
        opencv.rectangle(image, (20, 20), (800, 64), (b, g, r), -1)

        #Creating a text string to display color name and RGB value
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
        #text = recognizer(r, g, b)# + "  RGB(" + str(r) + "," + str(g) + "," + str(b) + ")"

        #opencv.putText() function will write data on image
        lighten = .5 # 1 is 0%, 0 is 100%
        if recognizer(r, g, b) == "Ismeretlen":
          lighten = .1
        elif r < 100 and g < 100 and b < 100:
          lighten = .25
        opencv.putText(image, text, (50, 50), opencv.FONT_HERSHEY_DUPLEX, .8, (abs(255 - r * lighten), abs(255 - g * lighten), abs(255 - b * lighten)), 1, opencv.LINE_AA)

        #For light colors we will choose black color
        if (r + g + b >= 600):
            opencv.putText(image, text, (50, 50), opencv.FONT_HERSHEY_DUPLEX, .8, (0, 0, 0), 1, opencv.LINE_AA)
        
        clickstate = False
        
    #Ends the function when Esc is clicked
    if opencv.waitKey(20) & 0xFF == 27:
        break

opencv.destroyAllWindows()

