# -*- c+ ding: utf-8 -*-
"""
Created on Mon Oct 14 10:38:58 2019

@author: Tirlapur
"""
from MyUtil import Util

class ByteCodes():
    
    def __init__(self, binData):
        self.ByteCodeTable = dict()
        self.ByteCodeLengthTable = dict()
        self.binData = binData
#        self.stack[500] = 0
#        self.frame[500] = 0
#        self.stackTop = 0
#        self.frameIndex = 0
  
    def getByteCodeTable(self):
        return self.ByteCodeTable
    
#    def pushToStack(self, data):
#        self.stackTop += 1
#        self.stack[self.stackTop] = data
        
#    
#    def popFromStack(self):
#        data = self.stack[self.stackTop]
#        self.stackTop -= 1
#        return data
#    
#    def writeToFrame(self, data):
#        self.frame[self.frameIndex] = data
#    
#    def readFromFrame(self):
#        return self.frame[self.frameIndex]

    def nop(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def aconst_null(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1		

    def sconst_m1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1		

    def sconst_0(self, index, byteCode, start, prnt):        
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1
    def sconst_1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sconst_2(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sconst_3(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sconst_4(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sconst_5(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def iconst_m1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def iconst_0(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iconst_1(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def iconst_2(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iconst_3(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def iconst_4(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iconst_5(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def bspush(self, index, byteCode, start, prnt):
        #index into the biData - start+2 and length 2(for one byte)
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)  
        return 2

    def sspush(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def bipush(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def sipush(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def iipush(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 8), 16))), prnt) 
        return 5

    def aload(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def sload(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def iload(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def aload_0(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def aload_1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def aload_2(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def aload_3(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sload_0(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sload_1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sload_2(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def sload_3(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        return 1

    def iload_0(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iload_1(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iload_2(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iload_3(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def aaload(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def baload(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def saload(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iaload(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def astore(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def sstore(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def istore(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def astore_0(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def astore_1(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def astore_2(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def astore_3(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sstore_0(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sstore_1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sstore_2(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sstore_3(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def istore_0(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def istore_1(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def istore_2(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def istore_3(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def aastore(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def bastore(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sastore(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iastore(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def pop(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def pop2(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def dup(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def dup2(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def dup_x(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def swap_x(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def sadd(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iadd(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ssub(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def isub(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def smul(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def imul(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sdiv(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def idiv(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def srem(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def irem(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sneg(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ineg(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sshl(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ishl(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sshr(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ishr(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sushr(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iushr(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sand(self, index, byteCode, start, prnt):  
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def iand(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sor(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ior(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sxor(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ixor(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sinc(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def iinc(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def s2b(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def s2i(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def i2b(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def i2s(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def icmp(self, index, byteCode, start, prnt):   
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ifeq(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def ifne(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def iflt(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def ifge(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def ifgt(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def ifle(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def ifnull(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def ifnonnull(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_acmpeq(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_acmpne(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def if_scmpeq(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_scmpne(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def if_scmplt(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_scmpge(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_scmpgt(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def if_scmple(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def goto(self, index, byteCode, start, prnt): 			
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def jsr(self, index, byteCode, start, prnt): 			
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def ret(self, index, byteCode, start, prnt): 			
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def stableswitch(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        start += 2
        length = 4
        
        start += length
        length = 4
        low = (int)(Util.convertDataToPrint(self.binData, start, length), 16)

        start += length
        length = 4        
        high = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        arrsize = high - low + 1;  
        return (7 + (arrsize*2))

    def itableswitch(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt)
        start += 2
        length = 4
        
        start += length
        length = 8
        low = (int)(Util.convertDataToPrint(self.binData, start, length), 16)

        start += length
        length = 8        
        high = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        arrsize = high - low + 1;  
        return (11 + (arrsize*2))

    def slookupswitch(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        start += 2
        length = 4
        
        start += length
        length = 4
        npairs = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
  
        return (5 + (npairs*4))

    def ilookupswitch(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        start += 2
        length = 4
        
        start += length
        length = 4
        npairs = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
  
        return (5 + (npairs*6))

    def areturn(self, index, byteCode, start, prnt):		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def sreturn(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def ireturn(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def j_return(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ 'return'), prnt) 
        return 1

    def getstatic_a(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getstatic_b(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def getstatic_s(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getstatic_i(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def putstatic_a(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def putstatic_b(self, index, byteCode, start, prnt):  		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def putstatic_s(self, index, byteCode, start, prnt):  		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def putstatic_i(self, index, byteCode, start, prnt):  		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getfield_a(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def getfield_b(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def getfield_s(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def getfield_i(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_a(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_b(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_s(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_i(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def invokevirtual(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def invokespecial(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def invokestatic(self, index, byteCode, start, prnt):  	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def invokeinterface(self, index, byteCode, start, prnt):  
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 4), 4), 16))+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 8), 2), 16))), prnt) 
        return 5

    def new(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def newarray(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def anewarray(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def arraylength(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def athrow(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]), prnt) 
        return 1

    def checkcast(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 6), 16))), prnt) 
        return 4

    def instanceof(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 6), 16))), prnt) 
        return 4

    def sinc_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 6), 16))), prnt)
        return 4

    def iinc_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 6), 16))), prnt) 
        return 4

    def ifeq_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def ifne_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def iflt_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def ifge_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def ifgt_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def ifle_w(self, index, byteCode, start, prnt): 		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def ifnull_w(self, index, byteCode, start, prnt):		
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def ifnonnull_w(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_acmpeq_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def if_acmpne_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmpeq_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmpne_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmplt_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmpge_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmpgt_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def if_scmple_w(self, index, byteCode, start, prnt):	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def goto_w(self, index, byteCode, start, prnt): 	  	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def getfield_a_w(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getfield_b_w(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getfield_s_w(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getfield_i_w(self, index, byteCode, start, prnt): 	
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def getfield_a_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def getfield_b_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def getfield_s_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def getfield_i_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_a_w(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def putfield_b_w(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt) 
        return 3

    def putfield_s_w(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def putfield_i_w(self, index, byteCode, start, prnt):    
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 4), 16))), prnt)
        return 3

    def putfield_a_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_b_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt) 
        return 2

    def putfield_s_this(self, index, byteCode, start, prnt): 
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    def putfield_i_this(self, index, byteCode, start, prnt):
        Util.printOnConsole(('              '+ self.ByteCodeTable[byteCode]+' '+str((int)(Util.convertDataToPrint(self.binData, (start + 2), 2), 16))), prnt)
        return 2

    
    def execByteCode(self, byteCode, index, start, prnt):
        method = getattr(self, self.ByteCodeTable[byteCode], lambda: "Invalid method")
        return method(index, byteCode, start, prnt)
    
    def updateByteCodeTable(self):
        self.ByteCodeTable.update({0x00 : 'nop'})
        self.ByteCodeTable.update({0x01 : 'aconst_null'})
        self.ByteCodeTable.update({0x02 : 'sconst_m1'})
        self.ByteCodeTable.update({0x03 : 'sconst_0'})
        self.ByteCodeTable.update({0x04 : 'sconst_1'})
        self.ByteCodeTable.update({0x05 : 'sconst_2'})
        self.ByteCodeTable.update({0x06 : 'sconst_3'})
        self.ByteCodeTable.update({0x07 : 'sconst_4'})
        self.ByteCodeTable.update({0x08 : 'sconst_5'}) 
        self.ByteCodeTable.update({0x09 : 'iconst_m1'})
        self.ByteCodeTable.update({0x0A : 'iconst_0'}) 
        self.ByteCodeTable.update({0x0B : 'iconst_1'}) 
        self.ByteCodeTable.update({0x0C : 'iconst_2'}) 
        self.ByteCodeTable.update({0x0D : 'iconst_3'}) 
        self.ByteCodeTable.update({0x0E : 'iconst_4'}) 
        self.ByteCodeTable.update({0x0F : 'iconst_5'})
    
        self.ByteCodeTable.update({0x10 : 'bspush'})
        self.ByteCodeTable.update({0x11 : 'sspush'})
        self.ByteCodeTable.update({0x12 : 'bipush'})
        self.ByteCodeTable.update({0x13 : 'sipush'})
        self.ByteCodeTable.update({0x14 : 'iipush'})
        self.ByteCodeTable.update({0x15 : 'aload'}) 
        self.ByteCodeTable.update({0x16 : 'sload'}) 
        self.ByteCodeTable.update({0x17 : 'iload'})
        self.ByteCodeTable.update({0x18 : 'aload_0'}) 
        self.ByteCodeTable.update({0x19 : 'aload_1'})
        self.ByteCodeTable.update({0x1A : 'aload_2'})
        self.ByteCodeTable.update({0x1B : 'aload_3'})
        self.ByteCodeTable.update({0x1C : 'sload_0'}) 
        self.ByteCodeTable.update({0x1D : 'sload_1'})
        self.ByteCodeTable.update({0x1E : 'sload_2'})
        self.ByteCodeTable.update({0x1F : 'sload_3'})
        
        self.ByteCodeTable.update({0x20 : 'iload_0'})   
        self.ByteCodeTable.update({0x21 : 'iload_1'})    
        self.ByteCodeTable.update({0x22 : 'iload_2'})    
        self.ByteCodeTable.update({0x23 : 'iload_3'})    
        self.ByteCodeTable.update({0x24 : 'aaload'})    
        self.ByteCodeTable.update({0x25 : 'baload'})    
        self.ByteCodeTable.update({0x26 : 'saload'})    
        self.ByteCodeTable.update({0x27 : 'iaload'})    
        self.ByteCodeTable.update({0x28 : 'astore'})    
        self.ByteCodeTable.update({0x29 : 'sstore'})    
        self.ByteCodeTable.update({0x2A : 'istore'})    
        self.ByteCodeTable.update({0x2B : 'astore_0'})    
        self.ByteCodeTable.update({0x2C : 'astore_1'})   
        self.ByteCodeTable.update({0x2D : 'astore_2'})   
        self.ByteCodeTable.update({0x2E : 'astore_3'})   
        self.ByteCodeTable.update({0x2F : 'sstore_0'})

        self.ByteCodeTable.update({0x30 : 'sstore_1'})
        self.ByteCodeTable.update({0x31 : 'sstore_2'})
        self.ByteCodeTable.update({0x32 : 'sstore_3'})
        self.ByteCodeTable.update({0x33 : 'istore_0'})
        self.ByteCodeTable.update({0x34 : 'istore_1'})
        self.ByteCodeTable.update({0x35 : 'istore_2'})
        self.ByteCodeTable.update({0x36 : 'istore_3'})
        self.ByteCodeTable.update({0x37 : 'aastore'})
        self.ByteCodeTable.update({0x38 : 'bastore'})
        self.ByteCodeTable.update({0x39 : 'sastore'})
        self.ByteCodeTable.update({0x3A : 'iastore'})
        self.ByteCodeTable.update({0x3B : 'pop'}) 	
        self.ByteCodeTable.update({0x3C : 'pop2'}) 	
        self.ByteCodeTable.update({0x3D : 'dup'}) 	
        self.ByteCodeTable.update({0x3E : 'dup2'}) 	
        self.ByteCodeTable.update({0x3F : 'dup_x'})
        
        self.ByteCodeTable.update({0x40 : 'swap_x'}) 
        self.ByteCodeTable.update({0x41 : 'sadd'})
        self.ByteCodeTable.update({0x42 : 'iadd'}) 
        self.ByteCodeTable.update({0x43 : 'ssub'}) 
        self.ByteCodeTable.update({0x44 : 'isub'})
        self.ByteCodeTable.update({0x45 : 'smul'}) 
        self.ByteCodeTable.update({0x46 : 'imul'}) 
        self.ByteCodeTable.update({0x47 : 'sdiv'}) 
        self.ByteCodeTable.update({0x48 : 'idiv'}) 
        self.ByteCodeTable.update({0x49 : 'srem'})
        self.ByteCodeTable.update({0x4A : 'irem'}) 
        self.ByteCodeTable.update({0x4B : 'sneg'}) 
        self.ByteCodeTable.update({0x4C : 'ineg'}) 
        self.ByteCodeTable.update({0x4D : 'sshl'}) 
        self.ByteCodeTable.update({0x4E : 'ishl'}) 
        self.ByteCodeTable.update({0x4F : 'sshr'}) 
        
        self.ByteCodeTable.update({0x50 : 'ishr'})   
        self.ByteCodeTable.update({0x51 : 'sushr'})    
        self.ByteCodeTable.update({0x52 : 'iushr'})    
        self.ByteCodeTable.update({0x53 : 'sand'})  
        self.ByteCodeTable.update({0x54 : 'iand'})   
        self.ByteCodeTable.update({0x55 : 'sor'})    
        self.ByteCodeTable.update({0x56 : 'ior'})    
        self.ByteCodeTable.update({0x57 : 'sxor'})   
        self.ByteCodeTable.update({0x58 : 'ixor'})   
        self.ByteCodeTable.update({0x59 : 'sinc'})   
        self.ByteCodeTable.update({0x5A : 'iinc'})   
        self.ByteCodeTable.update({0x5B : 's2b'})    
        self.ByteCodeTable.update({0x5C : 's2i'})    
        self.ByteCodeTable.update({0x5D : 'i2b'})    
        self.ByteCodeTable.update({0x5E : 'i2s'})    
        self.ByteCodeTable.update({0x5F : 'icmp'})   
        
        self.ByteCodeTable.update({0x60 : 'ifeq'}) 		
        self.ByteCodeTable.update({0x61 : 'ifne'}) 		
        self.ByteCodeTable.update({0x62 : 'iflt'}) 		
        self.ByteCodeTable.update({0x63 : 'ifge'}) 		
        self.ByteCodeTable.update({0x64 : 'ifgt'}) 		
        self.ByteCodeTable.update({0x65 : 'ifle'}) 		
        self.ByteCodeTable.update({0x66 : 'ifnull'})	
        self.ByteCodeTable.update({0x67 : 'ifnonnull'}) 
        self.ByteCodeTable.update({0x68 : 'if_acmpeq'}) 
        self.ByteCodeTable.update({0x69 : 'if_acmpne'}) 
        self.ByteCodeTable.update({0x6A : 'if_scmpeq'}) 
        self.ByteCodeTable.update({0x6B : 'if_scmpne'}) 
        self.ByteCodeTable.update({0x6C : 'if_scmplt'}) 
        self.ByteCodeTable.update({0x6D : 'if_scmpge'}) 
        self.ByteCodeTable.update({0x6E : 'if_scmpgt'}) 
        self.ByteCodeTable.update({0x6F : 'if_scmple'}) 
        
        self.ByteCodeTable.update({0x70 : 'goto'}) 			
        self.ByteCodeTable.update({0x71 : 'jsr'}) 			
        self.ByteCodeTable.update({0x72 : 'ret'}) 			
        self.ByteCodeTable.update({0x73 : 'stableswitch'}) 	
        self.ByteCodeTable.update({0x74 : 'itableswitch'}) 	
        self.ByteCodeTable.update({0x75 : 'slookupswitch'}) 
        self.ByteCodeTable.update({0x76 : 'ilookupswitch'}) 
        self.ByteCodeTable.update({0x77 : 'areturn'})		
        self.ByteCodeTable.update({0x78 : 'sreturn'}) 		
        self.ByteCodeTable.update({0x79 : 'ireturn'}) 		
        self.ByteCodeTable.update({0x7A : 'j_return'}) 		
        self.ByteCodeTable.update({0x7B : 'getstatic_a'}) 	
        self.ByteCodeTable.update({0x7C : 'getstatic_b'}) 	
        self.ByteCodeTable.update({0x7D : 'getstatic_s'}) 	
        self.ByteCodeTable.update({0x7E : 'getstatic_i'}) 	
        self.ByteCodeTable.update({0x7F : 'putstatic_a'}) 	
        
        self.ByteCodeTable.update({0x80 : 'putstatic_b'})  		
        self.ByteCodeTable.update({0x81 : 'putstatic_s'})  		
        self.ByteCodeTable.update({0x82 : 'putstatic_i'})  		
        self.ByteCodeTable.update({0x83 : 'getfield_a'}) 		
        self.ByteCodeTable.update({0x84 : 'getfield_b'}) 		
        self.ByteCodeTable.update({0x85 : 'getfield_s'}) 		
        self.ByteCodeTable.update({0x86 : 'getfield_i'}) 		
        self.ByteCodeTable.update({0x87 : 'putfield_a'}) 		
        self.ByteCodeTable.update({0x88 : 'putfield_b'}) 		
        self.ByteCodeTable.update({0x89 : 'putfield_s'}) 		
        self.ByteCodeTable.update({0x8A : 'putfield_i'}) 		
        self.ByteCodeTable.update({0x8B : 'invokevirtual'}) 	
        self.ByteCodeTable.update({0x8C : 'invokespecial'}) 	
        self.ByteCodeTable.update({0x8D : 'invokestatic'})  	
        self.ByteCodeTable.update({0x8E : 'invokeinterface'})  
        self.ByteCodeTable.update({0x8F : 'new'})
        
        self.ByteCodeTable.update({0x90 : 'newarray'}) 		
        self.ByteCodeTable.update({0x91 : 'anewarray'}) 	
        self.ByteCodeTable.update({0x92 : 'arraylength'}) 	
        self.ByteCodeTable.update({0x93 : 'athrow'}) 		
        self.ByteCodeTable.update({0x94 : 'checkcast'}) 	
        self.ByteCodeTable.update({0x95 : 'instanceof'}) 	
        self.ByteCodeTable.update({0x96 : 'sinc_w'}) 		
        self.ByteCodeTable.update({0x97 : 'iinc_w'}) 		
        self.ByteCodeTable.update({0x98 : 'ifeq_w'}) 		
        self.ByteCodeTable.update({0x99 : 'ifne_w'}) 		
        self.ByteCodeTable.update({0x9A : 'iflt_w'}) 		
        self.ByteCodeTable.update({0x9B : 'ifge_w'}) 		
        self.ByteCodeTable.update({0x9C : 'ifgt_w'}) 		
        self.ByteCodeTable.update({0x9D : 'ifle_w'}) 		
        self.ByteCodeTable.update({0x9E : 'ifnull_w'})		
        self.ByteCodeTable.update({0x9F : 'ifnonnull_w'}) 	
        
        self.ByteCodeTable.update({0xA0 : 'if_acmpeq_w'})	
        self.ByteCodeTable.update({0xA1 : 'if_acmpne_w'})	
        self.ByteCodeTable.update({0xA2 : 'if_scmpeq_w'})	
        self.ByteCodeTable.update({0xA3 : 'if_scmpne_w'})	
        self.ByteCodeTable.update({0xA4 : 'if_scmplt_w'})	
        self.ByteCodeTable.update({0xA5 : 'if_scmpge_w'})	
        self.ByteCodeTable.update({0xA6 : 'if_scmpgt_w'})	
        self.ByteCodeTable.update({0xA7 : 'if_scmple_w'})	
        self.ByteCodeTable.update({0xA8 : 'goto_w'}) 	  	
        self.ByteCodeTable.update({0xA9 : 'getfield_a_w'}) 	
        self.ByteCodeTable.update({0xAA : 'getfield_b_w'}) 	
        self.ByteCodeTable.update({0xAB : 'getfield_s_w'}) 	
        self.ByteCodeTable.update({0xAC : 'getfield_i_w'}) 	
        self.ByteCodeTable.update({0xAD : 'getfield_a_this'}) 
        self.ByteCodeTable.update({0xAE : 'getfield_b_this'}) 
        self.ByteCodeTable.update({0xAF : 'getfield_s_this'}) 
    
        self.ByteCodeTable.update({0xB0 : 'getfield_i_this'}) 
        self.ByteCodeTable.update({0xB1 : 'putfield_a_w'})    
        self.ByteCodeTable.update({0xB2 : 'putfield_b_w'})    
        self.ByteCodeTable.update({0xB3 : 'putfield_s_w'})    
        self.ByteCodeTable.update({0xB4 : 'putfield_i_w'})    
        self.ByteCodeTable.update({0xB5 : 'putfield_a_this'}) 
        self.ByteCodeTable.update({0xB6 : 'putfield_b_this'}) 
        self.ByteCodeTable.update({0xB7 : 'putfield_s_this'}) 
        self.ByteCodeTable.update({0xB8 : 'putfield_i_this'}) 