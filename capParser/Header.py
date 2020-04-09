# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:48:33 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class HeaderComp:
    
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def processPackageNameInfo(self, start, length):        
        start += length 
        length = 2
        nameLength = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print ('            package name length ', nameLength)  

        name=''
        index = 0
        while index < nameLength:
            start += length 
            length = 2
            name += chr(int(Util.convertDataToPrint(self.binData, start, length), 16))
            index += 1
        print('            package name '+ name)
        
        return start, length
    
    
    def processPackageInfo(self, binData, start, length):        
        start += length 
        length = 2
        minVrsn = Util.convertDataToPrint(binData, start, length)
        
        start += length 
        length = 2
        majVrsn = Util.convertDataToPrint(binData, start, length)
        print ('        package version ', majVrsn+'.'+minVrsn)
  
        start += length 
        length = 2
        aidLength = (int)(Util.convertDataToPrint(binData, start, length), 16)
        print('        package aid length, ',aidLength)  

        aid=''
        index = 0
        while index < aidLength:
            start += length 
            length = 2
            aid += '0x' + Util.convertDataToPrint(binData, start, length) + ':'
            index += 1
        print('        package aid '+ aid)
        
        return start, length

    def processHeaderComp(self):
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        print ('    tag, '+infTag)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        print('    size, '+"0x"+size)
        
        start += length 
        length = 8
        magic = Util.convertDataToPrint(self.binData, start, length)
        print('    magic, '+"0x"+magic)

        start += length 
        length = 2
        minVrsn = Util.convertDataToPrint(self.binData, start, length)
        
        start += length 
        length = 2
        majVrsn = Util.convertDataToPrint(self.binData, start, length)
        print ('    version, ', majVrsn+'.'+minVrsn)
        
        start += length 
        length = 2
        accessFlag = Util.convertDataToPrint(self.binData, start, length)
        if (accessFlag == '01'):
            print('    flag of the package is - ACC_INT')
        if (accessFlag == '02'):
            print('    flag of the package is - ACC_EXPORT')
        if (accessFlag == '04'):
            print('    flag of the package is - ACC_APPLET')

        start, length = self.processPackageInfo(self.binData, start, length)
        start, length = self.processPackageNameInfo(start, length)