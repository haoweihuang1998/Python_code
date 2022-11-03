string_DNA='TCAATCAAGATCGCGGCCGGCTCG'
print("Length:"+str(len(string_DNA)))
print("CG count:"+str(string_DNA.count('CG')))
print("TCG site:"+str(string_DNA.find('TCG')))
print("startswith():"+str(string_DNA.startswith('TCAAC')))
print(string_DNA[4:9])
