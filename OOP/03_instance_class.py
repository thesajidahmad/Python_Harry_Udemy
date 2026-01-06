class Product:
    company = "Asus"

    def __init__(self, name, price, discount, rating, company):
        self.name = name
        self.price = price
        self.discount = discount
        self.rating = rating
        self.company = company
    
    def get_info(self):
        print(f"Product name is {self.name}, Price is {self.price}, Discount is {self.discount} and the rating is {self.rating}")

p1 = Product("Apple Charger", 1700, "20%", 4.5, "Apple")
p1.get_info()
print(p1.company)
print(Product.company)
print(dir(p1))