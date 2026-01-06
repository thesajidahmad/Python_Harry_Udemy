# 3. Tuples and Operations on Tuples

# Create a tuple coordinates = (10, 20) and print both elements.

coordinates = (10, 20)

print(coordinates)

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.

# coordinates[0] = 50 #TypeError: 'tuple' object does not support item assignment

# Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.

corlist = list(coordinates)

corlist[0] = 50

coordinates = tuple(corlist)

print(coordinates)