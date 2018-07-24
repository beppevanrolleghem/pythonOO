#imports:


from PIL import Image as im
import logging
import os, sys
import logic


FORMAT='[%(asctime)s] - [%(levelname)s] - %(message)s'

logging.basicConfig(level=logging.INFO, format=FORMAT)



# (r - minKey)/(maxKey-minKey)


class Image:

    def __init__(self, path):
        self.path = path
        try:
            self.image = im.open(path)
        except IOError:
            logging.warnging("error while importing image: " + IOError)
            return
        self.width, self.height = self.image.size
        logging.info("loaded an image: type [{}] path [{}] width [{}] height [{}]"\
                    .format(self.image.format, self.path, self.width, self.height))
        self.pixels = self.image.load()
        return
    
    def stretchImage(self, highestR, highestG, highestB, lowestR, lowestG, lowestB):
        for i in range(self.getWidth()):
            for j in range(self.getHeight()):
                pix = self.getPixel(i, j)
                r = ((pix[0] - lowestR)*255) /(highestR-lowestR)
                g = ((pix[1] - lowestG)*255) /(highestG-lowestG)
                b = ((pix[2] - lowestB)*255) /(highestB-lowestB)
                self.setPixel(i, j, int(r), int(g), int(b))                
    
    def getPath(self):
        return self.path
    
    def getPixels(self):
        return self.pixels

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getImage(self):
        return self.image

    def showImage(self):
        try:
            self.image.show()
            return True
        except IOError:
            logging.warning("IOError while displaying image:"+IOError)
            return False   
        except:
            logging.warning("error while displaying image")
            return False

    def CreateHistogram(self):
        image = self
        tempR = [0]*256
        tempG = [0]*256
        tempB = [0]*256
        for i in range(image.getWidth()):
            for j in range(image.getHeight()):
                pix = image.getPixel(i, j)
                r = pix[0]
                g = pix[1]
                b = pix[2]
                tempR[r] = tempR[r]+1
                tempG[g] = tempG[g]+1
                tempB[b] = tempB[b]+1
        return tempR, tempG, tempB
    
    def getPixel(self, x, y):   
        return self.pixels[x, y]

    def setPixel(self, x, y, r, g, b):
        self.pixels[x, y] = (r, g, b)
        return

    def getFormat(self):
        return self.image.format

    def save(self, location=None):
        if location == None:
            location = self.path+".edited."+self.image.format
        try:
            self.image.save(location, self.image.format)
        except IOError:
            logging.warning("couldn't save image at {}".format(location)\
                          + ", an error came up: " + IOError)

