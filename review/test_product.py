from review.product import Product

p1 = Product(100, "thuốc lào", 4, 20)
#xuất p1 ra màn hình
print(p1)

p2 = Product(200, "Thuốc trị cảm",5,30)
p1 = p2
print("thông tin của p1 =")
print(p1)
p1.name = "Thuốc tăng tự trọng"
print("thông tin của p2 =")
print(p2) 