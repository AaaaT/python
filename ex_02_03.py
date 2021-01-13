#print("PY4E")
#Teacher's solution
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xp = float(xh) * float(xr)
print("Pay:", xp)


#Our solution
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
#xp = int(xh) * int(xr)
xp = float(xh) * float(xr)
print("Pay:{}".format(xp))
