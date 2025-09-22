class Product:
    def __init__(self, id = None ,name = None, quantity = None,price= None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
    def __str__(self): #__str__ tự động tương tác khi xuất ra màn hình giao diện
        return  f"{self.id}\t{self.name} {self.quantity} {self.price}"
