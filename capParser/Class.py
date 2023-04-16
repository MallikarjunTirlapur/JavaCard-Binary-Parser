# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:29:19 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util
from ConstantPool import ConstantPoolComp

class ClassComp:
    
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def typeDescriptor(self, start, length):
        start += length 
        length = 2
        nibbleCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        
        indx = 0
        while(indx < ((nibbleCount + 1) / 2)):
            start += length 
            length = 1
            typeNibble = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            if(0x1 == typeNibble):
                print ('        The type is void')
            if(0x2 == typeNibble):
                print ('        The type is boolean')
            if(0x3 == typeNibble):
                print ('        The type is byte')
            if(0x4 == typeNibble):
                print ('        The type is short')
            if(0x5 == typeNibble):
                print ('        The type is int')
            if(0x6 == typeNibble):
                print ('        The type is reference')
                start, length = ConstantPoolComp().classRefProcess(self.binData, start, length, 'printOnConsole')
                #padding
                start += length 
                
            if(0xA == typeNibble):
                print ('        The type is array of boolean')
            if(0xB == typeNibble):
                print ('        The type is array of byte')
                #padding
                start += length
                
            if(0xC == typeNibble):
                print ('        The type is array of short')
            if(0xD == typeNibble):
                print ('        The type is array of int')
            if(0xE == typeNibble):
                print ('        The type is array of reference')
                start, length = ConstantPoolComp().classRefProcess(self.binData, start, length, 'printOnConsole')
                #padding
                start += length 
                
        return start, length    
    
    def processInterfaceInfo(self, start, length, interfaceCount):
        cpComp = ConstantPoolComp()
        while ((interfaceCount) > 0):
            start, length = cpComp.classRefProcess(self.binData, start, length, 'printOnConsole')
            interfaceCount -= 1      
        return start, length
    
    def interfaceClassInfo(self, start, length):   
        cpComp = ConstantPoolComp()
        start += length 
        length = 2
        bitfield = int(Util.convertDataToPrint(self.binData, start, length), 16)
        flag = (bitfield >> 0x4)
        intrfceFlag = 0x08
        shareableFlag = 0x04
        remoteFlag = 0x02
        if (intrfceFlag == flag):
            interfaceCount = (bitfield & 0x0F)
            print ('        The info is Interface Info ')
            print ('        Super Interfaces Count: ', interfaceCount)
            start, length = self.processInterfaceInfo(start, length, interfaceCount)

        elif (shareableFlag == flag):
            interfaceCount = (bitfield & 0x0F)
            print ('        The info is Shareable Interface Info ')
            print ('        Super Interfaces Count: ', interfaceCount)
          
        elif (remoteFlag == flag):
            interfaceCount = (bitfield & 0x0F)
            print ('        The info is Remote Interface Info ')
            print ('        Super Interfaces Count: ', interfaceCount)   
            start, length = self.processInterfaceInfo(start, length, interfaceCount)
            start += length 
            length = 2
            intrfaceNameLength = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            name=''
            index = 0
            while index < intrfaceNameLength:
                start += length 
                length = 2
                name += chr(int(Util.convertDataToPrint(self.binData, start, length), 16))
                print('            Interface name '+ name)  
                index += 1
            print('            Interface name '+ name)  
            
        elif (0 == flag):
            bitfield = int(Util.convertDataToPrint(self.binData, start, length), 16)
            
            #Number of interfaces implemented by this class
            interfaceCount = (bitfield & 0x0F)
            print ('        The info is Class Info ')
            print ('        Implemented Interfaces Count: ', interfaceCount)
            
            #super class reference
            print ('        The Super Class Ref ')
            start, length = cpComp.classRefProcess(self.binData, start, length, 'printOnConsole')
            
            #declared instance fields size
            start += length 
            length = 2
            declaredInstanceSize = Util.convertDataToPrint(self.binData, start, length)
            print ('        declared instance size (number of 16 bit cells): ', declaredInstanceSize)
            
            #token of the first reference instance field defined by this class
            start += length 
            length = 2
            firstRefToken = Util.convertDataToPrint(self.binData, start, length)
            if (firstRefToken == 0xff):
                print ('        Class defines no reference instance field: ', firstRefToken)
            else:
                print ('        first reference token in this class: ', firstRefToken)
            
            #number of reference type instance field defined by this class. 
            start += length 
            length = 2
            referenceCount = Util.convertDataToPrint(self.binData, start, length)
            print ('        number of reference types defined by this class : ', referenceCount)
            
            #public_method_table_base 
            start += length 
            length = 2
            public_method_table_base  = Util.convertDataToPrint(self.binData, start, length)
            print ('        public_method_table_base : ', public_method_table_base)
            
            #public_method_table_count 
            start += length 
            length = 2
            public_method_table_count  = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            print ('        public_method_table_count : ', public_method_table_count)
            
            #package_method_table_base 
            start += length 
            length = 2
            package_method_table_base  = Util.convertDataToPrint(self.binData, start, length)
            print ('        package_method_table_base : ', package_method_table_base)
            
            #package_method_table_count 
            start += length 
            length = 2
            package_method_table_count  = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            print ('        package_method_table_count : ', package_method_table_count)
            
            #public_virtual_method_table[] 
            while ((public_method_table_count) > 0):
                start += length 
                length = 4
                public_virtual_method_offset  = Util.convertDataToPrint(self.binData, start, length)
                print ('        public virtual method offset into the info item of the Method Component : ', public_virtual_method_offset)
                public_method_table_count -= 1

            #package_virtual_method_table[] 
            while ((package_method_table_count) > 0):
                start += length 
                length = 4
                package_virtual_method_offset  = Util.convertDataToPrint(self.binData, start, length)
                print ('        package virtual method offset into the info item of the Method Component : ', package_virtual_method_offset)
                package_method_table_count -= 1
            
            #implemented interface info
            while ((interfaceCount) > 0):
                print ('        implemented interface info  ')
                start, length = cpComp.classRefProcess(self.binData, start, length, 'printOnConsole')
                start += length 
                length = 2
                count  = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
                while((count) > 0):
                    start += length 
                    length = 2
                    index  = Util.convertDataToPrint(self.binData, start, length)
                    print ('            virtual method token of the interface method : ', index)
                    count -= 1
                interfaceCount -= 1
            
            #define remote_interface_info here
            
        return start, length

    def processClassComp(self, descCmp):
        classCount = 0
        
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
        sigLength = (int)(Util.convertDataToPrint(self.binData, start, length))
        print('    signature pool length, ', sigLength)
        
        
        while ((sigLength) > 0):
            #define when package defines any remote interfaces or remote classes.
            start, length = self.typeDescriptor(start, length)
            sigLength -= 1
          
        #get class count from descriptor component
        while (classCount < descCmp.getClassCount()):
            print('    class, ', classCount + 1)
            start, length = self.interfaceClassInfo(start, length)
            classCount += 1
            print(' ')