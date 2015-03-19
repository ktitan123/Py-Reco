import math


def pearson(user1,user2,d):
	i=0
	n1=0.0
	av1=average(user1,d)
	av2=average(user2,d)
	d1=0.0
	d2=0.0
	while i<len(d[user1]):
		if d[user1][i]!='x' and d[user2][i]!='x':
			n1=n1+(av1-d[user1][i])*(av2-d[user2][i])
			d1=d1+(av1-d[user1][i])*(av1-d[user1][i])
			d2=d2+(av2-d[user2][i])*(av2-d[user2][i])
		i=i+1
	return (0.001+n1)/(0.001+math.sqrt(d1)*math.sqrt(d2))
    
def euclid(user1,user2,d):
    i=0
    n=len(