from itertools import combinations
count=0
length=int(input())
string=input()
res = [string[x:y] for x, y in combinations(
            range(len(string) + 1), r = 2)]
if length == 1:
    if('1' in string or '0' in string):
        count+=1
else:
    res = list(dict.fromkeys(res))
    res.remove(string)
    for i in res:
        ones = i.count('1')
        zeros = i.count('0')
        if(ones != zeros):
            count+=1
print(count)