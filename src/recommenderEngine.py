#import data
import item
import distances
import learner
import similiarity as sim
import item
import operator

def normalize(values):
    maxval=[]
    minval=[]
    for index in range(len(values[0])):
        maxv=0
        minv=99999999
        for p in range(len(values)):
            maxv=max(maxv,float(values[p][index]))
            minv=min(minv,float(values[p][index]))
        maxval.append(maxv)
        minval.append(minv)
    for index in range(len(values)):
        for p in range(len(values[0])):
            x=(float(values[index][p])-minval[p])/(maxval[p]-minval[p]+0.0001)
            values[index][p]=x
    return values

def train(trainfile):
    f=open(trainfile,"r")
    input=[]
    output=[]
    flag=0
    weights=[[0.8,0.8,0.8,0.8]]
    nn=learner.ANN(4,1,weights,0.005,0.0001,0.5,50000)
    for line in f:
        if flag==0:
            flag=1
            continue
        val=line.split(",")
        inp=val[0:4]
        op=[]
        op.append(float(val[4]))
        input.append(inp)
        nn.addoutput(op)
    input=normalize(input)
    for x in input:
        nn.addinput(x)
        
    nn.learn()
    return nn.weights
    
    
    
     
        
    
    
def recommend(user,ratings,items,moviesrev,movies,weights):
    candidates=[]
    i=0
    for i in range(len(ratings[user])):
        if ratings[user][i]=='x':
            candidates.append(moviesrev[i])
        i=i+1
    if len(candidates)==0:
        return "None"
    reco={}
    for candidate in candidates:
        metrics=[]
        x= sim.getitem2item(candidate,user,ratings,movies,moviesrev)
        metrics.append(x)
        x= sim.getperson2person(candidate,user,ratings,movies,moviesrev)
        metrics.append(x)
        x= sim.getperson2item(candidate,user,ratings,movies,moviesrev)
        metrics.append(x)
        x= sim.getproperty(candidate,user,ratings,movies,moviesrev,items)
        metrics.append(x)
        #Test neural network with data in sim as input 
        #and get the correct weights
        #predicted reco value of the current candidate would be 
        #weighted sum of all similiarity values
        sum=0.0
        #weights=[1.0,1.0,1.0,1.0]
        for i in range(4):
            sum = sum + weights[0][i]*metrics[i]
        reco[candidate]=sum
    
    reco = sorted(reco.items(), key=operator.itemgetter(1),reverse=True)
    return reco    
        
        
        
        
        
def initialize(itemfile,ratingsfile):
    items=[]
    movies={}
    moviesrev={}
    items,moviesrev,movies= item.readitems(itemfile,items,movies,moviesrev)
    ratings = item.readratings(ratingsfile,items,movies,moviesrev)
    return ratings,items,movies,moviesrev
    
ratings,items,movies,moviesrev = initialize("itemlist.txt","ratings.txt")
#print moviesrev[1]

weights = train("train.csv")   
print weights
print recommend('john',ratings,items,moviesrev,movies,weights)
    
    
    