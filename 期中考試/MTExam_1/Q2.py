a=open("protein.txt")
protein=a.read()
s="ACDEFGHIKLMNPQRSTVWY"
for i in range(0,len(s)):
    print(str(s[i])+":"+str(protein.count(s[i])))
a.close()
