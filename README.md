# 🏠 House Price Prediction & Real Estate Valuation Analytics

**Author:** Shailesh Mohan Shukla  
**Program:** IBM SkillsBuild Academic Internship Program (in association with BharatCares & AICTE)  
**Domain:** Data Analytics, Machine Learning & Business Intelligence  

---

## 📌 Project Overview
This project delivers a comprehensive machine learning and Business Intelligence valuation platform for residential real estate. Built using Python, Scikit-Learn, Flask, and Streamlit, the system provides accurate property valuation predictions ($R^2 = 0.9459$) alongside executive-level market dashboards.

---

## 📁 Required Submission Artifacts

| Mandatory File | Filename in Repository | Author | Description |
| :--- | :--- | :--- | :--- |
| **1️⃣ Code File** | [`Shailesh_HousePricePrediction.ipynb`](file:///C:/Users/dharm/.gemini/antigravity-ide/scratch/house_price_prediction_project/Shailesh_HousePricePrediction.ipynb) | Shailesh Mohan Shukla | Complete Jupyter Notebook with EDA, correlation matrices, ML algorithms, and evaluation |
| **2️⃣ Requirements File** | [`requirements.txt`](file:///C:/Users/dharm/.gemini/antigravity-ide/scratch/house_price_prediction_project/requirements.txt) | Shailesh Mohan Shukla | Project Python dependencies (`pandas`, `scikit-learn`, `flask`, `streamlit`, `python-docx`) |
| **3️⃣ Project Report** | [`Shailesh_ProjectReport.docx`](file:///C:/Users/dharm/.gemini/antigravity-ide/scratch/house_price_prediction_project/Shailesh_ProjectReport.docx) | Shailesh Mohan Shukla | Formal academic project documentation report formatted in MS Word |
| **4️⃣ README File** | [`README.md`](file:///C:/Users/dharm/.gemini/antigravity-ide/scratch/house_price_prediction_project/README.md) | Shailesh Mohan Shukla | Technical setup documentation and system architecture guide |

---

## 🏗️ Repository Architecture

```
house_price_prediction_project/
├── data/
│   └── house_price.csv                 # Housing dataset (300 property samples)
├── backend/
│   └── app.py                          # Flask REST API backend (/health, /predict, /)
├── frontend/
│   └── app_streamlit.py                # Streamlit Interactive Executive Dashboard
├── model/
│   ├── house_price_model.pkl           # Saved Random Forest Regressor artifact
│   └── scaler.pkl                      # Feature scaler artifact
├── train_model.py                      # Multi-model training and evaluation script
├── generate_report_docx.py             # Script generating Shailesh_ProjectReport.docx
├── Shailesh_HousePricePrediction.ipynb # Academic Jupyter Notebook submission
├── Shailesh_ProjectReport.docx          # Academic Word Document report submission
├── requirements.txt                    # Project environment dependencies
└── README.md                           # Documentation README
```

---

## ⚙️ Installation & Running Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Dataset & Model Training Script
```bash
python generate_dataset.py
python train_model.py
python generate_report_docx.py
```

### 3. Launch Flask REST API Server
```bash
python backend/app.py
```
* API Server will start on `http://127.0.0.1:5000`

### 4. Launch Streamlit Executive Dashboard
```bash
streamlit run frontend/app_streamlit.py
```
* Interactive UI will launch on `http://localhost:8501`

---

## 🏆 Model Performance Summary
* **Algorithm:** Random Forest Regressor (100 Trees)
* **$R^2$ Score:** `0.9459` (94.59% Variance Explained)
* **Mean Absolute Error (MAE):** `$28,153.40`
* **Root Mean Squared Error (RMSE):** `$34,862.57`
