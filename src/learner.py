#implementation of a single layer artificial neural network

#import data
import math


class ANN():
    def __init__(self,inodes,onodes,weights,lr,epsilon,threshold,maxiter):
        self.layers=1
        self.inodes=inodes
        self.onodes=onodes
        self.bias=0
        self.weights=weights
        self.input=[]
        self.training=True
        self.desired=[]
        self.lr=lr
        self.examples=0
        self.epsilon=epsilon
        self.threshold=threshold
        self.maxiter=maxiter
        
    def addinput(self,input):
        self.input.append(input)
        self.examples=self.examples+1
    
    def addoutput(self,output):
        self.desired.append(output)
        
    def forward_prop(self,input):
        result=[]
        for index in range(self.onodes):
            sum=0.0
            for x in range(self.inodes):
                sum=sum+input[x]*self.weights[index][x]
            if sum>=self.threshold:
                sum=1
            else:
                sum=0
            result.append(sum)
        return result
    
    def backward_prop(self,result,input,desired):
        eps=0.000000
        for x in range(self.onodes):
            eps=eps+(desired[x]-result[x])**2
            for index in range(self.inodes):
                error=self.lr*(desired[x]-result[x])*input[index]
                self.weights[x][index]=self.weights[x][index]+error
        return eps   
        
    
    def learn(self):
        err=100000.000
        result=[]
        iter=0
        while err>self.epsilon and iter<self.maxiter:
            err=0.000
            iter=iter+1
            for index in range(self.examples):
                result=self.forward_prop(self.input[index])
                eps=self.backward_prop(result,self.input[index],self.desired[index])
                err=err+eps
        
                
        
        
nn=ANN(2,1,[[1,0]],0.1,0.1,0,100)  
nn.addinput([0,0])
nn.addinput([0,1])
nn.addinput([1,0])
nn.addinput([1,1])
nn.addoutput([0])
nn.addoutput([1])
nn.addoutput([1])
nn.addoutput([1])
nn.learn()
print nn.weights     
                
                
        
        
    
    
        