def circle_properties(radius):
    pi = 3.1416  
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference


r = float(input("Enter radius: "))
a, c = circle_properties(r)
print("Area of circle:", a)
print("Circumference of circle:", c)