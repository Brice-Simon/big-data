import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the path if needed)
df = pd.read_csv("uber.csv")

# Select two columns: passenger_count and fare_amount
x = df['passenger_count']
y = df['fare_amount']

# Create a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, alpha=0.5, color='blue')
plt.title('Fare Amount vs. Passenger Count')
plt.xlabel('Passenger Count')
plt.ylabel('Fare Amount ($)')
plt.grid(True)
plt.show()
