from Bio import SeqIO

record = SeqIO.read("Section1/Chap5/J01636.1.fasta","fasta")
print(type(record))
print(record)
