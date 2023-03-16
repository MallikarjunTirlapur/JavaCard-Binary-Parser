# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:47:31 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util
from ByteCodes import ByteCodes

class MethodComp:
    
    def __init__(self):
        self.binData = 0
        
    def setBinaData(self, bnData):
        self.binData = bnData
        self.byteCode = ByteCodes(self.binData)
        self.byteCode.updateByteCodeTable()
        self.byteCodeTable = self.byteCode.getByteCodeTable()
        
    def parseMethodInfo(self, start, length, byteCodeCount, prnt):
        start += length 
        length = 2
        bitField = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        flags = ((bitField & 0xF0) >> 4)
        if(0x08 == flags):
            Util.printOnConsole(('    Method is extended method'), prnt)
        elif(0x04 == flags):
            Util.printOnConsole(('    Method is abstract method'), prnt)
            
        maxStack = (bitField & 0x0F)
        Util.printOnConsole(('        Max stack required for the execution of this method, '+ str(maxStack)), prnt)
        
        start += length 
        length = 2
        bitField = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        nargs = ((bitField & 0xF0) >> 4)
        Util.printOnConsole(('        Number of arguments including this pointer for virtual methods, '+ str(nargs)), prnt)
            
        maxLocals = (bitField & 0x0F)
        Util.printOnConsole(('        Number of locals declared by this method, '+ str(maxLocals)), prnt)

        Util.printOnConsole(('    ByteCode, '), prnt)
        indx = 0
        start += length 
        while(indx < byteCodeCount):
            length = 2
            byteCode = (int)(Util.convertDataToPrint(self.binData, start, length), 16) 
            #print('              ', self.byteCodeTable[byteCode])
            byteCodeLength = self.byteCode.execByteCode(byteCode, indx, start, prnt)                        
            indx += byteCodeLength
            start += byteCodeLength * 2

        return start, length

    def processExceptionHandlerInfo(self, cpCmp, start, length, prnt):
        start += length 
        length = 4
        startOffset = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    start offset (beginning of the try block), '+ str(startOffset)), prnt)
        
        start += length 
        length = 4
        bitField = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        stopBit = ((bitField & 0x8000) == 0x8000)
        if(stopBit):
            Util.printOnConsole(('    stop bit is high'), prnt)
        else:
            Util.printOnConsole(('    stop bit is low'), prnt)
            
        activeLength = (bitField & 0x7FFF)
        Util.printOnConsole(('    active length of the handler block, '+ str(activeLength)), prnt)
        
        start += length 
        length = 4
        handlerOffset = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    handler offset in the method component (catch/finally block), '+ str(handlerOffset)), prnt)
        
        start += length 
        length = 4
        catchTypeIndex = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    catch type index, '+ str(catchTypeIndex)), prnt)      
        
        if(catchTypeIndex):
            Util.printOnConsole(('    class info of the exception class caught by the exception handler, '), prnt)
            cpCmp.parseTheInfoForTheGivenIndex(catchTypeIndex, prnt)
            
        return start, length

    def processMethodInfo(self, offset, byteCodeCount, prnt):
        length = 0
        self.parseMethodInfo(((offset*2) + 6), length, byteCodeCount, prnt)
        
    def getByteFromMethodInfo(self, offset):
        length = 2
        return (int)(Util.convertDataToPrint(self.binData, ((offset*2) + 6), length), 16)

    def processMethodComp(self, cpCmp, prnt):
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
        hndlrCount = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    exception handlers count, '+ str(hndlrCount)), prnt)

        while ((hndlrCount) > 0):
            start, length = self.processExceptionHandlerInfo(cpCmp, start, length, prnt)
            hndlrCount -= 1
            
        byteCodeCount = (int)(size,16) - (start)
        start, length = self.parseMethodInfo(start, length, byteCodeCount, prnt)