# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:12:57 2019

@author: Mallikarjun Tirlapur
"""

from MyUtil import Util
from Header import HeaderComp
from Directory import DirectoryComp
from Applet import AppletComp
from Import import ImportComp
from ConstantPool import ConstantPoolComp
from Class import ClassComp
from Descriptor import DescriptorComp
from Method import MethodComp
from StaticField import StaticFieldComp
from ReferenceLocation import ReferenceLocationComp
from Export import ExportComp
from Debug import DebugComp
import zipfile
import os.path

class ComponentProcessor:

    def __init__(self):
        self.headerComp = HeaderComp()
        self.dirComp = DirectoryComp()
        self.appltComp = AppletComp()
        self.imprtComp = ImportComp()
        self.cpComp = ConstantPoolComp()
        self.classComp = ClassComp()
        self.descrptrComp = DescriptorComp()
        self.methdComp = MethodComp()
        self.staticFldComp = StaticFieldComp()
        self.refLocationComp = ReferenceLocationComp()
        self.exportComp = ExportComp()
        self.debugComp = DebugComp()
        self.hashMap = dict()
        
    #read the binary from the cap component
    def readInCapFile(self, directry, filePath, fileName, compnt):
        with open(directry + "\\" + filePath, "rb") as f:
            data = f.read()
            binData = Util.bufferToHex(data, 0, len(data))
            compnt.setBinaData(binData)
            self.hashMap.update({fileName: compnt})

    def processHeader(self):
        print("Header")
        self.hashMap['Header'].processHeaderComp()
        
    def processDirectory(self):
        print("\nDirectory")
        self.hashMap['Directory'].processDirectoryComp()

    def processApplet(self):
        print("\nApplet")
        self.hashMap['Applet'].processAppletComp()
        
    def processImport(self):
        print("\nImport")
        self.hashMap['Import'].processImportComp()
        
    def processCP(self, prnt):
        Util.printOnConsole("\nConstantPool", prnt)
        self.hashMap['ConstantPool'].processCPComp(prnt)
        
    def processDescriptor(self, prnt):
        self.processMethod('false')
        Util.printOnConsole("\nDescriptor", prnt)
        self.hashMap['Descriptor'].processDescriptorComp(self.hashMap['Method'], prnt)
        
    def processClass(self):
        self.processDescriptor('false')
        print("\nClass")
        self.hashMap['Class'].processClassComp(self.hashMap['Descriptor'])
        
    def processMethod(self, prnt):
        self.processCP('false')
        Util.printOnConsole("\nMethod", prnt)
        self.hashMap['Method'].processMethodComp(self.hashMap['ConstantPool'], prnt)
        
    def processStaticField(self):
        print("\nStaticField")
        self.hashMap['StaticField'].processStaticFieldComp()
        
    def processRefLoc(self):
        print("\nRefLocation")
        self.hashMap['RefLocation'].processReferenceLocationComp()
        
    def processExport(self):
        print("\nExport")
        self.hashMap['Export'].processExportComp()
        
    def processDebug(self):
        print("\nDebug")
        self.hashMap['Debug'].processDebugComp()

    def readInComponentBinaries(self, zfile, dirctry):
        for zinfo in zfile.filelist:
            #########get the component name######### 
            if (zinfo.filename[-3:] == "cap"):
                words = (zinfo.filename).split("/")
                output = ''
                fp = ''
                for n, i in enumerate(words[-1:]):
                    if n % 5 == 0:
                        output += '\n'
                    output += "{0:>15s}".format(i)
                    fp = i
            ########################################
                if (fp == 'Header.cap'):
                    self.readInCapFile(dirctry, zinfo.filename, 'Header', self.headerComp)

                elif(fp == "Directory.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Directory', self.dirComp)
                        
                elif(fp == "Applet.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Applet', self.appltComp)
                        
                elif(fp == "Import.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Import', self.imprtComp)
                        
                elif(fp == "ConstantPool.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'ConstantPool', self.cpComp)
                        
                elif(fp == "Descriptor.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Descriptor', self.descrptrComp)
                        
                elif(fp == "Class.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Class', self.classComp)
                        
                elif(fp == "Method.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Method', self.methdComp)
                        
                elif(fp == "StaticField.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'StaticField', self.staticFldComp)
                        
                elif(fp == "RefLocation.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'RefLocation', self.refLocationComp)
                        
                elif(fp == "Export.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Export', self.exportComp)
                        
                elif(fp == "Debug.cap"):
                    self.readInCapFile(dirctry, zinfo.filename, 'Debug', self.debugComp)
    
    def main(self, dirctry, cmpt):
        zfile = zipfile.ZipFile(dirctry, "r" )
        path = os.path.dirname(dirctry)
        zfile.extractall(path)
        self.readInComponentBinaries(zfile, path)
        
        if ((cmpt == 'header') or (cmpt == 'all')):
            self.processHeader()

        if((cmpt == "directory") or (cmpt == 'all')):
            self.processDirectory()
                
        if 'Applet' in self.hashMap:
            if((cmpt == "applet") or (cmpt == 'all')):
                self.processApplet()
                
        if((cmpt == "import") or (cmpt == 'all')):
            self.processImport()
                
        if((cmpt == "cp") or (cmpt == 'all')):
            self.processCP('printOnConsole')
                
        if((cmpt == "descriptor") or (cmpt == 'all')):
            self.processDescriptor('printOnConsole')
                
        if((cmpt == "class") or (cmpt == 'all')):
            self.processClass()
                
        if((cmpt == "method") or (cmpt == 'all')):
            self.processMethod('printOnConsole')
                
        if((cmpt == "staticfield") or (cmpt == 'all')):
            self.processStaticField()
                
        if((cmpt == "refloc") or (cmpt == 'all')):
            self.processRefLoc()
                
        if 'Export' in self.hashMap:
            if((cmpt == "export") or (cmpt == 'all')):
                self.processExport()
                
        if((cmpt == "debug") or (cmpt == 'all')):
            self.processDebug()         
