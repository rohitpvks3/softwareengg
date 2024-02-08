import matplotlib.pyplot as plt
import numpy as np

# Requirement 1: Data Collection
# For simplicity, generate random data
np.random.seed(42)
data = np.random.randint(1, 100, 5)  # 5 random data pointsmn 
# Requirement 2: Data Analysis
# Analyze data using basic statistics
mean_value = np.mean(data)
std_dev = np.std(data)

# Requirement 3: Data Visualization
# Visualize the analyzed data using line graphs
labels = ['Data Point 1', 'Data Point 2', 'Data Point 3', 'Data Point 4', 'Data Point 5']

fig, ax = plt.subplots()

# Plotting the data points
ax.plot(labels, data, marker='o', linestyle='-', color='blue', label='Random Data')

# Plotting mean and standard deviation lines
ax.axhline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean Value')
ax.axhline(mean_value + std_dev, color='green', linestyle='dashed', linewidth=2, label='Mean + Std Dev')
ax.axhline(mean_value - std_dev, color='green', linestyle='dashed', linewidth=2, label='Mean - Std Dev')

# Adding labels and title
ax.set_xlabel('Data Points')
ax.set_ylabel('Values')
ax.set_title('Data Analysis and Visualization')

# Adding legend
ax.legend()

# Show the plot
plt.show()