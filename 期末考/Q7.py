a=open("protein_seqs.fasta","r")
count=0
s=["A",'C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
w=""
y=""
for line in a:
    count=count+1
    if count%2==0:
        w=w+line
    else:
        y=y+line
Q=w.split("\n")
Z=y.replace(">","").split("\n")
def hahaha(t):
    p=""
    s=["A",'C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    for i in range(len(s)):
        u=t.count(s[i])
        f=len(t)
        v=(u*100/f)
        p=p+str(round(v,1))+"\t"
    return p
b=open("protein_seqs.acc","w")
b.write("Prot")
for i in range(len(s)):
    b.write("\t"+s[i])
for i in range(10):
    b.write("\n"+Z[i]+"\t"+hahaha(Q[i]))

b.close()
a.close()

    
