#Viết một chương trình cho phép người dùng thêm 1 số vào cuối 1 dãy số đã có
arr = ["1", "5", "-9", "3"]
print("Hi there, this is our sequence:")
print(", ".join(arr))
add = str(input("What do you want to add: "))
arr.append(add)
print("This is our new sequence: ")
print(", ".join(arr))
