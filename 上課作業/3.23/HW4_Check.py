file=open("Ans.txt","r")
file_1=open("GrayOutput.txt","r")
file_2=open("CheckOutput.txt","w")
c=[]
d=[]
q=[]
for line in file_1:
    a=line.rstrip("\n")
    b=a.split("\t")[1]
    w=a.split("\t")[0]
    c.append(b)
    q.append(w)
for line in file:
    e=line.rstrip("\n")
    f=e.split("\t")[1]
    d.append(f)
file_3=file_2.write("This in put is\tGrayOutput.txt\n")
for i in range(1,6,1):
    aa=c[i]
    bb=d[i]
    s=q[i]
    ans=(aa==bb)
    file_3=file_2.write(str(s)+"\t"+str(ans)+"\n")
print(file_3)
file.close()
file_1.close()
file_2.close()

    
    
        
        
