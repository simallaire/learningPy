def fib(n):
    a,b=0,1
    while a<n:
        print(a,end="\n")
        a,b=b,a+b
    print()
def fib2(n):
    a,b,i=0,1,0
    while i < n:
        print(a,end="\n")
        a,b,i=b,a+b,i+1

if __name__ == "__main__":
    import sys
    if sys.argv[1]=="fib":
        fib(int(sys.argv[2]))
    if sys.argv[1]=="fib2":
        fib2(int(sys.argv[2]))