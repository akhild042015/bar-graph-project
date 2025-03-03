import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate random data
num_points = 20  # Number of data points
x = np.arange(num_points)  # x-values (0 to num_points - 1)
y = np.random.randint(0, 100, num_points)  # Random y-values (0 to 99)

# Create a Pandas DataFrame (recommended for Seaborn)
data = pd.DataFrame({'x': x, 'y': y})

# Create the line graph using Seaborn's basic line plot
sns.lineplot(x='x', y='y', data=data)

# Add title and labels
plt.title("Random Line Graph with Random Values Created with Seaborn And Pandas")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the graph
plt.show()

#Example with multiple random lines.

num_lines = 3
for i in range(num_lines):
    y = np.random.randint(0,100, num_points)
    data = pd.DataFrame({'x':x, 'y':y})
    sns.lineplot(x='x', y='y', data=data, label = f"Line {i+1}") #creates multiple lines, and labels them.

plt.title("Multiple Random Line Graph with Random Values Created with Seaborn And Pandas")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()