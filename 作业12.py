from random import randint
n=int(input("how many numbers do you want to generate?"))
nums=[]
for i in range(n):
    nums.append(randint(1,999))
for each in sorted(nums):
    print(each,end='\t')