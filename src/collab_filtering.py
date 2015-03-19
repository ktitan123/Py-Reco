
import math




def average(user,d):
	l=d[user]
	sum=0.0
	n=0
	for x in l:
		if x != 'x':
			sum=sum+x
			n=n+1
	return (sum/float(n))

	
def itemSimilarity(item1, item2, d):
    users=[]
    index1=movies[item1]
    index2=movies[item2]
    for x in d:
        if d[x][index1]!='x' and d[x][index2]!='x':
            users.append(x)
    sum1=0.0
    sum2=0.0
    sum3=0.0
    for user in users:
        av=average(user,d)
        sum1=sum1+(d[user][index1]-av)*(d[user][index2]-av)
        sum2=sum2+(d[user][index1]-av)**2
        sum3=sum3+(d[user][index2]-av)**2
    return (sum1/(sum2*sum3+0.0001))
    
        
        
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




def calc(user1,user2,d,index):
	return (((pearson(user1,user2,d))**2))*d[user2][index]

def recommend(user,d):
    candidates=[]
    i=0
    while i<len(d[user]):
        if d[user][i]=='x':
            candidates.append(moviesrev[i])
        i=i+1
    if len(candidates)==0:
        return "None"
    reco=[]
    for c in candidates:
        i=0
        num=0.0
        den=0.0
        while i<len(d[user]):
            if d[user][i]!='x':
                num=num+itemSimilarity(moviesrev[i],c,d)*d[user][i]
                den=den+itemSimilarity(moviesrev[i],c,d)
            i=i+1
        reco.append((((num/den)+0.001),c))
    reco.sort()
    return reco
        

def predict(user,d):
	i=0
	reco={}
	den=0.0
	num=0.0
	while i<len(d[user]):
		if d[user][i]=='x':
			for person in d:
				if person != user:
					num=num+calc(user,person,d,i)
					den=den+(pearson(user,person,d)**2)
			reco[moviesrev[i]]=round((num/den),2)
		i=i+1
	return reco
			
		






moviesrev={0:'Inception',1:'Hangover',2:'Excorcism',3:'Frozen',4:'Mission Impossible'}
movies={'Inception':0,'Hangover':1,'Excorcism':2,'Frozen':3,'Mission Impossible':4}
d={}
d['john']=[1.5,'x',4.0,'x',3.0]
d['jack']=[0.0,0.5,4.5,1.0,2.0]
d['alice']=[2.0,2.0,1.5,2.5,2.0]
d['peter']=[2.5,2.5,1.0,5.0,3.0]

print d
print recommend('john',d)
#print itemSimilarity('Inception','Hangover',d)



