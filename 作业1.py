n=int(input("Please input a number: "))
fact=1
for i in range(n,1,-1):
    fact*=i
print("The factorial of%d is %d."%(n,fact))
