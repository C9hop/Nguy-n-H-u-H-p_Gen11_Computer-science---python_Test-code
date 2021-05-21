#Viết một chương trình cho phép người dùng xóa 1 số trong 1 dãy số đã có ở vị trí đầu hoặc cuối
arr = ["1", "5", "-9", "3"]
print("Hi there, this is our sequence:")
print(", ".join(arr))
def output():
    x = str(input(("Where do you want to delete (head/tail): ")))
    if x=="tail":
        arr.pop()
        print("This is our new sequence: ")
        print(", ".join(arr))
    elif x=="head":
        arr.pop(0)
        print("This is our new sequence: ")
        print(", ".join(arr))
    else:
        return output()
output()


