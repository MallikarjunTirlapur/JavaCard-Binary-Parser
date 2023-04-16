# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:04:31 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class DirectoryComp:
    
    def __init__(self):
        self.binData = 0
        self.COMPONENT_Header = 0x01
        self.COMPONENT_Directory = 0x02
        self.COMPONENT_Applet = 0x03
        self.COMPONENT_Import = 0x04
        self.COMPONENT_ConstantPool = 0x05
        self.COMPONENT_Class = 0x06
        self.COMPONENT_Method = 0x07
        self.COMPONENT_StaticField = 0x08
        self.COMPONENT_ReferenceLocation = 0x09
        self.COMPONENT_Export = 0x0A
        self.COMPONENT_Descriptor = 0x0B
        self.COMPONENT_Debug = 0x0C
        self.COMPONENT_Static_Resources = 0x0D
        
        
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
        
        ComponentSizes={}
        compTotalSize = 0
        for item in range((int)("C", 16)):
            start += length 
            length = 4
            compSize = Util.convertDataToPrint(self.binData, start, length)
            if item == 0:
                ComponentSizes.update({'header':int(compSize, 16)})
            if item == 1:
                ComponentSizes.update({'directory':int(compSize, 16)})
            if item == 2:
                ComponentSizes.update({'applet':int(compSize, 16)})
            if item == 3:
                ComponentSizes.update({'import':int(compSize, 16)})
            if item == 4:
                ComponentSizes.update({'constantPool': int(compSize, 16)})
            if item == 5:
                ComponentSizes.update({'class': int(compSize, 16)})
            if item == 6:
                ComponentSizes.update({'method': int(compSize, 16)})
            if item == 7:
                ComponentSizes.update({'staticField': int(compSize, 16)})
            if item == 8:
                ComponentSizes.update({'refLoc': int(compSize, 16)})
            if item == 9:
                ComponentSizes.update({'export': int(compSize, 16)})
            if item == 10:
                ComponentSizes.update({'descriptor': int(compSize, 16)})
            if item == 11:
                ComponentSizes.update({'debug': int(compSize, 16)})

            compTotalSize += int(compSize, 16)
            
        print('    Component_Sizes ', ComponentSizes)
        print('    Component_Toatl_Sizes '+ str(compTotalSize))



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