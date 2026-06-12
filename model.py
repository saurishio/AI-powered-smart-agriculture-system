import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset

df = pd.read_csv("crop_recommendation.csv")

# Features
X = df.drop("label", axis=1)

# Target
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

# Save model
pickle.dump(model, open("crop_model.pkl", "wb"))

# Save accuracy
with open("accuracy.txt", "w") as file:
    file.write(f"{accuracy * 100:.2f}")

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Model saved successfully")