
import sys
import re
from pprint import pprint


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
    
#     def getInfo(self):
#         pprint(FD.get_files(self.DirPath,"*/*.py"))
        
        
    def read_file(self,FileName):
        
        with open(FileName) as fl:
            data= fl.readlines()
        
        return data
    
    def get_match_all(self,pat,source,n):
            
        x = re.findall(pat, source)
        if x:
            return [n,*x]
        else:
            return None
        
    def parse_code_info(self,fileName=None):
        if fileName:
            Data = self.read_file(fileName)
        else:
            Data = self.read_file(self.FilePath)


        for num, item in enumerate(Data,1):
            D = self.get_match_all(self.Pat_Funtion, item,num)
            if D:
                self.InfoFunction.append(D)
                continue
            D = self.get_match_all(self.Pat_Class, item,num)
            if D:
                self.InfoClass.append(D)
                continue
            
            D = self.get_match_all(self.Pat_Import, item,num)
            if D:
                self.InfoImport.append(D)
                continue
            
            D = self.get_match_all(self.Pat_FromImport, item,num)
            if D:
                self.InfoImport.append(D)
                continue
            
    def print_all_info(self):
        print("File : {}".format(self.FilePath))
        pprint(self.InfoImport)
        pprint(self.InfoClass)
        pprint(self.InfoFunction)
        
                
            
        
        
        
    
Fls = FD.get_files("/Users/abk/dev/python/ofc/bit/sb-automation-py-behave/BDDFramework","*/*.py")

for fl in Fls:
    FS = FL_Structrure(fl)
    # CS.getInfo()
    FS.parse_code_info()
    FS.print_all_info()
