from Bio import SeqIO

aa=SeqIO.parse("../Section1/Chap13/13.2.fasta","fasta")

for i in aa:
    seq=i.seq
    print(i.id)
    print("A ",seq.count("A"))
    print("C ",seq.count("C"))
    print("G ",seq.count("G"))
    print("T ",seq.count("T"))
    print("N ",seq.count("N"))

