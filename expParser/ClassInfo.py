# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:35:04 2019

@author: Mallikarjun Tirlapur
"""
from MyUtil import Util

class ClassInfo:
    
    
    def processAttributesinfo(self, binData, start, length, attributesCount):
        for item in range((int)(attributesCount, 16)):
            start += length 
            length = 4
            attributeIndex = Util.convertDataToPrint(binData, start, length)
            print('        attribute index into the constant_pool table,  ',attributeIndex)
            
            start += length 
            length = 8
            attributeLength = Util.convertDataToPrint(binData, start, length)
            print('        attribute_length ',attributeLength)
            
            start += length 
            length = 4
            constantVlaueIndex = Util.convertDataToPrint(binData, start, length)
            print('        constantvlaue index into the constant_pool table ',constantVlaueIndex)
            
        return start, length
    

    def processFieldInfo(self, binData, start, length, exportFieldsCount):
        for item in range((int)(exportFieldsCount, 16)):
            start += length 
            length = 2
            token = Util.convertDataToPrint(binData, start, length)
            print('        Field token ',token)
    
            start += length 
            length = 4
            accessFlag = (int)(Util.convertDataToPrint(binData, start, length), 16)
            print('        access_flag ', accessFlag)
            if ((accessFlag & 0x0001) == 0x0001):
                print('            access modifier of the  field is - public')
            if ((accessFlag & 0x0004) == 0x0004):
                print('            access modifier of the  field is - protected')
            if ((accessFlag & 0x0008) == 0x0008):
                print('            access modifier of the  field is - static')
            if ((accessFlag & 0x0010) == 0x0010):
                print('            access modifier of the  field is - final')
    
            start += length 
            length = 4
            nameIndex = Util.convertDataToPrint(binData, start, length)
            print('        name index into the constant_pool table, '+nameIndex)
            
            start += length 
            length = 4
            descriptorIndex = Util.convertDataToPrint(binData, start, length)
            print('        descriptor index into the constant_pool table, ',descriptorIndex)

            start += length 
            length = 4
            attributesCount = Util.convertDataToPrint(binData, start, length)
            print('        number of additional attributes of this field, ',attributesCount)
        
            start, length = self.processAttributesinfo(binData, start, length, attributesCount)
        return start, length
    
    def processMethodInfo(self, binData, start, length, exportMethodsCount):
        for item in range((int)(exportMethodsCount, 16)):
            start += length 
            length = 2
            token = Util.convertDataToPrint(binData, start, length)
            print('        Method token ',token)            
 
            start += length 
            length = 4
            accessFlag = (int)(Util.convertDataToPrint(binData, start, length), 16)
            print('        access_flag ', accessFlag)
            if ((accessFlag & 0x0001) == 0x0001):
                print('            access modifier of the  method is - public')
            if ((accessFlag & 0x0004) == 0x0004):
                print('            access modifier of the  method is - protected')
            if ((accessFlag & 0x0008) == 0x0008):
                print('            access modifier of the  method is - static')
            if ((accessFlag & 0x0010) == 0x0010):
                print('            access modifier of the  method is - final')          
            if ((accessFlag & 0x0400) == 0x0400):
                print('            access modifier of the  method is - abstract')  
            
            start += length 
            length = 4
            nameIndex = Util.convertDataToPrint(binData, start, length)
            print('        name index into the constant_pool table ',nameIndex)
            
            start += length 
            length = 4
            descriptorIndex = Util.convertDataToPrint(binData, start, length)
            print('        descriptor index into the constant_pool table, ',descriptorIndex)
            
        return start, length

    def processClassInfo(self, binData, start, length, exprtClassCount):
        for item in range((int)(exprtClassCount, 16)):
            start += length 
            length = 2
            token = Util.convertDataToPrint(binData, start, length)
            print('        token ',token)
            
            start += length 
            length = 4
            accessFlag = (int)(Util.convertDataToPrint(binData, start, length), 16)
            print('        access_flag ', accessFlag)
            if ((accessFlag & 0x0001) == 0x0001):
                print('            access modifier of the class/interface is a Public')
            if ((accessFlag & 0x0010) == 0x0010):
                print('            access modifier of the class is a Final class')
            if ((accessFlag & 0x0200) == 0x0200):
                print('            access modifier of the class is an Interface')
            if ((accessFlag & 0x0400) == 0x0400):
                print('            access modifier of the class/interface is an Abstract')
            if ((accessFlag & 0x0800) == 0x0800):
                print('            access modifier of the class/interface is a Sharable')
            if ((accessFlag & 0x1000) == 0x1000):
                print('            access modifier of the class/interface is a Remote')
                
            start += length 
            length = 4
            nameIndex = Util.convertDataToPrint(binData, start, length)
            print('        name index into the constant pool to read class/interface name, ',nameIndex)
            
            start += length 
            length = 4
            exportSupersCount = Util.convertDataToPrint(binData, start, length)
            print('        number of entries for each public superclass in the supers array, ',exportSupersCount)  
            
            supers=''
            for item in range((int)(exportSupersCount, 16)):
                start += length 
                length = 4
                supers += Util.convertDataToPrint(binData, start, length) + ' '
            print('        supers, ',supers)
            
            start += length 
            length = 2
            exportInterfacesCount = Util.convertDataToPrint(binData, start, length)
            print('        number of entries for each public superclass in the interfaces array, ',exportInterfacesCount)  
            
            interfaces=''
            for item in range((int)(exportInterfacesCount, 16)):
                start += length 
                length = 4
                interfaces += Util.convertDataToPrint(binData, start, length) + ' '
            print('        interfaces ',interfaces)
            
            start += length 
            length = 4
            exportFieldsCount = Util.convertDataToPrint(binData, start, length)
            print('        number of entries for each publicly accessible field in the fields table, ',exportFieldsCount)  
            
            start, length = self.processFieldInfo(binData, start, length, exportFieldsCount)
            
            start += length 
            length = 4
            exportMethodsCount = Util.convertDataToPrint(binData, start, length)
            print('        number of entries for each publicly accessible class method in the methods table, ',exportMethodsCount) 
            
            start, length = self.processMethodInfo(binData, start, length, exportMethodsCount)
            
        return start, length