# Giới hạn bởi cặp ngoặc vuông []
# Phần tử của list được cách nhau bởi dấu phẩy ,
# List có thể chứa mọi giá trị, và chứa chính nó

#Example

arrName = ["Linh", "Kim", "Thuyet","25/08/2018]",2018]

print(arrName)

# List in List

arrName = ["Linh", "Kim", "Thuyet","25/08/2018]",2018, ["Test","Test"],arrName]

print(arrName)

# Create list 0 - 29

arrNumber = [i for i in range(30)]
print(arrNumber)

# List contructor

arrTemp = list("Linh")
print(arrTemp)

# Add data
arrTemp += "Thuyet"
print(arrTemp)
print(arrTemp[0])