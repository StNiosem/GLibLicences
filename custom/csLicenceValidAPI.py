import CustomEncodingHandler
import os
import fileinput
import sys

blockIterationCounter = 0
licFileData = []

def licenceFileInput(licenceFile = fileinput.input()) :
    for l in licenceFile :
        print("block " + blockIterationCounter + " found")
        blockIterationCounter = blockIterationCounter + 1
        licFileData =  licFileData + l

    return licFileData

def licenceFileCheck() :
    if (licFileData == "" or licFileData == []) :
        print("Licence File is Empty.")