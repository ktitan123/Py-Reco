#import data
import item
import distances
import learner
import similiarity as sim
import item
import operator




    
    
def recommend(user,ratings,items,moviesrev,movies):
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
        weights=[1.0,1.0,1.0,1.0]
        for i in range(4):
            sum = sum + weights[i]*metrics[i]
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
print recommend('peter',ratings,items,moviesrev,movies)
    
    
    
    
    