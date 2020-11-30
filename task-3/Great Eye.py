listwords=[]
sum=0
t=int(input())
for i in range(0,t):
    k=int(input())
    sentence=input()
    words = len(sentence.split())
    listwords=sentence.split()
    if k in range(1,len(listwords)):
        for j in listwords[k]:
            sum=sum+ord(j)
        print(sum)
        sum=0
    else:
        print(-1)