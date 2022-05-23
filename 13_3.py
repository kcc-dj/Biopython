from Bio.Seq import Seq

aa = Seq("ACATTA")
print("comp_seq",Seq.complement(aa))
print("rev_comp_seq",Seq.reverse_complement(aa))
