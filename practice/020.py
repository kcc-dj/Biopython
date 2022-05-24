num = int(input("Enter: "))
try:
    print(10/num)
except ZeroDivisionError:
    print("can not divide with zero")
except ValueError:
    print("plz insert value")
