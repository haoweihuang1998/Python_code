def combi(r,n):
    return 1 if n==0 else combi(r,n-1)*(r-n+1)//n
height=12
c=[[combi(r,n) for n in range(r+1)] for r in range(height)]
r=0
n=0
while r<len(c):
    print(("%"+str((len(c)-r)*3)+"s")%"",end="")
    while n<len(c[r]):
        print("%6d" % c[r][n],end="")
        n+=1
    n=0
    r=r+1
    print()
