import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model & scaler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'house_price_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'model', 'scaler.pkl')

model = None
scaler = None

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>House Price Prediction API - IBM SkillsBuild Internship</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f8f9fa; color: #333; }
            .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); max-width: 700px; margin: 0 auto; }
            h1 { color: #0066cc; margin-top: 0; }
            .badge { display: inline-block; padding: 4px 12px; background: #e3f2fd; color: #0d47a1; border-radius: 20px; font-weight: bold; font-size: 0.9em; }
            ul { line-height: 1.8; }
            code { background: #f1f3f5; padding: 2px 6px; border-radius: 4px; font-weight: bold; color: #d63384; }
            .btn { display: inline-block; padding: 10px 20px; background: #0066cc; color: white; text-decoration: none; border-radius: 6px; margin-top: 15px; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">API Active</span>
            <h1>🏠 House Price Valuation REST API</h1>
            <p><strong>IBM SkillsBuild Academic Internship Project</strong> | BharatCares & AICTE</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            <h3>Available Endpoints:</h3>
            <ul>
                <li><code>GET /health</code> &mdash; Check API & Model Status (<a href="/health">Test /health</a>)</li>
                <li><code>POST /predict</code> &mdash; JSON Property Valuation Prediction API</li>
            </ul>
            <h3>Frontend Dashboard:</h3>
            <p>To view the Executive Interactive BI Dashboard, run <code>streamlit run frontend/app_streamlit.py</code> in a new terminal tab.</p>
        </div>
    </body>
    </html>
    """

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'online', 'model_loaded': model is not None})


@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not trained or missing'}), 500
    
    try:
        data = request.get_json()
        area = float(data.get('area', 1500))
        rooms = int(data.get('rooms', 3))
        bedrooms = int(data.get('bedrooms', 2))
        bathrooms = int(data.get('bathrooms', 2))
        location_score = float(data.get('location_score', 7.5))
        age_years = int(data.get('age_years', 10))

        input_features = np.array([[area, rooms, bedrooms, bathrooms, location_score, age_years]])
        input_scaled = scaler.transform(input_features)

        predicted_price = model.predict(input_scaled)[0]
        
        # Decision BI Framework metrics
        confidence_margin = predicted_price * 0.05
        price_lower = round(predicted_price - confidence_margin, -2)
        price_upper = round(predicted_price + confidence_margin, -2)

        return jsonify({
            'predicted_price': round(predicted_price, 2),
            'price_range': {
                'min': price_lower,
                'max': price_upper
            },
            'input_summary': {
                'area': area,
                'rooms': rooms,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'location_score': location_score,
                'age_years': age_years
            },
            'decision_insight': {
                'category': 'Opportunity' if location_score >= 8.0 else ('Risk' if age_years > 20 else 'Standard'),
                'recommendation': 'High appreciation potential' if location_score >= 8.0 else 'Renovation budget recommended'
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
