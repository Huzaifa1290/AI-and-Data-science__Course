def age_category(age):
    if age < 18:
        return "Minor"
    elif 18 <= age < 60:
        return "Adult"
    else:
        return "Senior Citizen"

print(age_category(65))