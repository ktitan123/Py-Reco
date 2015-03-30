

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

           
        
def readitems(filename,items,moviesrev,movies):
    f=open(filename,"r")
    count=0
    for line in f:
        val=line.split(",")
        #print val
        items.append(Item(val[0],[val[1],val[2],val[3]]))
        movies[val[0]]=count
        moviesrev[count]=val[0]
        count=count+1
    print "movies: ", movies
    print "moviesrev ", moviesrev
    f.close()
    return items,moviesrev,movies
    

def readratings(filename,items,movies,moviesrev):
    f=open(filename,"r")
    ratings={}
    x=len(items)
    count=0
    for line in f:
        val=line.split(",")
        user=val[0]
        movie=val[1]
        rating=float(val[2])
        if user in ratings:
            index=movies[movie]
            ratings[user][index]=rating
        else:
            list=[]
            for i in range(x):
                list.append('x')
            index=movies[movie]
            ratings[user]=list
            ratings[user][index]=rating
    f.close()
    return ratings
    

#items=[]    
#moviesrev={}
#movies={}
#items,moviesrev,movies=readitems("itemlist.txt",items,moviesrev,movies)
#print items
#print moviesrev
#print movies
#print readratings("ratings.txt",items,moviesrev,movies)