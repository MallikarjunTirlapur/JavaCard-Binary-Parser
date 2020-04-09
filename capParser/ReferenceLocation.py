# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:46:22 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class ReferenceLocationComp:    

    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def processReferenceLocationComp(self):
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        print ('    tag, '+infTag)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        print('    size, '+"0x"+size)
        
        start += length 
        length = 4
        byteIndexCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    byte_index_count, ', byteIndexCount)

        index = 0
        while index < byteIndexCount:
            start += length 
            length = 2
            offsetToByteIndices = Util.convertDataToPrint(self.binData, start, length)
            print ('    offset_to_byte_indices, '+offsetToByteIndices)
            index += 1
            
        start += length 
        length = 4
        byte2IndexCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    byte2_index_count, ', byte2IndexCount)

        index = 0
        while index < byte2IndexCount:
            start += length 
            length = 2
            offsetToByte2Indices = Util.convertDataToPrint(self.binData, start, length)
            print ('    offset_to_byte2_indices, '+offsetToByte2Indices)
            index += 1