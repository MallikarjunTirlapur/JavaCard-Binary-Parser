# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:51:46 2019

@author: Mallikarjun Tirlapur
"""
##todo: dont return length, this info is not important
from MyUtil import Util

class ConstantPoolComp:
  
    def __init__(self):
        self.binData = 0
        self.constantPoolTable = dict()
        
    def setBinaData(self, bnData):
        self.binData = bnData
    
    def classRefProcess(self, binData, start, length, prnt):
        start += length 
        length = 4
        classRef = Util.convertDataToPrint(binData, start, length)
        extrnalRef = ((int(Util.convertDataToPrint(binData, start, 2), 16) & 0x80) == 0x80)
        if (extrnalRef):
            packageToken = Util.convertDataToPrint(classRef, 0, 2)
            Util.printOnConsole(('               Package Token: '+packageToken), prnt)
            classToken = Util.convertDataToPrint(classRef, 2, 2)
            Util.printOnConsole(('               Class Token: '+ classToken), prnt)
        else:
            Util.printOnConsole(('               Internal Class Ref: '+ classRef), prnt)
        
        return start, length    
    
    def classRefInfo(self, start, length, prnt):                
        start, length = self.classRefProcess(self.binData, start, length, prnt)

        start += length 
        length = 2
        padding = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('               padding '+ padding), prnt)

        return start, length
   
    def instanceFieldRefInfo(self, start, length, prnt):    
            
        start, length = self.classRefProcess(self.binData, start, length, prnt)
        
        start += length 
        length = 2
        token = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('               instance field token, '+ token), prnt)  
        
        return start, length
    
    def virtualMethoddRefInfo(self, start, length, prnt):    
            
        start, length = self.classRefProcess(self.binData, start, length, prnt)
        
        start += length 
        length = 2
        token = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('               virtual method token, '+ token), prnt)  
        
        return start, length
    
    def superMethoddRefInfo(self, start, length, prnt):    
            
        start, length = self.classRefProcess(self.binData, start, length, prnt)
        
        start += length 
        length = 2
        token = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('               super method token, '+ token), prnt)  
        
        return start, length
    
    def staticFieldRefInfo(self, binData, start, length, prnt):        
        start += length 
        length = 6
        refBin = Util.convertDataToPrint(self.binData, start, length)
        extrnalRef = ((int(Util.convertDataToPrint(self.binData, start, 2), 16) & 0x80) == 0x80)
        if (extrnalRef):
            packageToken = Util.convertDataToPrint(refBin, 0, 2)
            Util.printOnConsole(('                Package Token: '+ packageToken), prnt)
            classToken = Util.convertDataToPrint(refBin, 2, 2)
            Util.printOnConsole(('                Class Token: '+ classToken), prnt)
            fieldToken = Util.convertDataToPrint(refBin, 4, 2)
            Util.printOnConsole(('                Static Field Token: '+ fieldToken), prnt)
        else:
            offset = Util.convertDataToPrint(refBin, 2, 4)
            Util.printOnConsole(('                Offset into the static field image: '+ offset), prnt)
            
        return start, length
    
    def staticMethodRefInfo(self, start, length, prnt):        
        start += length 
        length = 6
        refBin = Util.convertDataToPrint(self.binData, start, length)
        extrnalRef = ((int(Util.convertDataToPrint(self.binData, start, 2), 16) & 0x80) == 0x80)
        if (extrnalRef):
            packageToken = Util.convertDataToPrint(refBin, 0, 2)
            Util.printOnConsole(('               Package Token: '+ packageToken), prnt)
            classToken = Util.convertDataToPrint(refBin, 2, 2)
            Util.printOnConsole(('               Class Token: '+ classToken), prnt)
            fieldToken = Util.convertDataToPrint(refBin, 4, 2)
            Util.printOnConsole(('               Static Method Token: '+ fieldToken), prnt)
        else:
            offset = Util.convertDataToPrint(refBin, 2, 4)
            Util.printOnConsole(('               Offset into the info item of the Method Component: '+ offset), prnt)
            
        return start, length

    def parseTheInfoForTheGivenIndex(self, index, prnt):
        start = self.constantPoolTable[index]
        length = 2
        tag = Util.convertDataToPrint(self.binData, start, length)
        if(tag == '01'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_ClassRefInfo '), prnt)
            return self.classRefInfo(start, length, prnt)
        elif(tag == '02'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_InstanceFieldRefInfo '), prnt)
            return self.instanceFieldRefInfo(start, length, prnt)
        elif(tag == '03'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_VirtualMethodRefInfo '), prnt)
            return self.virtualMethoddRefInfo(start, length, prnt)
        elif(tag == '04'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_SuperMethodRefInfo '), prnt)
            return self.superMethoddRefInfo(start, length, prnt)
        elif(tag == '05'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_StaticFieldRefInfo '), prnt)
            return self.staticFieldRefInfo(self.binData,start, length, prnt)
        elif(tag == '06'):
            Util.printOnConsole(('        tag '+ tag), prnt)
            Util.printOnConsole(('            CONSTANT_StaticMethodRefInfo '), prnt)
            return self.staticMethodRefInfo(start, length, prnt)

    def processCPComp(self, prnt): 
        start = 0
        length = 2
        infTag = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('    tag, '+infTag), prnt)
            
        start += length 
        length = 4
        size = Util.convertDataToPrint(self.binData, start, length)
        Util.printOnConsole(('    size, '+"0x"+size), prnt)
        
        start += length 
        length = 4
        count = (int)(Util.convertDataToPrint(self.binData, start, length), 16)
        Util.printOnConsole(('    count, '+str(count)), prnt)
        
        indx = 0
        while (indx < (count)):
            start += length 
            length = 2
            self.constantPoolTable.update({indx : start})
            start, length = self.parseTheInfoForTheGivenIndex(indx, prnt)
            indx += 1
                