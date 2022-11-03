ww=open("codons.txt","r")
dic={}
s=0
for line in ww:
    s=s+1
    if s <62:
        b=line.rstrip("\n").split("\t")
        RNAkey=b[0]
        AAvalue=b[1]
        dic[RNAkey]=AAvalue
    else:
        b=line.rstrip("\n").split("\t")
        RNAkey=b[0]
        dic[RNAkey]=""
a=["Homo_sapiens_ADRA2A.fasta","Homo_sapiens_BRCA2.fasta","Homo_sapiens_HTR1B.fasta","Homo_sapiens_PRKN.fasta","musculus_P53.fasta"]
b=[966,229,620,135,101]
c=[2363,10485,1792,1085,1273]
def hahaha(a,b,c):
    r=0
    w=""
    q=""
    dna=open(a)
    for line in dna:
        r=r+1
        if r>=2:
            w=w+line
    y=w.replace("\n","")
    z=y[b-1:c-1]
    z=z.replace("T","U")
    if len(z)%3==0:
        for x in range(0,len(z),3):
                q=q+dic[z[x:x+3]]
    elif len(z)%3==1:
        z=z[0:-1]
        for x in range(0,len(z),3):
            q=q+dic[z[x:x+3]]
    elif len(z)%3==2:
        z=z[0:-2]
        for x in range(0,len(z),3):
            q=q+dic[z[x:x+3]]
    else:
        pass
    return("File name:"+"\t"+"mRNA\\"+a+"\n"+"mRNA length:"+"\t"+str(len(y))+"\n"+"5'UTR:"+"\t"+y[0:b-1]+"\n"+"3'UTR:"+"\t"+y[c:] +"\n"+"Protein:"+"\t"+q)
v=""
for i in range(len(a)):
    v=v+hahaha(a[i],b[i],c[i])+"\n"
    m=open("output.txt","w")
    m.write(v)
    m.close()
ww.close()
                
