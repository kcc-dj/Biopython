from Bio.Seq import Seq
from Bio.SeqUtils import GC, MeltingTemp
aa=Seq("AAGTGACAGGGATTG")
bb=aa.reverse_complement()
cc = GC(bb)
print(cc)
dd=MeltingTemp.Tm_Wallace(bb)
print(dd)
