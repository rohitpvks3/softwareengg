def calculate_temperature(time, a, b, c):
    temperature = a * (time ** 2) + (b * time) + c
    return temperature

# Read coefficients from a file
with open("coffiecient.txt", "r") as file:
    line = file.readline().split()
    a, b, c = map(float, line)

time = float(input("Enter time: "))
temp = calculate_temperature(time, a, b, c)
print(f"Temperature at {time} is {temp} degrees Celsius.")