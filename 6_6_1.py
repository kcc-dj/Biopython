from Bio import SeqIO,Entrez

aa=SeqIO.read("Section1/Chap6/HM624086.1.gbk","genbank")

print(aa.description)
print(aa.annotations["taxonomy"])
print(len(aa.seq))
