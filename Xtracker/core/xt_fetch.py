
import os
import sys
import re
from pprint import pprint

sys.path.append(".")

from Xtracker.helper.handle_files import FD
from Xtracker.core.xt_structure import FL_Structrure

class FetchTests:
    
    def __init__(self,module_name,test_file_name_pattern="Test*.py",test_directory="Test",test_function_regex="test.*"):

        self.module_name = module_name
        self.test_file_name_pattern = test_file_name_pattern
        self.test_directory = test_directory
        self.test_function_regex = test_function_regex
        self.test_files =[]
        self.test_functions = {}
        
        
    
    
    def get_test_files(self):
        self.test_files = FD.get_files(self.test_directory,self.test_file_name_pattern)

        
    
    def get_test_functions(self):
        self.get_test_files()
        for fl in self.test_files:
            FS = FL_Structrure(fl)
            FS.parse_code()
#             pprint(FS.InfoClassFunction)
            

            for k,v in FS.InfoClassFunction.items():
#                 for k,v in item.items():
#                 print(v)
                x = re.findall(self.test_function_regex, v)
                if x:
                    self.test_functions[fl[-50:]]=[k,v]
                
        
        
if __name__=="__main__":
    FT = FetchTests("BDDTests","0*.py","/Users/abk/dev/python/ofc/bit/sb-automation-py-behave/BDDFramework/steps","step.*")
    FT.get_test_functions()
    pprint(FT.test_functions)
    