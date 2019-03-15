
#%%
import numpy as np
import statistics as st
from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt
#%%
class mathstat:

    mu_,s_,x_,sigma_=None,None,None,None
    n_,N_ = 1,1

    def __init__(self,mu=None,s=None,x=None,sigma=None,n=0,N=0,**kwargs):
        self.mu_ = mu
        self.s_ = s
        self.x_ = x
        self.sigma_ = sigma
        self.n_ = n
        self.N_ = N
        
        if s!=None and n>0 and sigma == None:
            self.sigma_ = s/(n)**(1/2)
        
    def find_confidence(self,borneInf, borneSup):
        me = (borneSup-borneInf)/2
        if self.sigma_ == None and self.s_ != None:
            self.sigma_ = self.s_/(self.n_)**(1/2)
        tn = me/self.sigma_
        print("ecart type_x = "+ str(self.sigma_))
        print("t_n-1;a/2 ="+str(tn))
        res = t.cdf([-tn,tn],self.n_-1) #tCdf
        return res[1]-res[0]

    def find_borne(self,confidence):
        alpha = 1-confidence
        print("alpha = "+ str(alpha))
        if self.sigma_ == None:
            self.sigma_ = self.s_/(self.n_)**(1/2)
            me = t.isf(1-alpha/2,self.n_-1) #inverse Student
        else:
            me = norm.isf(1-alpha/2,0,1)
        
        me = me*self.sigma_
        return [self.mu_+me,self.mu_-me]


        
        



