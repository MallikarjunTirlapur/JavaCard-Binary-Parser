# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:16:32 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class ExportComp:    
   
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def processClassExportInfo(self, start, length):        
        start += length 
        length = 4
        classOffset = Util.convertDataToPrint(self.binData, start, length)
        print('        class_offset, ',classOffset)  

        start += length 
        length = 2
        static_field_count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('        static_field_count, ', static_field_count)
        
        start += length 
        length = 2
        static_method_count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('        static_method_count, ', static_method_count)
        
        index = 0
        while index < static_field_count:
            start += length 
            length = 4
            static_field_offsets = Util.convertDataToPrint(self.binData, start, length)
            print('        static_field_offsets, ',static_field_offsets) 
            index += 1

        index = 0
        while index < static_method_count:
            start += length 
            length = 4
            static_method_offsets = Util.convertDataToPrint(self.binData, start, length)
            print('        static_method_offsets, ',static_method_offsets)
            index += 1
            
        return start, length

    def processExportComp(self):
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
        class_count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    class_count, ', class_count)

        index = 0
        while(index < class_count):
            start, length = self.processClassExportInfo(start, length)
            index += 1