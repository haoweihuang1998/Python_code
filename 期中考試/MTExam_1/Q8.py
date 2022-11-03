dna=open("genomic_dna.txt")
dna1=dna.read()
a=open("genomic_dna.coding.txt","w")
for i in range(0,len(dna1),3):
    a.write("Exon "+str(int(i/3+1))+":"+dna1[i:i+3]+"\n")
a.close()
dna.close()
