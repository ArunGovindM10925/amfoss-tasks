t=int(input())
count,numbersdone=0,0
for i in range(t):
    n=int(input())
    number=2*n
    flag=0
    while flag==0:
        for j in range(1,n+1):
            if(number%j==0):
                count+=1
        if(count==n):
            flag=1
            numbersdone+=1
            print(number)
        if(numbersdone==t):
            break
        number=number+n
        count=0
