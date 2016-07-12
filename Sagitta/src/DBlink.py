'''
Created on 01 lug 2016

@author: claudio
'''
import MySQLdb
from Document import Document
class DBlink:
    '''
    classdocs
    '''
    
    def __init__(self):
        self.doc=Document("config.txt")
        
    def config(self,params):
        self.get_doc().write(params)
        
    def get_doc(self):
        return self.doc
    
    def get_cursore(self):
        a=self.get_doc().get_params()
        database=MySQLdb.connect(host=a["host"],user=a["user"],passwd=a["passwd"],db=a["db"])
        return database.cursor()
    
    def get_table(self):
        params=self.get_doc().get_params()
        return params["table"]
    
    def get_db(self):
        return self.get_doc().get_params()["db"]
        
    def send_query(self,query):
        cursore=self.get_cursore()
        cursore.execute(query)
        return cursore.fetchall()