# Gioi han boi dau ()
# Ngan cach boi dau phay
# chua dc moi gia tri
# Nhanh hon List
# Co the dung lam Key


arrTuple = ("10","Linh")
print(arrTuple)

arrTuple = ()

#Create Tupble Generator Expression

tup = (i for i in range(0,30) if (i %2 == 0))
arrTuple = tuple(tup)
print(arrTuple)

# Check value
check = 1 in arrTuple
print(check)

print (arrTuple [1])

print(arrTuple.__len__())
print(arrTuple.count(10))
print(arrTuple.index(10))
print(arrTuple[10])

