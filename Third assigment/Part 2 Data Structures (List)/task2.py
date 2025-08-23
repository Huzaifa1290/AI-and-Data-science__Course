# Task 2: Separate strings, numbers, and Boolean data from the list
data = ["Tahir", 44, "AI and Data Science", True]

strings = [x for x in data if isinstance(x, str)]
numbers = [x for x in data if isinstance(x, int) or isinstance(x, float)]
booleans = [x for x in data if isinstance(x, bool)]

print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)
