k=0
t=int(input())
for i in range(t):
    n=int(input())
    if n<3 :
        print(0)
    for j in range(3,n,3):
        sum=sum+j
        k=k+5
        sum=sum+k
    print(sum)