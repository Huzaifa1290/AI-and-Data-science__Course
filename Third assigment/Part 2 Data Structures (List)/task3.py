# Task 3: List operations
fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a) Check if apple is present
if "apple" in fruits:
    print("Apple found at index:", fruits.index("apple"))

# b) Replace raspberry and pineapple with orange
fruits[1:3] = ["orange"]
print("After replacement:", fruits)

# c) Insert apricot at index 2
fruits.insert(2, "apricot")
print("After insertion:", fruits)

# d) Extend with other items
fruits.extend(["car", "bike", "aeroplane"])
print("After extending:", fruits)
