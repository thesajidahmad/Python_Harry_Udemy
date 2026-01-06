class Product:

    def __init__(self, name, price, discount, rating):
        self.name = name
        self.price = price
        self.discount = discount
        self.rating = rating
    
    def get_info(self):
        print(f"Product name is {self.name}, Price is {self.price}, Discount is {self.discount} and the rating is {self.rating}")

p1 = Product("Apple Charger", 1700, "20%", 4.5)
p1.get_info()