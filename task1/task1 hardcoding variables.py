#implement weather modeling using the quzdratic solution in stages hard coding variables, keyboard input, read from a file, for a single set of input, multiple sets of input and save all versions debug, fix problems, create a github account.

def calculate_temperature(time, a, b, c):

    temperature = a * (time ** 2) + (b * time) + c
    return temperature

a = 0.5
b = 1.5
c = 20

time = 3
temp = calculate_temperature(time, a, b, c)
print(f"Temperature at {time} is {temp} degrees Celsius.")