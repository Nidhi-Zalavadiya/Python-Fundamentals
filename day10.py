from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import numpy as np

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df["target"] = housing.target
print(df["target"])
print(df.shape)
print(df.info())
print(df.describe())

X = df[housing.feature_names]
y = df["target"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, y, test_size = 0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)
# Tells you which features matter most
coefficients = pd.Series(model.coef_, index=housing.feature_names)
print(coefficients.sort_values(ascending=False))

predictions = model.predict(X_test)

# Mean Absolute Error (MAE)
mae = mean_absolute_error(Y_test, predictions)
mse = mean_squared_error(Y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, predictions) 

print(f"MAE:  {mae:.2f}")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

# Plot 1 — Actual vs Predicted
plt.subplot(121)
plt.scatter(Y_test, predictions, alpha=0.3, color="steelblue")
plt.plot(
    [Y_test.min(), Y_test.max()],
    [Y_test.min(), Y_test.max()],
    "r--", linewidth=2, label="Perfect Prediction"
)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.legend()

# Plot 2 — Feature Importance
plt.subplot(122)
coefficients.sort_values().plot(kind="barh", color="coral")
plt.xlabel("Coefficient Value")
plt.title("Feature Importance (Coefficients)")

plt.tight_layout()
plt.savefig("images\day10_linear_regression.png")
plt.show()



# Questions to Answer in Your Code Comments

# What is the difference between Classification and Regression in one line?

'''
    classification returns category find best match for data
    regression return number (best straight line through data)
'''
# What does an R² of 0.6 mean in plain English?
'''
    0.6 of  R2 explain 60% variation in data
'''
# Which feature had the highest coefficient? What does that mean?
'''
    AveBedrms had highest cofficient
    it means AveBedrms matters the most in prediction
'''
# Looking at your Actual vs Predicted plot — are points close to the diagonal line or scattered?
'''
    Points are close to the diagonal line
'''
# Why can't we use accuracy_score for regression problems?
'''
    accuracy_score gives exact number of match
    in regression we find nearest number 
    so accuracy_score will fail if there is single point mismatch
    that's why we can not use accuracy_score in regression problems
'''