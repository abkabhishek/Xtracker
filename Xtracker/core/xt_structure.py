
import sys
import re
from pprint import pprint
from certifi import __main__


sys.path.append(".")

from Xtracker.helper.handle_files import FD


class FL_Structrure:
    
    def __init__(self,FLPath):


        
        self.FilePath = FLPath
        
        self.Pat_Funtion = "def .*:"
        self.Pat_Class = "class .*:"
        self.Pat_Import = "^import .*"
        self.Pat_FromImport = "^from .* import .*"
        
        self.InfoClass = []
        self.InfoFunction = []
        self.InfoImport = []
        self.InfoClassFunction = {}
    
#     def getInfo(self):
#         pprint(FD.get_files(self.DirPath,"*/*.py"))
        
        
    def _read_file(self,FileName):
        
        with open(FileName) as fl:
            data= fl.readlines()
        
        return data
    
    def _get_match_all(self,pat,source,n):
            
        x = re.findall(pat, source)
        if x:
            return [n,*x]
        else:
            return None
        
    def parse_code(self,fileName=None):
        if fileName:
            Data = self._read_file(fileName)
        else:
            Data = self._read_file(self.FilePath)


        for num, item in enumerate(Data,1):
            D = self._get_match_all(self.Pat_Funtion, item,num)
            if D:
                self.InfoFunction.append(D)
                continue
            D = self._get_match_all(self.Pat_Class, item,num)
            if D:
                self.InfoClass.append(D)
                continue
            
            D = self._get_match_all(self.Pat_Import, item,num)
            if D:
                self.InfoImport.append(D)
                continue
            
            D = self._get_match_all(self.Pat_FromImport, item,num)
            if D:
                self.InfoImport.append(D)
                continue
            
        for item in self.InfoClass:
            self.InfoClassFunction[item[0]]=item[1]
        
        for item in self.InfoFunction:
            self.InfoClassFunction[item[0]]=item[1]
            
    def print_structure(self):
        print("="*30)
        print("File : {}".format(self.FilePath))
        print("-"*30)
        print("Imports :-")
        for item in self.InfoImport:
            print(" "*4,end="")
            print(item[1])
        print("-"*30)
        print("Classes/Functions :-")
        for lineNum in sorted(self.InfoClassFunction.keys()):
            x = 4
            item = self.InfoClassFunction[lineNum]
            if item[0]=="d":
                x=8
            print(" "*x,end="")
            print(item)
            
            

        
                
            
        
        
        
if __name__=="__main__":
    # Fls = FD.get_files("Path/To/ProjectRoot","*/*.py")
    Fls = FD.get_files("/Users/abk/dev/python/ofc/bit/sb-automation-py-behave","**/*.py")
    
    for fl in Fls:
        FS = FL_Structrure(fl)
        FS.parse_code()
#         FS.print_structure()
        pprint(FS.InfoClassFunction)
