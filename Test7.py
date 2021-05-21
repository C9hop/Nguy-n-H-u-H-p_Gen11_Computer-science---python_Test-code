#Viết một chương trình cho phép người dùng thêm 1 số vào đầu 1 dãy số đã có
arr = ["1", "5", "-9", "3"]
print("Hi there, this is our sequence:")
print(", ".join(arr))
add = str(input("What do you want to add: "))
arr.insert(0, add)
print("This is our new sequence: ")
print(", ".join(arr))


