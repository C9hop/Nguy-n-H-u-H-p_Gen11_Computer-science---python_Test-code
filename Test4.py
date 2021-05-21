#Viết chương trình in ra 1 dãy số từ 1 đến 20
arr = []
for i in range(1,21):
    arr.append(str(i))
print("Dãy số từ 1 đến 20: ")
print(", ".join(arr))
