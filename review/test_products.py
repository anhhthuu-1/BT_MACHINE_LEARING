from review.product import Product
from review.products import ListProducts

lp = ListProducts()
lp.add_product(Product(100,"Product_1", 200, 10))
lp.add_product(Product(200,"Product_2", 10, 15))
lp.add_product(Product(150,"Product_3", 80, 8))
lp.add_product(Product(300,"Product_4", 50, 20))
lp.add_product(Product(250,"Product_5", 150, 17))
print("List of Products:")
lp.print_products()

lp.desc_sort_products()
print("List of Products after descending sort:")
lp.print_products()

lp.desc_sort_products2()
print("List of Products after descending sort:")
lp.print_products()