n =  int(input())

l = [1,122,212,221,333,1333,3133,3313,3331,4444,122333,1223334444]
d = {1:1,2:2,3:[3,{1,2}],4:[4,{1,3}],5:[5,{1,4},{2,3}],6:[]}

if n>1 and n<=22:
    print(22)
elif n>22 and n<=122:
    print(122)
elif n>122:
    l = len(str(n))
    if l>=3:
        if n<=212:
            print(212)
        elif n>212 and n<=221:
            print(221)
strn = str(n)
le = len(strn)
frst = n[0]
highest = [s=s+str(i)*i for i in range(n[0],0,-1)]
if n<int(''.join(highest)):
    
