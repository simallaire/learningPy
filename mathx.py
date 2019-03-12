
#%%
import numpy as np
import statistics as st
from scipy.stats import t
import matplotlib.pyplot as mpt
#%%
class mathx:

    numList = [133,295,166,175,339,124,256,126,191,280,125,198]
    moyenneS=0
    n = len(numList)
    ecartTypeS=0
    sample = True

    def __init__(self):
        self.comp_moyenne()
        self.comp_ecarttype()
        print("Moyenne(x) = "+ str(self.moyenneS))
        print("Ecart-Type(s) = "+ str(self.ecartTypeS))
        
    def comp_moyenne(self):
        self.moyenneS = np.mean(self.numList)

    def comp_ecarttype(self):
        self.ecartTypeS = st.stdev(self.numList)

    def isSample(self,isSamp):
        sample = isSamp
        
    def find_Confidence(self,borneInf, borneSup):
        me = (borneSup-borneInf)/2
        ecartTypeX = self.ecartTypeS/(self.n)**(1/2)
        tn = me/ecartTypeX
        print("ecart type_x = "+ str(ecartTypeX))
        print("t_n-1;a/2 ="+str(tn))
        res = t.cdf([-tn,tn],self.n-1) #tCdf
        return res[1]-res[0]

    def find_borne(self,confidence):
        alpha = 1-confidence
        print("alpha = "+ str(alpha))
        ecartTypeX = self.ecartTypeS/(self.n)**(1/2)
        me = t.isf(1-alpha/2,self.n-1) #inverse Student
        me = me*ecartTypeX
        return [self.moyenneS+me,self.moyenneS-me]


#%%
e = mathx()



#%%
print("(1 - alpha) = "+str(e.find_Confidence(166.2408,235.0925)))


#%%
print(e.find_borne(0.99))


#%%
x = np.linspace(0,len(e.numList)-1,len(e.numList))
e.numList.sort()
mpt.plot(x,e.numList)
mpt.plot(e.moyenneS)
mpt.show()


#%%

# a = '\\frac{a}{b}'  #notice escaped slash
# mpt.plot()
# mpt.text
# mpt.text(10.5, 10.5,'$%s$'%a)
# mpt.show()

#%%



#%%



