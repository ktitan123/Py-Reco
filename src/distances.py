import math
#import data

def average_items(user,d):
	l=d[user]
	sum=0.0
	n=0
	for x in l:
		if x != 'x':
			sum=sum+x
			n=n+1
	return (sum/float(n))

def average_users(item,d):
    n=0
    sum=0.0
    index=movies[item]
    for x in d:
        if d[x][index]!='x':
            sum=sum+d[x][index]
            n=n+1
    return (sum/float(n))
    

def pearson(user1,user2,d):
	i=0
	n1=0.0
	av1=average_items(user1,d)
	av2=average_items(user2,d)
	d1=0.0
	d2=0.0
	while i<len(d[user1]):
		if d[user1][i]!='x' and d[user2][i]!='x':
			n1=n1+(av1-d[user1][i])*(av2-d[user2][i])
			d1=d1+(av1-d[user1][i])*(av1-d[user1][i])
			d2=d2+(av2-d[user2][i])*(av2-d[user2][i])
		i=i+1
	return (0.001+n1)/(0.001+math.sqrt(d1)*math.sqrt(d2))

def calc(user1,user2,ratings,index):
    val=ratings[user2][index]
    if val=='x':
        return 0.00
    return (((pearson(user1,user2,ratings))**2))*val
     
	 
    
def euclid(user1,user2,d):
    i=0
    dist=0.000
    i=0
    while i < len(d[user1]):
        if d[user1][i]!='x' and d[user2][i]!='x':
            dist=dist+ (d[user1][i]-d[user2][i])**2
    return math.sqrt(dist)
    
    

  
      
    