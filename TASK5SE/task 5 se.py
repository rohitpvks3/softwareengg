import matplotlib.pyplot as plt

class AgileTemperatureModel:
    @staticmethod
    def calculate_temperature(time, a, b, c):
        temperature = a * (time ** 2) + (b * time) + c
        return temperature

    def gather_user_input(self):
        a = float(input("Enter coefficient related to rate of change (a): "))
        b = float(input("Enter coefficient for linear change (b): "))
        c = float(input("Enter base temperature (c): "))
        time = float(input("Enter time: "))

        return a, b, c, time

    def get_confirmation(self, a, b, c, time):
        confirmed = input(f"Entered values are: a={a}, b={b}, c={c}, time={time}. Are you satisfied? (yes/no): ").lower()
        return confirmed == 'yes'

    def get_satisfaction(self, output):
        satisfied_output = input(f"Is the calculated temperature ({output}) satisfactory? (yes/no): ").lower()
        return satisfied_output == 'yes'

    def generate_parameter_values(self, original_value, parameter, time, b, c):
        values_to_test = [original_value + 0.2 * i for i in range(-5, 6)]  # Adjusted for 10 values

        parameter_values = []
        temperature_values = []

        for value in values_to_test:
            if parameter == 'a':
                new_output = self.calculate_temperature(time, value, b, c)
            elif parameter == 'b':
                new_output = self.calculate_temperature(time, value, b, c)

            parameter_values.append(value)
            temperature_values.append(new_output)

        return parameter_values, temperature_values

    def plot_results(self, parameter_values, temperature_values, const_c_values):
        plt.figure(figsize=(10, 6))
        for parameter in ['a', 'b']:
            start_idx = 10 * ['a', 'b'].index(parameter)
            end_idx = start_idx + 11  # Adjusted for 11 values (0 to 10)
            plt.plot(parameter_values[parameter], temperature_values[start_idx:end_idx], label=f'{parameter} values')

        plt.plot(parameter_values['a'], const_c_values, label="Constant c (Base Temperature)", linestyle='--', color='black')

        plt.title('Temperature vs. Parameter Values')
        plt.xlabel('Parameter Values')
        plt.ylabel('Temperature')
        plt.legend()
        plt.grid(True)
        plt.show()

    def execute_iteration(self):
        while True:
            a, b, c, time = self.gather_user_input()

            if not self.get_confirmation(a, b, c, time):
                continue

            output = self.calculate_temperature(time, a, b, c)
            print(f"Calculated temperature: {output}")

            if not self.get_satisfaction(output):
                continue

            parameter_values = {'a': [], 'b': []}
            temperature_values = []

            for parameter in ['a', 'b']:
                original_value = locals()[parameter]
                values, temps = self.generate_parameter_values(original_value, parameter, time, b, c)
                parameter_values[parameter] = values
                temperature_values.extend(temps)

            # Plotting
            const_c_values = [self.calculate_temperature(time, a, b, c) for _ in range(11)]
            self.plot_results(parameter_values, temperature_values, const_c_values)

            break

# Create an instance and execute the iteration
agile_model_instance = AgileTemperatureModel()
agile_model_instance.execute_iteration()