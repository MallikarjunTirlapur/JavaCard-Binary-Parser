# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:57:11 2019

@author: Mallikarjun Tirlapur
"""

class Util:
    
    @staticmethod
    def convertDataToPrint(data, start, length):
        accumulator = ''
        x = 0
        for item in range((int)(length/2)):
            accumulator += data[start + (x)] + data[start + (x + 1)]
            x += 2
        return accumulator
    
    @staticmethod
    def bufferToHex(buffer, start, count):
        accumulator = ''
        for item in range(count):
            accumulator += '%02X' % buffer[start + item]
        return accumulator
    
    @staticmethod
    def printOnConsole(strng, prnt):
        if('printOnConsole' == prnt):
            print(strng)