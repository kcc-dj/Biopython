import pandas as pd

aa=pd.read_csv("../Section2/read_sample.txt")

print(aa)

f = open("../Section2/read_sample.txt","r")
r=f.readlines()
f.close()
for i in r:
    print(i.strip())

