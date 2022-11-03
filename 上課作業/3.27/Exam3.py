a=open("ss.fasta","w")

sequence_one="ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence_two="actgatcgacgatcgatcgatcacgact"
sequence_three="ACTGAC-ACTGT--ACTGTA----CATGTG"
a.write(">ABC123"+"\n"+sequence_one+"\n")
a.write(">DEF456"+"\n"+sequence_two.upper()+"\n")
a.write(">HIJ789"+"\n"+sequence_three)

a.close()
