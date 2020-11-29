sum=2
t=int(input())
for i in range(t):
    n=int(input())
    first=2
    second=3
    third=5
    while third < n:
        if third % 2 == 0:
            sum=sum+third        
        first,second=second,third
        third=first+second
    print(sum)
    sum=2