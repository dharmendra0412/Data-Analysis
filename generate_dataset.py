import pandas as pd
import numpy as np

# Set seed for reproducible synthetic dataset
np.random.seed(42)
n_samples = 300

area = np.random.randint(800, 4800, size=n_samples)
rooms = np.random.choice([2, 3, 4, 5, 6], size=n_samples, p=[0.18, 0.32, 0.28, 0.16, 0.06])
bedrooms = np.maximum(1, rooms - np.random.choice([1, 2], size=n_samples, p=[0.65, 0.35]))
bathrooms = np.maximum(1, bedrooms - np.random.choice([0, 1], size=n_samples, p=[0.55, 0.45]))
location_score = np.random.uniform(5.0, 9.8, size=n_samples).round(1)
age_years = np.random.randint(1, 28, size=n_samples)

# Price baseline with domain logic (per sqft rate, room multiplier, location weight, age decay)
base_price = 45000
price = (
    base_price
    + (area * 145)
    + (rooms * 14000)
    + (bathrooms * 9500)
    + (location_score * 27000)
    - (age_years * 1800)
    + np.random.normal(0, 16000, size=n_samples)
)

price = np.round(price, -2).astype(int)

df = pd.DataFrame({
    'area': area,
    'rooms': rooms,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'location_score': location_score,
    'age_years': age_years,
    'price': price
})

df.to_csv('C:/Users/dharm/.gemini/antigravity-ide/scratch/house_price_prediction_project/data/house_price.csv', index=False)
print(f"Generated clean dataset with {len(df)} records in data/house_price.csv")
