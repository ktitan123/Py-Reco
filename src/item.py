

class Item():
    def __init__(self,name,properties):
        self.name=name
        self.properties=properties
        self.property_names=['genre','duration','language']
        
    def addproperty(self,val,name):
        self.properties.append(val)
        self.property_names.append(name)
        
    def changeproperty(self,index,newval,newname):
        self.properties[index]=newval
        self.property_names[index]=newname
        
        
 #sample      
items=[]
items.append(Item('Inception',['thriller','medium','eng']))
items.append(Item('Frozen',['children','short','eng']))
items.append(Item('3 idiots',['comedy','long','hindi']))
items.append(Item('Omen',['horror','medium','eng']))
items.append(Item('The Wedding bride',['romance','short','eng']))