"""


"""
from tinydb import TinyDB, Query


class DB:

    def __init__(self,json_db_path):
        self.db = TinyDB(json_db_path)
        self.tables =[]

    def create_table(self,table_name):
        pass

    def insert(self,json_data,table_name=None):
        self.db.insert(json_data)

    def update(self,search_item,search_value,data):
        self.db.update(data,Query()[search_item]==search_value)

    def get(self,item_name,expected_value):
        q_obj = Query()
        result = self.db.search(q_obj[item_name]==expected_value)
        return result

    def getAll(self):
        return self.db.all()

    def delete(self,search_item,search_value):
        self.db.remove(Query()[search_item]==search_value)

    def deleteAll(self):
        self.db.purge()



if __name__=="__main__":
    # Sample Run
    db = DB("sample.json")
    data1 = {"Name":"Abhishek","Age":32}
    data2 = {"Name":"Ram","Age":30}
    data3 = {"Name":"Suresh","Age":40}
    # db.insert(data1)
    # db.insert(data2)
    # db.update("Name","Ram",data3)
    # print(db.get("Name","Suresh"))
    # db.delete("Name","Suresh")
    db.deleteAll()
    print(db.getAll())

