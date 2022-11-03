string_DNA='TCAATCAAGATCGCGGCCGGCTCG'
string_DNA=string_DNA.lower()
string_DNA=(string_DNA.replace('a','T'))
string_DNA=(string_DNA.replace('t','A'))
string_DNA=(string_DNA.replace('g','C'))
string_DNA=(string_DNA.replace('c','G'))
print(string_DNA)
