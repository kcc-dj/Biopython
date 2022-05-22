from Bio.Seq import Seq

aa = Seq("AAGTGACAGGGATTG")
bb= aa.translate(to_stop=True)
print(bb)
