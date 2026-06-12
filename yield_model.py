import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset

df = pd.read_csv("data/yield.csv")

# Features
X = df[[
    "Rainfall",
    "Temperature",
    "Humidity"
]]

# Target
y = df["Yield"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("yield_model.pkl", "wb"))

print("Yield model trained")