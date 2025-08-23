temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif 0 <= temp < 26:
    print("Moderate")
else:
    print("Hot")