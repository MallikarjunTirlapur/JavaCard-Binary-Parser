# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:31:22 2019

@author: Mallikarjun Tirlapur
"""
from MyUtil import Util
from ConstantPool import ConstantPool
from ClassInfo import ClassInfo
import argparse

def getTheArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--exp", help="set the path to exp file, e.g \path\javacard\test.exp")
    args = vars(ap.parse_args())
    return args

if __name__ == "__main__":
    #read the arguments from the command line
    args = getTheArguments()
    constPool = ConstantPool()
    classinfo = ClassInfo()
    
    with open(args['exp'], "rb") as f:
        data = f.read()
        binData = Util.bufferToHex(data, 0, len(data))
        
        start = 0
        length = 8
        magic = Util.convertDataToPrint(binData, start, length)
        print ('    magic number, ', '0x'+magic)
        
        start += length 
        length = 2
        minVrsn = Util.convertDataToPrint(binData, start, length)
        
        start += length 
        length = 2
        majVrsn = Util.convertDataToPrint(binData, start, length)
        print ('    version, ', majVrsn+'.'+minVrsn)
        
        
        start += length 
        length = 4
        constPoolCount = Util.convertDataToPrint(binData, start, length)
        print ('    number of constants in the constant pool, ', constPoolCount)
        
        start, length = constPool.processConstantPool(binData, start, length, constPoolCount)
        print (' ')
        print (' ')
        start += length 
        length = 4
        thisPackge = Util.convertDataToPrint(binData, start, length)
        print ('    package index into the constant pool table, ', thisPackge)
        
        start += length 
        length = 2
        exprtClassCount = Util.convertDataToPrint(binData, start, length)
        print ('    number of elements in the export classes table, ', exprtClassCount)

        start, length = classinfo.processClassInfo(binData, start, length, exprtClassCount)