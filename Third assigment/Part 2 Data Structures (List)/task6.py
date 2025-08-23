# Task 6: Gadget list operations
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

strings = [x for x in Gadgets if isinstance(x, str)]
numbers = [x for x in Gadgets if isinstance(x, int) or isinstance(x, float)]

print("Strings:", strings)
print("Numbers:", numbers)

# b) Sort strings ascending and descending
print("Strings Ascending:", sorted(strings))
print("Strings Descending:", sorted(strings, reverse=True))

# c) Sort by length
print("Strings by Length:", sorted(strings, key=len))

# d) Sort numbers ascending and descending
print("Numbers Ascending:", sorted(numbers))
print("Numbers Descending:", sorted(numbers, reverse=True))
