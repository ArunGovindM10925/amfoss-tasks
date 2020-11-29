flag=1
t=int(input())
for i in range(t):
    n=int(input())
    if n % 2 == 0:
        if n % 5 == 0 :
            print(5)
            flag=0
        else:
            print(2)
            flag=0
    else:
        for j in range(n-2,2,-2):
            if n % j == 0:
                print(j)
                flag=0
                break
    if flag == 1:
        print(n)
    flag=1        