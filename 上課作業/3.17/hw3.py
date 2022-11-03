q=open("DNA.txt")
q1=q.read()

my_file=open("output.txt","w")
my_file.write("Your student ID:0517064"+"\n")
 
dna1=len(q1)
my_file.write("length:"+str(dna1)+"\n")

dna2=q1.count("CG")
my_file.write('"CG "count:'+str(dna2)+"\n")

dna3=q1.find("TCG")
my_file.write('"TCG" site:'+str(dna3)+"\n")

dna4=q1.startswith("TCAAC")
my_file.write('startswith("TCAAC"):'+str(dna4)+"\n")

dna5=q1[4:9]
my_file.write("string_DNA[4:9]:" + str(dna5)+ "\n")

s1=q1[:13]
s2=q1[13:21]
s3=q1[21:]
s4=s2.lower()
my_file.write("hw2 answer:"+str(s1)+str(s4)+str(s3)+"\n")

my_file.close()
q.close()