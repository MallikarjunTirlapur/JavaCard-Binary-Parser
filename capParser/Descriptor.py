# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:51:24 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util
from ConstantPool import ConstantPoolComp

class DescriptorComp:
    
    def __init__(self):
        self.classCount = 0
        self.binData = 0
        self.classDescriptorTable = dict()
        self.classDecrptr = self.ClassDescriptorInfo()
        
    def setBinaData(self, bnData):
        self.binData = bnData
        
    def getClassCount(self):
        return self.classCount
    
    class ClassDescriptorInfo:
        def __init__(self):
            self.interfaceCount = 0
            self.fieldCount = 0
            self.methodCount = 0
            self.interfacesTable = dict()
            self.fieldDescriptorTable = dict()
            self.methodDescriptorTable = dict()
            self.fldDesc = self.FieldDescriptor()
            self.mtdDesc = self.MethodDescriptor()
        
        class MethodDescriptor:
            def __init__(self):
                self.byteCodeCount = 0
                self.exceptionHandlerCount = 0
                
            def processMethodDescriptorInfo(self, binData, start, length, mtComp, prnt):
                start += length
                length = 2
                accessFlag = (int)(Util.convertDataToPrint(binData, start, length),16)
                if(0x01 == accessFlag):
                    Util.printOnConsole(('        Method is Public '), prnt)
                if(0x02 == accessFlag):
                    Util.printOnConsole(('        Method is Private '), prnt)
                if(0x04 == accessFlag):
                    Util.printOnConsole(('        Method is Protected '), prnt)
                if(0x08 == accessFlag):
                    Util.printOnConsole(('        Method is Static '), prnt)
                if(0x10 == accessFlag):
                    Util.printOnConsole(('        Method is Final '), prnt)                  
                if(0x40 == accessFlag):
                    Util.printOnConsole(('        Method is Abstract '), prnt)
                if(0x80 == accessFlag):
                    Util.printOnConsole(('        Method is Init '), prnt)  
                    
                start += length
                length = 4
                methodOffset = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                Util.printOnConsole(('        The method offset into the method info '+ str(methodOffset)), prnt)

                start += length
                length = 4
                typeOffset = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                Util.printOnConsole(('        The type offset into type descriptor info '+ str(typeOffset)), prnt)

                start += length
                length = 4
                self.byteCodeCount = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                Util.printOnConsole(('        The number of bytecodes in the method '+ str(self.byteCodeCount)), prnt)
                
                mtComp.processMethodInfo(methodOffset, self.byteCodeCount, prnt)
                
                start += length
                length = 4
                self.exceptionHandlerCount = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                Util.printOnConsole(('        The number of exception handlers implemented by this method '+ str(self.exceptionHandlerCount)), prnt)
                
                start += length
                length = 4
                exceptionHandlerIndex = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                Util.printOnConsole(('        The index to the first exception handler implemented by this method '+ str(exceptionHandlerIndex)), prnt)
                    
                return start, length, self                
        
        class FieldDescriptor:
            def processDescriptorInfo(self, binData, start, length, prnt):
                start += length
                length = 2
                accessFlag = (int)(Util.convertDataToPrint(binData, start, length), 16)
                if(0x01 == accessFlag):
                    Util.printOnConsole(('        Field is Public '), prnt)
                if(0x02 == accessFlag):
                    Util.printOnConsole(('        Field is Private '), prnt)
                if(0x04 == accessFlag):
                    Util.printOnConsole(('        Field is Protected '), prnt)
                if(0x08 == accessFlag):
                    Util.printOnConsole(('        Field is Static '), prnt)
                if(0x10 == accessFlag):
                    Util.printOnConsole(('        Field is Final '), prnt)  
                    
                if(0x08 == accessFlag):
                    start, length = ConstantPoolComp().staticFieldRefInfo(binData, start, length, prnt) 
                else:
                    start, length = ConstantPoolComp().classRefProcess(binData, start, length, prnt)
                    start += length
                    length = 2
                    token = (int)(Util.convertDataToPrint(binData, start, length), 16)
                    Util.printOnConsole(('        Token of the class which declares this field '+ str(token)), prnt)
                    
                start += length
                length = 4
                dataType = (int)(Util.convertDataToPrint(binData, start, length), 16)                
                if((dataType & 0x8000) == 0x8000):
                    if(0x0002 == (dataType & 0x000F)):
                        Util.printOnConsole(('        The field type is boolean'), prnt)
                    if(0x0003 == (dataType & 0x000F)):
                        Util.printOnConsole(('        The field type is byte'), prnt)
                    if(0x0004 == (dataType & 0x000F)):
                        Util.printOnConsole(('        The field type is short'), prnt)
                    if(0x0005 == (dataType & 0x000F)):
                        Util.printOnConsole(('        The field type is int'), prnt)
                else:
                    Util.printOnConsole(('        The field type is reference and the offset into type descriptor info '+ str((dataType & 0x7FFF))), prnt)
                    
                return start, length, self
        
            
        def getMethodCount(self):
            return self.methodCount
        
        def processClassDescriptorInfo(self, binData, start, length, mtComp, prnt):
            start += length
            length = 2
            accessFlag = (int)(Util.convertDataToPrint(binData, start, length), 16)
            if(0x01 == accessFlag):
                Util.printOnConsole(('        Class is Public '), prnt)
            if(0x10 == accessFlag):
                Util.printOnConsole(('        Class is Final '), prnt)
            if(0x40 == accessFlag):
                Util.printOnConsole(('        Class is Interface '), prnt)
            if(0x80 == accessFlag):
                Util.printOnConsole(('        Class is Abstract '), prnt)

            start, length = ConstantPoolComp().classRefProcess(binData, start, length, prnt)
            
            start += length
            length = 2
            self.interfaceCount = (int)(Util.convertDataToPrint(binData, start, length), 16)
            Util.printOnConsole(('        Implemented interface count, '+ str(self.interfaceCount)), prnt)
            
            start += length
            length = 4
            self.fieldCount = (int)(Util.convertDataToPrint(binData, start, length), 16)
            Util.printOnConsole(('        Class instance field count, '+ str(self.fieldCount)), prnt)
            
            start += length
            length = 4
            self.methodCount = (int)(Util.convertDataToPrint(binData, start, length), 16)
            Util.printOnConsole(('        Number of methods defined by this class, '+ str(self.methodCount)), prnt)
            Util.printOnConsole((' '), prnt) 
            
            indx = 0
            while(indx < self.interfaceCount):
                self.interfacesTable.update({indx : start})
                start, length = ConstantPoolComp().classRefProcess(binData, start, length, prnt)
                indx += 1
              
            indx = 0
            while(indx < self.fieldCount):
                start += length
                length = 2
                token = (int)(Util.convertDataToPrint(binData, start, length), 16)
                Util.printOnConsole(('    Field Token, '+ str(token)), prnt)
                start, length, obj = self.fldDesc.processDescriptorInfo(binData, start, length, prnt)
                self.fieldDescriptorTable.update({token:obj})
                indx += 1                
                Util.printOnConsole((' '), prnt)
                
            indx = 0
            while(indx < self.methodCount):
                start += length
                length = 2
                token = (int)(Util.convertDataToPrint(binData, start, length), 16)
                Util.printOnConsole(('    Method Token, '+ str(token)), prnt)
                start, length, obj = self.mtdDesc.processMethodDescriptorInfo(binData, start, length, mtComp, prnt)
                self.methodDescriptorTable.update({token:obj})
                indx += 1            
                Util.printOnConsole((' '), prnt)                
                
            return start, length, self

    def processTypeDescriptorInfo(self, start, length, prnt):
        start += length
        length = 4
        constantPoolCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('        Number of entries in the constant pool table, '+ str(constantPoolCount)), prnt)        
        
        indx = 0
        while(indx < constantPoolCount):
            start += length
            length = 4
            constantPoolType = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            Util.printOnConsole(('        Type of the field or method, '+ str(constantPoolType)), prnt)
            indx += 1
            Util.printOnConsole((' '), prnt)
        
        return start, length

    def getMethodCountForTheGivenClassToken(self, token):
        return self.classDescriptorTable[token].getMethodCount()
        

    def processDescriptorComp(self, mtComp, prnt):
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('    tag, '+infTag), prnt)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('    size, '+"0x"+size), prnt)
        
        start += length 
        length = 2
        self.classCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    class count, '+ str(self.classCount)), prnt)
        
        indx = 0
        while(indx < self.classCount):
            start += length
            length = 2
            token = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
            Util.printOnConsole(('    Class Token, '+ str(token)), prnt)
            start, length, obj = self.classDecrptr.processClassDescriptorInfo(self.binData, start, length, mtComp, prnt)
            self.classDescriptorTable.update({token:obj})
            indx += 1
            Util.printOnConsole((' '), prnt)
        
        start, length = self.processTypeDescriptorInfo(start, length, prnt)

        size = (int)(size, 16)
        start += length
        length = (size - start)*2
        Util.printOnConsole(('    Remaining bytes, '+ Util.convertDataToPrint(self.binData, start, length)), prnt)