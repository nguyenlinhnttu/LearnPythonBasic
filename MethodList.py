arrList = [1, 2, 3, 4, 5, 6, 7, 8, 10,9]
# Count Phan tu
print(arrList.count(1))

# Get index of value
print(arrList.index(4))


#Size List
print(arrList.__len__())

#CopyList

arrCopy = arrList.copy()

print(arrCopy)

# Clear data
arrCopy.clear()

# Add data

arrCopy.append( 2009 )
arrCopy.append( 2009 )

print(arrCopy)

# Remove

arrCopy.remove(2009)
print(arrCopy)

# Remove at index

arrCopy.pop(0)

print(arrCopy)


# Sort List
arrList.sort()
print(arrList)

# Reverse list
arrList.reverse()
print(arrList)