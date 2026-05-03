n=int(input("Please input a whole number(>=3):"))
f1=1
f2=1
print("The Fibonacci sequence is；1,1",end="")
for i in range(3,n+1):
    f=f1+f2
    print(",%d"%f,end="")
    f1,f2=f2,f