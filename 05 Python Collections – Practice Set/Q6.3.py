# 6. Bonus Challenges

# Write a program that merges two dictionaries into one.

products = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 8500,
    "Headphones": 1500
}
contacts = {"sajid": "7739207110", "priyanshu": "9102429844", "makhdum": "7549001649"}

products.update(contacts)

print(products)