aa=int(input("insert one integer"))
if not aa%3 and not aa%7:
    print("multiple of 3 and 7")
elif not aa%3:
    print("multiple of 3")
elif not aa%7:
    print("mulple of 7")
else:
    print("not multiple of 3 and 7")
