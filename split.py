from Bio.Seq import Seq

mrna = Seq("AUGAACUAAGUUUAGAAU")
ptn = mrna.translate()
print(ptn)
for seq in ptn.split("*"):
    print(seq)
