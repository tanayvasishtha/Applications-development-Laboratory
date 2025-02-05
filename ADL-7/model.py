import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

# Load and preprocess data
df = pd.read_csv('house_data.csv', encoding='latin1')

# Select only the required features
selected_features = ['sqft_living', 'bedrooms', 'bathrooms', 'yr_built']
X = df[selected_features]
y = df['price']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and scaler
with open('house_data.pkl', 'wb') as file:
    pickle.dump((model, scaler, selected_features), file)

# Print model performance
print(f"R2 Score: {model.score(X_test, y_test):.4f}")
