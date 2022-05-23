from Bio import Entrez
import pandas as pd
Entrez.email = "kcc0225@naver.com"

handle = Entrez.efetch(db="nucleotide",id="NC_002058.3",rettype="gb",retmode="xml")

records = Entrez.parse(handle)
for record in records:
    for journal in record["GBSeq_references"]:
        print(journal["GBReference_title"])
