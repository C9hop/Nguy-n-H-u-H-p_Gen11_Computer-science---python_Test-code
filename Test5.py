#Viết chương trình in ra 1 dãy số từ 1 đến 20, chia hết cho 3
arr = []
for i in range(1,21):
    if i % 3 == 0:
        arr.append(str(i))
print("Dãy số từ 1 đến 20, chia hết cho 3: ")
print(", ".join(arr))