age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Senior Citizen")