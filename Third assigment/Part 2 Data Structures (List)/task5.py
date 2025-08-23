# Task 5: List filtering and sorting
numbers = [32, 54, 66, 11, 77, 10, 90]

# a) Remove items < 20
numbers = [x for x in numbers if x >= 20]
print("Filtered list:", numbers)

# b) Sort ascending and descending
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# c) Compute average
average = sum(numbers) / len(numbers)
print("Average:", average)
