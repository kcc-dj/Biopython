from Bio import SwissProt

aa=open("../Section1/Chap10/P02649.txt")
record=SwissProt.read(aa)
print(type(record))
aa.close()
