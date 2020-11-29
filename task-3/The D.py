n=int(input())
s=int((n-1)/2)
d="D"
m=1
for i in range(0,s):
    print("*"*s+"D"*m+"*"*s)
    s=s-1
    m=m+2
print("D"*n)
s=int((n-1)/2)
m=m-2
k=1
for j in range(0,s):
    print("*"*k+"D"*m+"*"*k)
    k=k+1
    m=m-2