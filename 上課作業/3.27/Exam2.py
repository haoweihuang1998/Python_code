DNA="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna=DNA.lower()
dna1=dna.replace("a","T")
dna2=dna1.replace("t","A")
dna3=dna2.replace("c","G")
dna4=dna3.replace("g","C")
print(dna4)
