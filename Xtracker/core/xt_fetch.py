
import os
import sys
import re
from pprint import pprint
from prettytable import PrettyTable

sys.path.append(".")

from helper.handle_files import FD
from helper.handle_xl import XL_Man

from core.xt_structure import FL_Structure


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

        
    
    def fetch_test_functions(self):
        self.get_test_files()

        for fl in self.test_files:
            FS = FL_Structure(fl)
            FS.parse_code()

            self.test_functions[fl] =[]
            for k,v in FS.InfoClassFunction.items():

                x = re.findall(self.test_function_regex, v)
                if x:
                    self.test_functions[fl].append([k,v])
                    
    def _get_test_id(self,testName):
        
        x = re.findall("[_0-9]{9}", testName)
        return x
                    
    def print_test_functions(self):
        print("File,LineNumber,TestFunction,")
        for k,v in self.test_functions.items():
            print(k+",,,")
            for item in v:
                print(","+str(item[0])+","+item[1]+",")
                
    def print_test_table(self):
        x = PrettyTable()
        x.field_names = ["File","LineNumber", "TestFunction"]
        x.align["LineNumber"] = "l"
        x.align["TestFunction"] = "l"
        x.align["File"] = "l"
        for k,v in self.test_functions.items():
#             print(k+",,,")
            x.add_row([k[-35:],"",""])
            for item in v:
#                 print(","+str(item[0])+","+item[1]+",")
                x.add_row(["",str(item[0]),item[1]])
        print(x)

        
                
    def save_in_xl(self,xlPath):
        xl = XL_Man()
        xl.add_sheet("Test_functions")
        xl.write("Test_functions",1,1,"File")
        xl.write("Test_functions",1,2,"LineNumber")
        xl.write("Test_functions",1,3,"FunctionSignature")
        xl.write("Test_functions",1,4,"FunctionName")
        xl.write("Test_functions",1,5,"TestID")
        row=2
        col=1
        for k,v in self.test_functions.items():

            xl.write("Test_functions",row,col,k)
            row+=1
            col=1
            for item in v:
                col+=1
                xl.write("Test_functions",row,col,str(item[0]))
                col+=1
                xl.write("Test_functions",row,col,str(item[1]))
                col+=1
                xl.write("Test_functions",row,col,str(item[1].split("(")[0]))
                testids = self._get_test_id(str(item[1].split("(")[0]))
                for id in testids:
                    col+=1
                    xl.write("Test_functions",row,col,id[1:])
                row+=1
                col=1
        xl.save(xlPath)

        
        
        
if __name__=="__main__":
    FT = FetchTests("BDDTests","0*.py","/Users/abk/dev/python/ofc/bit/sb-automation-py-behave/BDDFramework/steps","step.*")
    FT.fetch_test_functions()
#     FT.print_test_functions()
    FT.print_test_table()
#     FT.save_in_xl("TestFunctions.xls")
    

    