from Bio import SeqIO
import gzip

aa = gzip.open("Section1/Chap6/sample_1.fastq.gz","rt")
seq = SeqIO.parse(aa,"fastq")
print(type(seq))

for s in seq:
    print(type(s))
    print(s.seq)
