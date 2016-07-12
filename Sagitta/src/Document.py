'''
Created on Jul 12, 2016

@author: claudio
'''

class Document:
    '''
    classdocs
    '''


    def __init__(self,name):
        self.name=name
        self.params=self.read()
        
    def read(self):
        doc= open(self.name, "r").read()
        p=doc.split("\n")
        params={}
        for i in p:
            lista_riga=i.split(";")
            if lista_riga!=[""]:
                    params[lista_riga[0]]=lista_riga[1]
        return params
    
    def get_params(self):
        return self.params
    
    def set_params(self,params):
        self.params=params
    
    def write(self,params):
        doc = open(self.name, "w")
        for p in params.keys():
            riga = "%s;%s\n"%(p,params[p])
            doc.write(riga)
        doc.close()
        self.set_params(self.read())