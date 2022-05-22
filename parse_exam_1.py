from Bio import SeqIO

seq = SeqIO.parse("Section1/Chap6/sample_1.fasta","fasta")
print(type(seq))

for s in seq:
    print(type(s))
    print(s)
    print("")
