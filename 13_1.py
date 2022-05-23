from Bio import SeqIO

aa=SeqIO.parse("../Section1/Chap13/13.2.fasta","fasta")
bb=list()
for i in aa:
    i=i.lower()
    bb.append(i)
SeqIO.write(aa,"13.2.upper.fasta","fasta")
print(bb)

