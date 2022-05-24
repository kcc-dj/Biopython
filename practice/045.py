from random import randint

aa=[]
while True:
    bb=randint(1,45)
    if not bb in aa:
        aa.append(bb)
        print(bb)
    if len(aa)==6:
        break

