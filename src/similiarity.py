#import data
import distances
import math

def sim_useritem(user,item,d):
    i=0
    reco={}
    den=0.0
    num=0.0
    index=movies[item]
    if d[user][index]=='x':
        for person in d:
			if person != user:
				num=num+distances.calc(user,person,d,i)
				den=den+(distances.pearson(user,person,d)**2)
        return round((num/den),2)
    else:
        return d[user][index]
        
	
    
