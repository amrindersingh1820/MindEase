import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Step 1: Generate dummy mood data
def generate_data(samples=1000):
    np.random.seed(42)
    data = {
        "sleep_hours": np.random.uniform(4, 10, samples),
        "screen_time": np.random.uniform(1, 10, samples),
        "physical_activity": np.random.uniform(0, 90, samples),
        "journal_freq": np.random.randint(0, 5, samples),
        "previous_mood": np.random.uniform(1, 10, samples),
    }
    df = pd.DataFrame(data)
    df["mood_score"] = (
        0.3 * df["sleep_hours"] -
        0.2 * df["screen_time"] +
        0.2 * df["physical_activity"] / 10 +
        0.1 * df["journal_freq"] +
        0.2 * df["previous_mood"]
    ) + np.random.normal(0, 1, samples)
    df["mood_score"] = df["mood_score"].clip(0, 10)
    return df

# Step 2: Prepare the dataset
df = generate_data()

X = df.drop("mood_score", axis=1)
y = df["mood_score"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Step 3: Build the model
model = Sequential([
    Input(shape=(X.shape[1],)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1)  # Regression output
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Step 4: Train the model
model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# Step 5: Save the model and scaler
os.makedirs("../model", exist_ok=True)
model.save("../model/mood_predictor.keras")  # Save the model in Keras format
joblib.dump(scaler, "../model/scaler.pkl")