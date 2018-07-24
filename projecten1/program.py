import sys
import os
import classes
from logic import *

if len(sys.argv) > 1:
    print("Loaded Image: {}".format(sys.argv[1]))
    path = sys.argv[1]
else:
    print("input the pat of the image you want to import:")
    path = input()

print("what would you like to do with the image? \n(a): convert it to greyscale image\
\n(b): convert it to a stretched rgb image\n(c): convert it to a stretched greyscale image\
\n(d): just show the image\n(e): show data about the image\n(any other key): exit program")
choice = input()
if choice == "a":
    #convert to greyscale and display / save

else if choice == "b":
    #convert to stretched rgb and display / save

else if choice == "c":
    #convert to stretched greyscale and display / save

else if choice == "d":
    #show image

else if choice == "e":
    #data menu
    print("")
else
    sys.exit()


test = None
test = classes.Image(sys.argv[1])
testStretch = classes.Image(sys.argv[1])
histoR, histoG, histoB = testStretch.CreateHistogram()
testStretch.stretchImage(GetHighestVal(histoR), GetHighestVal(histoG),\
                         GetHighestVal(histoB), GetLowestVal(histoR),\
                         GetLowestVal(histoG), GetLowestVal(histoB))
testStretch.save()

