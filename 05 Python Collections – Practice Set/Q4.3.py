# 4. Sets and Set Methods

# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}

# Find their:
# 1. Union
# 2. Intersection
# 3. Difference ( a - b )

a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)  # 1. Union
print(c)

d = a.intersection(b)   # 2. Intersection
print(d)

e = a.difference(b) # 3. Difference ( a - b )
print(e)