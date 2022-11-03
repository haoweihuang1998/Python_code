code=open("codons.txt")
target=open("protein_coding_DNA.fasta","w")
c=[]
q=[]
for line in code:
    a=line.rstrip("\n")
    b=a.split("\t")[1]
    w=a.split("\t")[0]
    c.append(b)
    q.append(w)
for i in range(0,len(c)):
    aa=c[i]
    s=q[i]
    target.write(">"+str(s)+"\n"+str(aa)+"\n")
target.close()
code.close()

