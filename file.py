f = open('test')
i = 1 
for l in f:
    print(i,end="= ")
    print(len(l),end="\t")
    i=i+1
print()
