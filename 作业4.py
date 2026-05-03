n=int(input("How many numbers do you want to input:"))
s=0
for i in range(1,n+1):
    x=float(input("Number %d:"%i))
    s+=x
print("The average of the %d numbers is %f."%(n,s/n))