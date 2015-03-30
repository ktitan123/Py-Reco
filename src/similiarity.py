#import data

import distances
import math
import learner

def person2itemSimiliarity(user,item,d,movies,moviesrev):
    i=0
    reco={}
    den=0.0
    num=0.0
    index=movies[item]
    if d[user][index]=='x':
        for person in d:
			if person != user and d[person][index]!='x':
				num=num+distances.calc(user,person,d,i)
				den=den+(distances.pearson(user,person,d)**2)
        return round((num/(den+0.0001)),2)
    else:
        return d[user][index]
        
def item2itemSimiliarity(item1,item2,d,movies,moviesrev):
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
        av=distances.average_items(user,d)
        sum1=sum1+(d[user][index1]-av)*(d[user][index2]-av)
        sum2=sum2+(d[user][index1]-av)**2
        sum3=sum3+(d[user][index2]-av)**2
    return (sum1/(sum2*sum3+0.0001))
    
def person2personSimiliarity(user1,user2,d,movies,moviesrev):
    items=[]
    n=len(d[user1])
    i=0
    while i<n:
        if d[user1][i]!='x' and d[user2][i]!='x':
            items.append(i)
        i=i+1
    sum1=0.0
    sum2=0.0
    sum3=0.0
    for item in items:
        av=average_users(item,d)
        index=movies[item]
        sum1=sum1+(d[user1][index]-av)*(d[user2][index1]-av)
        sum2=sum2+(d[user1][index]-av)**2
        sum3=sum3+(d[user2][index]-av)**2
    return (sum1/(sum2*sum3+0.0001))	
    
def propertySimiliarity(item1,item2,movies,moviesrev,items):
    list1=[]
    list2=[]
    for x in items:
        if x.name==item1:
            list1=x.properties
        if x.name==item2:
            list2=x.properties
    ans=0.000
    for index in range(len(list1)):
        if list1[index]==list2[index]:
            ans=ans+1.0000
    return ans
    
    
def getitem2item(candidate,user,ratings,movies,moviesrev):
    sum=0.0000
    for i in range(len(ratings[user])):
        if ratings[user][i]!='x':
            it=moviesrev[i]
            sum=sum+item2itemSimiliarity(candidate,it,ratings,movies,moviesrev)*ratings[user][i]
    return sum
    
def getperson2person(candidate,user,ratings,movies,moviesrev):
    sum=0.0000
    i=movies[candidate]
    for x in ratings:
        if x!=user and ratings[user][i]!='x':
            sum=sum+person2personSimiliarity(user,x,ratings,movies,moviesrev)*ratings[x][i]
    return sum
    
def getperson2item(candidate,user,ratings,movies,moviesrev):
    return person2itemSimiliarity(user,candidate,ratings,movies,moviesrev)
        
def getproperty(candidate,user,ratings,movies,moviesrev,items):
    sum=0.0000
    for i in range(len(ratings[user])):
        if ratings[user][i]!='x':
            it=moviesrev[i]
            sum=sum+propertySimiliarity(candidate,it,movies,moviesrev,items)*ratings[user][i]
    return sum    
    