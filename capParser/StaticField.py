# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:47:32 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class StaticFieldComp:    
   
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def arrayInitValues(self, start, length, valueSize):
        start += length 
        length = 4
        count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('        count, ',count) 

        index = 0
        print('        initial values of the array, ') 
        while(index < count):
            start += length 
            length = valueSize
            value = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            print('                                ',value) 
            index += 1

        return  start, length           
    
    def arrayInitInfo(self, start, length):        
        start += length 
        length = 2
        arrayType = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        if(0x02 == arrayType):
            print('        array_type is boolean ')
            start, length = self.arrayInitValues(start, length, 2)
        elif(0x03 == arrayType):
            print('        array_type is byte ')
            start, length = self.arrayInitValues(start, length, 2)
        elif(0x04 == arrayType):
            print('        array_type is short ')
            start, length = self.arrayInitValues(start, length, 4)
        elif(0x05 == arrayType):
            print('        array_type is int ')
            start, length = self.arrayInitValues(start, length, 8)
        
        return start, length

    def processStaticFieldComp(self):
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
        imageSize = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    image_size, ',imageSize)
        
        start += length 
        length = 4
        refCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    reference_count, ',refCount)
        
        start += length 
        length = 4
        arrayInitCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    array_init_count, ',arrayInitCount)
        
        index = 0
        while index < arrayInitCount:
            start, length = self.arrayInitInfo(start, length)
            index += 1
            
        start += length 
        length = 4
        defaultValueCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    default_value_count, ',defaultValueCount)
        
        start += length 
        length = 4
        nonDefaultValueCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        print('    non_default_value_count, ',nonDefaultValueCount)
        
        index = 0
        print('        non-default values , ')
        while index < nonDefaultValueCount:
            start += length 
            length = 2
            value = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            print('                                ',value)
            index += 1