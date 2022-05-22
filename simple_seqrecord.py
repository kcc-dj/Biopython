from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq = Seq("ACGT")
seqRecord=SeqRecord(seq)

print(seqRecord)
seqRecord=SeqRecord(seq,id="NC_1111",name="Test")
print(seqRecord)
