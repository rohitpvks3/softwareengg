def calculate_temperature(time, a, b, c):
    temperature = a * (time ** 2) + (b * time) + c
    return temperature

# Get coefficients from user input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

time = float(input("Enter time: "))
temp = calculate_temperature(time, a, b, c)
print(f"Temperature at {time} is {temp} degrees Celsius.")