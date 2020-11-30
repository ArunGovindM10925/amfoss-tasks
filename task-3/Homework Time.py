first=1
second=2
third=3
L=[1,2,3]
for l in range(0,5):
    m=int(input())
    for i in range (2,m):
        sum=first+second+third
        L.append(sum)
        first=second
        second=third
        third=sum
    res=str(L[m])
    final=res.rstrip("0")
    print(final[::-1])