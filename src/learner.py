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
                sum=sum+float(input[x])*self.weights[index][x]
            
            result.append(sum)
        return result
    
    def backward_prop(self,result,input,desired):
        eps=0.000000
        for x in range(self.onodes):
            eps=eps+math.sqrt((desired[x]-result[x])**2)
            for index in range(self.inodes):
                error=self.lr*(desired[x]-result[x])*float(input[index])
                self.weights[x][index]=self.weights[x][index]+error
        return eps   
        
    
    def learn(self):
        err=100000.000
        result=[]
        iter=0
        while err>self.epsilon and iter<self.maxiter:
            #if iter%20==0:
            #   print str(err)+","
            err=0.000
            iter=iter+1
            for index in range(self.examples):
                result=self.forward_prop(self.input[index])
                eps=self.backward_prop(result,self.input[index],self.desired[index])
                #print result," ",self.weights
                err=err+eps
        
     
         
                
        
#items.append(Item('Inception',['thriller','medium','eng']))
#items.append(Item('Frozen',['children','short','eng']))
#items.append(Item('3 idiots',['comedy','long','hindi']))
#items.append(Item('Omen',['horror','medium','eng']))
#items.append(Item('The Wedding bride',['romance','short','eng']))   

def runNeuralNetwork(train_input,train_output,inodes,onodes,weights,lr,eps,threshold,maxiter):
    nn=ANN(inodes,onodes,weights,lr,eps,threshold,maxiter)  
    #nn.addinput([2,4,4,5])
    #nn.addinput([2,1,0,2])
    #nn.addinput([3,4,5,2])
    #nn.addinput([2,1,4,3])
    #nn.addinput([2,1,2,2])
    #nn.addoutput([4.5])
    #nn.addoutput([1.5])
    #nn.addoutput([3.5])
    #nn.addoutput([3])
    #nn.addoutput([2.5])
    for inp in train_input:
        nn.addinput(inp)
    for op in train_output:
        nn.addoutput(op)
    nn.learn()
    print nn.weights 
    return nn.forward_prop([2,1,2,2])
   
#print runNeuralNetwork([],[],4,1,[[0.5,0.5,0.5,0.5]],0.005,0.0001,2.5,10000)
                   
                
        
        
    
    
        