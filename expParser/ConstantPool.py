# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:29:28 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util

class ConstantPool(object):
    
    
    def processPackageInfo(self, binData, start, length):
        infTag = Util.convertDataToPrint(binData, start, length)
        print ('            tag, '+infTag)
    
        start += length 
        length = 2
        flags = Util.convertDataToPrint(binData, start, length)
        if(flags == '01'):
            print('            Package is a library package, defines no applet ')
        elif(flags == '00'):
            print('            Package defines applet ')
        
        start += length 
        length = 4
        nameIndex = Util.convertDataToPrint(binData, start, length)
        print('            name index into the constant_pool table, '+nameIndex)
        
        start += length 
        length = 2
        minVrsn = Util.convertDataToPrint(binData, start, length)
         
        start += length 
        length = 2
        majVrsn = Util.convertDataToPrint(binData, start, length)
        print('            version, '+majVrsn+'.'+minVrsn)
        
        start += length 
        length = 2
        aidlength = Util.convertDataToPrint(binData, start, length)
        print ('            package aid length, '+aidlength)
        
        aid=''
        for item in range((int)(aidlength, 16)):
            start += length 
            length = 2
            aid += '0x' + Util.convertDataToPrint(binData, start, length) + ':'
            
        print('            AID of this package, '+ aid)
        return (start, length)
    
    def processUtf8Info(self, binData, start, length):
        infTag = Util.convertDataToPrint(binData, start, length)
        print ('            tag, '+infTag)
        
        start += length 
        length = 4
        byteLenth = Util.convertDataToPrint(binData, start, length)
        print('            string length, '+byteLenth)
        nameBytes=''
        for item in range((int)(byteLenth, 16)):
            start += length 
            length = 2
            nameBytes += chr(int(Util.convertDataToPrint(binData, start, length), 16))
            
        print('            string, '+nameBytes)
        return start, length
    
    def processClassRefInfo(self, binData, start, length):
        infTag = Util.convertDataToPrint(binData, start, length)
        print ('            tag, '+infTag)
        
        start += length 
        length = 4
        nameIndex = Util.convertDataToPrint(binData, start, length)    
        
        print('            name index into the constant_pool table, '+nameIndex)
        return start, length
    
    def processIntegerInfo(self, binData, start, length):
        infTag = Util.convertDataToPrint(binData, start, length)
        print ('            tag, '+infTag)
        
        start += length 
        length = 8
        value = Util.convertDataToPrint(binData, start, length)    
        
        print('            bytes, '+value)
        return start, length

    def processConstantPool(self, binData, start, length, constPoolCount):
        for item in range((int)(constPoolCount, 16)):
            start += length 
            length = 2
            cpTag = Util.convertDataToPrint(binData, start, length)
            if (cpTag == '01'):
                print ('        '+str(item)+' CONSTANT_Utf8')
                start, length = self.processUtf8Info(binData, start, length)
            elif(cpTag == '0D'):
                print ('        '+str(item)+' CONSTANT_Package')
                start, length = self.processPackageInfo(binData, start, length)
            elif(cpTag == '07'):
                print ('        '+str(item)+' CONSTANT_Classref')
                start, length = self.processClassRefInfo(binData, start, length)
            elif(cpTag == '03'):
                print ('        '+str(item)+' CONSTANT_Integer')
                start, length = self.processIntegerInfo(binData, start, length)
                
        return start, length