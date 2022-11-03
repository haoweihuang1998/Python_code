file = open("sequence1.txt","r")
sequence = file.read()

A_count = 0
T_count = 0
C_count = 0
G_count = 0
i=0
while i<len(sequence):
  if sequence[i] == "A":
    A_count = A_count + 1
  elif sequence[i] == "T":
    T_count = T_count + 1
  elif sequence[i] == "C":
    C_count = C_count + 1   
  else :
    G_count = G_count + 1    
  i=i+1
print(str(sequence) + "\n")
print("A_count = " + str(A_count) + "\n")
print("T_count = " + str(T_count) + "\n")
print("C_count = " + str(C_count) + "\n")
print("G_count = " + str(G_count) + "\n")
