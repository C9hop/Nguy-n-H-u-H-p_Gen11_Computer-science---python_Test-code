#Viết một chương trình cho phép người dùng nhập vào một năm (ví dụ 1989) 
# in ra xem năm người dùng nhập vào có phải năm nhuận không
year = int(input("Nhập vào 1 năm bất kỳ: "))
if(year/4==0) :
    print("Năm " + str(year) + "là một năm nhuận")
else:
    print("Năm " + str(year) + " là một năm không nhuận")