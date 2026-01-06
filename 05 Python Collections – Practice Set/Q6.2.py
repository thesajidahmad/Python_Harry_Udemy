# 6. Bonus Challenges

# Given a dictionary of products and their prices, find the product with the highest price.

products = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 8500,
    "Headphones": 1500
}

a = products.values()
b = max(a)
print(b)

print(max(products.values()))