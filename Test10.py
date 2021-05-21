#Viết một class có tên là Counter có 
# 1 thuộc tính (property) là count 
# và hai phương thức là tick() và reset()
#-------------------------------------------------------------------------
#Viết hàm khởi tạo (init) cho class này, trong hàm khởi tạo, cho count = 0
#Viết hàm tick(), mỗi khi tick() được gọi, tặng count lên 1
#Viết hàm reset(), mỗi khi reset() được gọi, đưa count về 0
class Counter: 
    def __init__(self):
        self.count = 0
    def tick(self):
        self.count = self.count + 1
    def reset(sefl):
        sefl.count = 0
c = Counter()
print(c.count)
c.tick()
print(c.count)







