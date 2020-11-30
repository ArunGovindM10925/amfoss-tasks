t=int(input())
for i in range(t):
    n=int(input())
    sum=0
    if n<3 :
        print(0)
    else:
        for j in range(3,n):
            if(j%3 == 0):
                sum=sum+j
            elif(j%5 == 0):
                sum=sum+j
        print(sum)
