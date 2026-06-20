import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("sales_data.csv")

print("Dataset:")
print(data)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Features and Target
X = data[['Year']]
y = data['Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("MAE:", mae)
print("R2 Score:", r2)

# Predict for 2025
future_year = pd.DataFrame({'Year': [2025]})
future_sales = model.predict(future_year)

print("\nPredicted Sales for 2025:")
print(future_sales[0])

# Predict next 5 years
future_years = pd.DataFrame({
    'Year': [2025, 2026, 2027, 2028, 2029]
})

future_predictions = model.predict(future_years)

print("\nFuture Predictions:")
for year, sales in zip(future_years['Year'], future_predictions):
    print(f"{year}: {sales:.2f}")

# Visualization
plt.figure(figsize=(8,5))

# Historical data
plt.plot(
    data['Year'],
    data['Sales'],
    marker='o',
    label='Historical Sales'
)

# Future predictions
plt.plot(
    future_years['Year'],
    future_predictions,
    marker='o',
    linestyle='--',
    label='Predicted Sales'
)

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Forecast Prediction")
plt.legend()

# Save graph
plt.savefig("output_graph.png")

plt.show()