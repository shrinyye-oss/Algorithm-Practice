for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            num= 100*i+ 10*j+k
            if num==i**3 +j**3 +k**3:
                print(num)
