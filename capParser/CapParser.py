# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:31:22 2019

@author: Mallikarjun Tirlapur
"""
from ComponentProcessor import ComponentProcessor
import argparse

def getTheArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--cap", help="set the path to cap file, e.g \path\javacard\test.cap")
    ap.add_argument("-c", "--component", help="print component information, feed in the component names e.g 'header' to information of each component and 'all' for all")
    args = vars(ap.parse_args())
    return args

if __name__ == "__main__":
    #read the arguments from the command line
    args = getTheArguments()
    compProcess = ComponentProcessor()
    dirctry = args['cap']
    compProcess.main(dirctry, args['component'])