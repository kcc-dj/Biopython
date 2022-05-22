from Bio.Seq import Seq

exon_seq = Seq("ATCGGCATTA")
count_a=exon_seq.count("A")
print(count_a)
