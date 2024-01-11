import matplotlib.pyplot as plt

class IterativeModel:
    @staticmethod
    def calculate_temperature(time, a, b, c):
        temperature = a * (time ** 2) + (b * time) + c
        return temperature

    def execute_iteration(self):
        while True:
            a = float(input("Enter coefficient related to rate of change (a): "))
            b = float(input("Enter coefficient for linear change (b): "))
            c = float(input("Enter base temperature (c): "))
            time = float(input("Enter time: "))

            confirmed = input(f"Entered values are: a={a}, b={b}, c={c}, time={time}. Are you satisfied? (yes/no): ").lower()
            if confirmed != 'yes':
                continue

            output = self.calculate_temperature(time, a, b, c)
            print(f"Calculated temperature: {output}")

            satisfied_output = input(f"Is the calculated temperature satisfactory? (yes/no): ").lower()
            if satisfied_output != 'yes':
                continue

            parameter_values = {'a': [], 'b': []}
            temperature_values = []

            for parameter in ['a', 'b']:
                original_value = locals()[parameter]
                values_to_test = [original_value + 0.2 * i for i in range(-5, 6)]  # Adjusted for 10 values

                for value in values_to_test:
                    if parameter == 'a':
                        new_output = self.calculate_temperature(time, value, b, c)
                    elif parameter == 'b':
                        new_output = self.calculate_temperature(time, a, value, c)
                    
                    parameter_values[parameter].append(value)
                    temperature_values.append(new_output)

            # Plotting
            plt.figure(figsize=(10, 6))
            for parameter in ['a', 'b']:
                start_idx = 10 * ['a', 'b'].index(parameter)
                end_idx = start_idx + 11  # Adjusted for 11 values (0 to 10)
                plt.plot(parameter_values[parameter], temperature_values[start_idx:end_idx], label=f'{parameter} values')

            # Plotting the constant 'c' value
            const_c_values = [self.calculate_temperature(time, a, b, c) for _ in range(11)]
            plt.plot(parameter_values['a'], const_c_values, label="Constant c (Base Temperature)", linestyle='--', color='black')

            plt.title('Temperature vs. Parameter Values')
            plt.xlabel('Parameter Values')
            plt.ylabel('Temperature')
            plt.legend()
            plt.grid(True)
            plt.show()

            break

# Create an instance and execute the iteration
model_instance = IterativeModel()
model_instance.execute_iteration()