import classes
import sys
import os


def GetLowestVal(l):
    for x, val in enumerate(l):
       if val > 0:
            return x

def GetHighestVal(l):
    returnVal = 0
    for x, val in enumerate(l):
       if val > 0:
            returnVal = x
    return returnVal

