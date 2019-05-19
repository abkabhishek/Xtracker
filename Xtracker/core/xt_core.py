"""
This is the core class of Xtracker
All processing should be initiated through this class only


Basic Structure


Project
    TC Track
        - Provide following info:
            -- Test Location
            -- File Pattern
            -- Test Pattern
            -- Other Info to parse from Test File
        - Fetch Test Info and Save into DB


    TC Update
        - Provide Test Result File
        - Process and save status of Test Result in DB

    TC Analyse
        - Get info of Test as per History Test Results


"""




class XTcore:
    
    def __init__(self):
        pass

