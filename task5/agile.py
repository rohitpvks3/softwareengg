import matplotlib.pyplot as plt

class WeatherModel:
    def __init__(self):
        self.locations = []

    def add_location(self, location, temperature):
        self.locations.append({'location': location, 'temperature': temperature})

    def get_current_weather(self, location):
        # Placeholder for weather information (replace with actual logic)
        return f"Current weather in {location['location']}: {location['temperature']}°C, sunny"

    def collect_user_input(self):
        while True:
            location = input("Enter a location (or 'done' to finish): ").strip()
            if location.lower() == 'done':
                break
            temperature = float(input(f"Enter the temperature for {location} (in °C): "))
            self.add_location(location, temperature)

    def visualize_weather_data(self):
        # Collecting weather data
        weather_data = {}
        for location in self.locations:
            current_weather = self.get_current_weather(location)
            weather_data[location['location']] = location['temperature']

        # Visualizing the data using matplotlib
        locations = list(weather_data.keys())
        temperatures = list(weather_data.values())

        plt.bar(locations, temperatures, color='blue')
        plt.xlabel('Locations')
        plt.ylabel('Temperature (°C)')
        plt.title('Current Weather Information')
        plt.show()

# Sample usage of the WeatherModel class
if __name__ == "__main__":
    weather_model = WeatherModel()

    # Sprint 1: User input and data collection
    weather_model.collect_user_input()

    # Sprint 2: Visualization
    weather_model.visualize_weather_data()
