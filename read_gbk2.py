from Bio import SeqIO

gbk = SeqIO.read("Section1/Chap6/KT225476.2.gbk","genbank")
print(gbk.id)
print(gbk.description)
print(gbk.seq)
