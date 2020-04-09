# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:08:36 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util
from Header import HeaderComp

class ImportComp:    

    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def processImportComp(self):
        hdrComp = HeaderComp()
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        print ('    tag, '+infTag)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        print('    size, '+"0x"+size)
        
        start += length 
        length = 2
        count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    count, ', count)

        index = 0
        while index < count:
            start, length = hdrComp.processPackageInfo(self.binData, start, length)
            index += 1