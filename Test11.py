#Sử dụng đệ quy
#----------------------------------------------------------------------------------------------------------
#Tìm số bé nhất trong 1 dãy số
def minimum(l, val):
  if not l[1:]:
     return val
  return minimum(l[1:], l[0] if l[0] < val else val)

l = [34, 23, 12, 4, 5]
print(minimum(l, l[0]))
#Tính giai thừa của 1 số nhập bởi người dùng
def giaithua(n):
    if n == 1:
        return 1
    else:
        return (n * giaithua(n-1))
num1 = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", num1, "là:", giaithua(num1))

#Tính một số trong dãy fibbonacii f(n) = f(n - 1) + f(n - 2) và f(0) = 1, f(1) = 1 với n nhập từ người dùng
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
num2 = int(input("Nhập n: "))
print("Số fibonacci f (",num2,") là:", fibonacci(num2))

#Tìm ước số chung lớn nhất của 2 số bằng phương pháp Euclid
def uscln(a, b):
    if (b == 0):
        return a
    else:
        return uscln(b, a % b)
a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))

