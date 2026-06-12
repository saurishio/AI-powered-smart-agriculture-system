import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset

df = pd.read_csv("data/fertilizer.csv")

# Encode crop names
encoder = LabelEncoder()
df["crop"] = encoder.fit_transform(df["crop"])

# Features
X = df[["N", "P", "K", "crop"]]

# Target
y = df["fertilizer"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("fertilizer_model.pkl", "wb"))

print("Fertilizer model trained")