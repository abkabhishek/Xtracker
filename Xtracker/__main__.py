
import fire



from core.xt_fetch import FetchTests


class XT:
    
    
    def __init__(self):
        self.FetchTests =  FetchTests("BDDTests","0*.py","/Users/abk/dev/python/ofc/bit/sb-automation-py-behave/BDDFramework/steps","step.*")
        
    def GetTests(self):
        self.FetchTests.fetch_test_functions()
        self.FetchTests.save_in_xl("TestFunctions.xlsx")
        
if __name__=="__main__":
    fire.Fire(XT)
    