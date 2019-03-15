
#%%
import numpy as np
import statistics as st
from scipy.stats import t

import matplotlib.pyplot as plt
#%%

#%%
class mathdata:

    numList = []
    mu_,s_,x_,sigma_=0,0,0,0
    n_,N_ = 1,1



    def __init__(self,numlist = []):
        
        self.numList = numlist
        self.n_ = len(self.numList)
        self.comp_moyenne()
        self.comp_ecarttype()
        print("n\t\t=\t"+str(self.n_))
        print("Moyenne(x)\t=\t"+ str(self.mu_))
        print("Ecart-Type(s)\t=\t"+ str(self.s_))
    
    def get_hist(self):
        plt.hist(self.numList)
        plt.axvline(self.mu_,color='white')
        plt.axvline(self.mu_-self.s_,linestyle='dashed',color='blue')
        plt.axvline(self.mu_+self.s_,linestyle='dashed',color='blue')
        return plt


    def comp_moyenne(self):
        self.mu_ = np.mean(self.numList)

    def comp_ecarttype(self):
        self.s_ = st.stdev(self.numList)

        
    def find_confidence(self,borneInf, borneSup):
        me = (borneSup-borneInf)/2
        ecartTypeX = self.s_/(self.n_)**(1/2)
        tn = me/ecartTypeX
        print("ecart type_x\t=\t"+ str(ecartTypeX))
        print("t_n-1;a/2\t=\t"+str(tn))
        res = t.cdf([-tn,tn],self.n_-1) #tCdf
        return res[1]-res[0]

    def find_borne(self,confidence):
        alpha = 1-confidence
        print("alpha\t=\t"+ str(alpha))
        ecartTypeX = self.s_/(self.n_)**(1/2)
        me = t.isf(1-alpha/2,self.n_-1) #inverse Student
        me = me*ecartTypeX
        return [self.mu_+me,self.mu_-me]





#%%
