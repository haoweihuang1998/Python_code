#密碼子與胺基酸對應字典---------------------------------------
Fcon = open("codons.txt","r")

CodonDict = {} #dict
for line in Fcon:
	item = line.rstrip("\n").split("\t")
	
	RNAkey = item[0]
	AAvalue = item[1]
	CodonDict[RNAkey] = AAvalue 

Fcon.close()
#胺基酸個數字典------------------------------------------------
aminoacids = {
	'K': 0, 'G': 0, 'V': 0, 'C': 0, 'N': 0, 
	'Y': 0, 'U': 0, 'M': 0, 'P': 0, 'Q': 0,
	'E': 0, 'L': 0, 'W': 0, 'A': 0, 'H': 0,
	'F': 0, 'D': 0, 'I': 0, 'S': 0, 'R': 0
}

#for a_key in CodonDict:
#	aminoacids[CodonDict[a_key]] = 0

print(CodonDict)
print(aminoacids)

#開啟一個序列檔案-------------------------------------------
#閃過第一行&處理換行"\n"
mRNA_file = open("AMPK.txt", "r")

mRNA_sequence = ""
line_count = 0 
for line in mRNA_file:
	line_count = line_count + 1
	if (line_count >= 2 ): 
		mRNA_sequence = mRNA_sequence + line

mRNA_sequence = mRNA_sequence.replace("\n","")


print(mRNA_sequence)
print("length "+str(len(mRNA_sequence)))
#_____確認長度與序列

#切割核酸序列(3個3個切)&轉譯<codons to AAs>--------------------------------------------------
#這裡沒有避免非3倍數的例外，請加入此功能
protein = ""
for i in range(0, len(mRNA_sequence), 3):
	codon = mRNA_sequence[i:i+3]
	codon = codon.replace("T", "U")
	protein = protein + CodonDict[codon] #<codons to AAs>
	
print(protein)
#計算AAs的個數---------------------------------------
for i in range(0, len(protein)):
	if protein[i] != "*": 
		aminoacids[protein[i]] += 1

print(aminoacids)
mRNA_file.close()




#protein = ""
#amino_acids_count = 0
#for i in range(0, len(mRNA_sequence), 3):
#for i in range(1, len(mRNA_sequence)-2, 3):
#	codon = mRNA_sequence[i:i+3]
#	codon = codon.replace("T", "U")
#	if CodonDict[codon]=="*": print("{"+codon+"}")
#	amino_acids_count += 1
#	protein = protein + CodonDict[codon]
	

#for i in range(1, len(mRNA_sequence)-2, 3):
#for i in range(2, len(mRNA_sequence)-2, 3):






#		line = line.rstrip("\n")
	#print(line)
	#skip fist line







#mRNA_sequence = mRNA_file.read()
#print(mRNA_sequence)
#print(" ---- ")
#mRNA_sequence = mRNA_sequence.rstrip("\n")
#mRNA_sequence = mRNA_sequence.replace("\n","")
#print(mRNA_sequence)





	
	

