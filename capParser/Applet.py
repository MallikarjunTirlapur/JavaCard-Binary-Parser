# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:00:00 2019

@author: Tirlapur
"""

from MyUtil import Util

class AppletComp:    
   
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def processAppletsInfo(self, start, length):        
        start += length 
        length = 2
        aidLength = Util.convertDataToPrint(self.binData, start, length)
        print('        applet aid length, '+"0x"+aidLength)  

        aid=''
        for item in range((int)(aidLength, 16)):
            start += length 
            length = 2
            aid += '0x' + Util.convertDataToPrint(self.binData, start, length) + ':'
            
        print('        applet aid - '+ aid)
        
        start += length 
        length = 4
        offset = Util.convertDataToPrint(self.binData, start, length)
        print('        install method offset into the info item of the Method Component, ', offset)
        
        return start, length

    def processAppletComp(self):
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
        count = Util.convertDataToPrint(self.binData, start, length)
        print('    count, ', count)

        for item in range((int)(count, 16)):
            start, length = self.processAppletsInfo(start, length)