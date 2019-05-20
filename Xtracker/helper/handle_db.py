"""


"""
from tinydb import TinyDB, Query


class DB:

    def __init__(self,json_db_path):
        self.db = TinyDB(json_db_path)

    def insert(self,json_data,table=None):
        if table:
            self.db.table(table).insert(json_data)
        else:
            self.db.insert(json_data)

    def update(self,search_item,search_value,data,table=None):
        if table:
            self.db.table(table).update(data,Query()[search_item]==search_value)
        else:
            self.db.update(data,Query()[search_item]==search_value)

    def get(self,item_name,expected_value,table=None):
        if table:
            result = self.db.table(table).search(Query()[item_name]==expected_value)
        else:
            result = self.db.search(Query()[item_name]==expected_value)
        return result

    def getAll(self,table=None):
        if table:
            return self.db.table(table).all()
        else:
            return self.db.all()

    def delete(self,search_item,search_value,table=None):
        if table:
            self.db.table(table).remove(Query()[search_item]==search_value)
        else:
            self.db.remove(Query()[search_item]==search_value)

    def deleteAll(self,table=None):
        if table:
            self.db.table(table).purge()
        else:
            self.db.purge()



if __name__=="__main__":
    # Sample Run
    db = DB("sample1.json")
    data1 = {"Name":"Abhishek","Age":32}
    data2 = {"Name":"Ram","Age":30}
    data3 = {"Name":"Suresh","Age":40}
    db.insert(data1,table="PR1")
    db.insert(data2,table="PR1")
    db.update("Name","Ram",data3,table="PR1")
    print(db.get("Name","Suresh",table="PR1"))
    db.delete("Name","Suresh",table="PR1")
    # db.deleteAll()
    print(db.getAll(table="PR1"))

