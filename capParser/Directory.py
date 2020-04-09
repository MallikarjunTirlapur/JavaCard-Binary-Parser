# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:04:31 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class DirectoryComp:
    
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def customComponentInfo(self, start, length):    
        start += length 
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        print ('        custom component tag, '+infTag)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        print('        custom component size, '+"0x"+size)
        
        start += length 
        length = 2
        aidLength = Util.convertDataToPrint(self.binData, start, length)
        print('        custom component aid length, '+"0x"+aidLength)  

        aid=''
        for item in range((int)(aidLength, 16)):
            start += length 
            length = 2
            aid += '0x' + Util.convertDataToPrint(self.binData, start, length) + ':'
            
        print('        custom component aid '+ aid)
        
        return start, length
    
    
    def staticFieldSizeInfo(self, start, length):        
        start += length 
        length = 4
        image_size = Util.convertDataToPrint(self.binData, start, length)
        print ('        static field image size ', image_size)
        
        start += length 
        length = 4
        array_init_count = Util.convertDataToPrint(self.binData, start, length)
        print ('        number of arrays initialized in all of the constructors in this package ', array_init_count)
  
        start += length 
        length = 4
        array_init_size = Util.convertDataToPrint(self.binData, start, length)
        print ('        total number of bytes in all of the arrays initialized ', array_init_size)
        
        return start, length

    def processDirectoryComp(self):
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        print ('    tag, '+infTag)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        print('    size, '+"0x"+size)
        
        ComponentSizes=''
        for item in range((int)("C", 16)):
            start += length 
            length = 4
            ComponentSizes += '0x' + Util.convertDataToPrint(self.binData, start, length) + ' '
            
        print('    Component_Sizes '+ ComponentSizes)

        start, length = self.staticFieldSizeInfo(start, length)

        start += length 
        length = 2
        import_count = Util.convertDataToPrint(self.binData, start, length)
        print ('    number of packages imported by class/interface in this package ', import_count)
        
        start += length 
        length = 2
        applet_count = Util.convertDataToPrint(self.binData, start, length)
        print ('    number of applets defined in this package ', applet_count)
        
        start += length 
        length = 2
        custom_count = Util.convertDataToPrint(self.binData, start, length)
        print ('    number of entries in the custom_components table ', custom_count)
        
        if(custom_count != "00"):
            start, length = self.customComponentInfo(start, length)