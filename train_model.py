"""
House Price Prediction Model Training Script
Author: Shailesh Mohan Shukla
Description: Trains and compares Linear Regression, Decision Tree, and Random Forest Regressor models.
"""

import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_models():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'house_price.csv')
    model_dir = os.path.join(base_dir, 'model')
    os.makedirs(model_dir, exist_ok=True)

    print(f"Reading dataset: {data_path}")
    df = pd.read_csv(data_path)

    features = ['area', 'rooms', 'bedrooms', 'bathrooms', 'location_score', 'age_years']
    X = df[features]
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Evaluate multiple candidate models
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree Regressor': DecisionTreeRegressor(random_state=42, max_depth=8),
        'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42)
    }

    results = {}
    best_model = None
    best_r2 = -float('inf')
    best_name = ""

    print("\n" + "="*50)
    print("      MODEL PERFORMANCE COMPARISON TABLE      ")
    print("="*50)
    print(f"{'Algorithm':<26} | {'R² Score':<10} | {'MAE ($)':<12} | {'RMSE ($)':<12}")
    print("-" * 68)

    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        
        r2 = r2_score(y_test, preds)
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        results[name] = {'r2': r2, 'mae': mae, 'rmse': rmse}
        print(f"{name:<26} | {r2:<10.4f} | {mae:<12,.2f} | {rmse:<12,.2f}")

        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_name = name

    print("="*68)
    print(f"\nOptimal Selected Model: {best_name} (R² = {best_r2:.4f})")

    # Persist model and scaler
    joblib.dump(best_model, os.path.join(model_dir, 'house_price_model.pkl'))
    joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))
    print(f"Artifacts successfully saved to '{model_dir}' directory.")

if __name__ == '__main__':
    train_models()
