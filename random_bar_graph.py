import seaborn as sns
import matplotlib.pyplot as plt
import random

# Generate random categories (labels)
categories = [f"Category {i}" for i in range(7)] #7 categories

#generate random values
values = [random.randint(10, 90) for _ in range(7)] #random integers between 10, 90

#create the bar graph using seaborn
sns.barplot(x=categories, y=values)

#Add labels and title
plt.xlabel("Categories")
plt.ylabel("Random Values")
plt.title("Random Bar Graph Created using Seaborn with Random Values")

#Rotate x-axis labels
plt.xticks(rotation=45, ha="right")
plt.tight_layout()#prevents labels from being cut off
plt.show()
