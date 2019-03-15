#%%
from maths import mathdata as mtx
from maths import mathstat as mts
from maths import matrix as mat
from sympy import *

list1=  [133,295,166,175,339,124,256,126,191,280,125,198]
e = mtx.mathdata(list1)
# g = mts.mathstat(s=74.53410852,mu=200.6666,n=12)
init_printing()
init_session()

x = symbols('x')
inte = Integral(sqrt(1/x),x)
print(inte.doit())

# e.get_hist()
# #%%
# print("(1 - alpha)\t=\t"+str(e.find_confidence(166.2408,235.0925)))


# print(g.find_borne(0.95))


# print("A X B= \n"+str(mat.produit_vectoriel("1;2","2 3")),end="\n\n")
# print("A*B= \n"+str(mat.produit_scalaire("1 2 4","2;3;2")),end="\n\n")
