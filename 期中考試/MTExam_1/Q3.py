dna=open("dp_sequences.txt")
c=[]
for line in dna:
    a=line.rstrip("\n")
    b=a.split("\t")
    c.append(b)
for i in range(0,len(c)):
    aa=c[i]
    bb=str(aa)
    cc=bb.replace("[","")
    dd=cc.replace("]","")
    ee=dd.replace("'","")
    print(str(i+1)+"\t"+"DNA"+"\t"+str(ee))
    
#I can't change to Prot
