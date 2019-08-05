import glob
import os
from pprint import pprint
class FD:
    
    @staticmethod
    def get_files(root_path,file_pattern,specific_folder="**"):
        files = [f for f in glob.glob(root_path + specific_folder+"/"+file_pattern, recursive=True)]
        return files


    @staticmethod
    def get_folders(root_path,folder_pattern,specific_folder="*"):
        folders = [f for f in glob.glob(root_path + specific_folder+folder_pattern+"/", recursive=True)]
        return folders

if __name__=="__main__":
    print(FD.get_folders("","*","*"))