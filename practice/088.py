aa=[0,1]

def fibo(num):
    for i in range(num):
        aa.append(aa[-2]+aa[-1])
    return aa

print(fibo(10))
