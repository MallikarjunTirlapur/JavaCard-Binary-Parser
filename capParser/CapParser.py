# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:31:22 2019

@author: Mallikarjun Tirlapur
"""
from ComponentProcessor import ComponentProcessor
import argparse

def getTheArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--capPath", help="path to cap file, e.g \path\javacard\test.cap")
    ap.add_argument("-c", "--component", help="to get each component information, pass component name as argument 'header', 'directory', 'applet', 'import', 'constantpool', 'descriptor', 'class', 'method', 'staticfield', 'refloc', 'export', 'debug' or 'all' for all components")
    args = vars(ap.parse_args())
    return args

if __name__ == "__main__":
    #read the arguments from the command line
    args = getTheArguments()
    compProcess = ComponentProcessor()
    dirctry = args['capPath']
    compProcess.main(dirctry, args['component'])