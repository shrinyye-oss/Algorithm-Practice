num=input("Please input a whole number:")
count=0
sum_digit=0
for i in num:
    if count:
       print("+",end='')
    count+=1
    sum_digit+=int(i)
    print(i,end='')
print("=",sum_digit)