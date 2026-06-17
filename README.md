# 🚢 Titanic Survival Prediction

An end-to-end machine learning project that predicts whether a Titanic passenger would have survived — from raw data and EDA all the way to a deployed REST API and interactive web app.

🔗 **Live Demo:** https://titanic-analysis-fvvyusvhibvlsjhfthm7dc.streamlit.app  
📡 **API Docs:** https://titanic-api-2tpg.onrender.com/docs
🌐 **Titanic Lab:** https://ameydande.github.io/Titanic-analysis/

---

## What This Project Does

1. **Explores the data** — univariate, bivariate, and multivariate analysis with visualizations
2. **Engineers features** — `family_size`, `lone_traveler`, `fare_per_person` extracted from raw columns
3. **Imputes missing Age values** — using a Ridge Regression model trained on passengers with known ages, instead of a simple median fill
4. **Predicts survival** — two classifiers (Logistic Regression and Random Forest) built inside sklearn Pipelines, tuned with GridSearchCV
5. **Serves predictions via API** — FastAPI app deployed on Render
6. **Interactive UI** — Streamlit frontend where anyone can fill in passenger details and get a prediction

---

## Results

### Age Imputation (Stage 1)
| Model | MAE | RMSE | R² |
|---|---|---|---|
| Ridge Regression | 9.08 | 11.60 | 0.190 |
| SGD Regressor | 9.09 | 11.61 | 0.189 |

Ridge selected as best model (alpha = 10.0).

**Why Age prediction has low R² (0.19):**  
Age is genuinely hard to predict from the available features. The dataset only gives us 
Pclass, Sex, Fare, family size, and embarkation port — none of which have a strong linear 
relationship with age. A person's age is largely independent of how much they paid or 
where they boarded. The low R² reflects this — not a modelling mistake, but a data 
limitation. Despite this, ML-based imputation still captures rough patterns (e.g. 1st 
class passengers skewing older) and is more informative than filling every missing value 
with the same median.

### Survival Classification (Stage 2)
| Model | Accuracy | AUC |
|---|---|---|
| Logistic Regression | 79.3% | 0.843 |
| **Random Forest** | **81.0%** | **0.861** |

Best Random Forest hyperparameters (via GridSearchCV):
- `n_estimators`: 200
- `max_depth`: 5  
- `max_features`: sqrt
- `min_samples_split`: 2

Random Forest classification report:
```
              precision    recall  f1-score

Died (0)          0.80      0.90      0.85
Survived (1)      0.82      0.69      0.75

accuracy                              0.81
```

---

## Project Structure

```
Titanic-analysis/
├── app.py                          # FastAPI prediction API
├── streamlit_app.py                # Streamlit frontend
├── titanic_model.pkl               # Saved trained pipeline
├── requirements.txt                # Dependencies
├── README.md
└── notebook/
    ├── titanic-assessment+EDA.ipynb    # EDA and feature engineering
    └── titanic-ML-work.ipynb           # Model training and evaluation
```

---

## How It Works

```
User fills form
      ↓
Streamlit frontend
      ↓
POST /predict → FastAPI on Render
      ↓
sklearn Pipeline (imputer → scaler → Random Forest)
      ↓
{"survived": 0} or {"survived": 1}
      ↓
Result displayed in UI
```

---

## Run Locally

```bash
git clone https://github.com/AmeyDande/Titanic-analysis.git
cd Titanic-analysis
pip install -r requirements.txt
```

**Run the API:**
```bash
uvicorn app:app --reload
# visit http://127.0.0.1:8000/docs
```

**Run the UI:**
```bash
streamlit run streamlit_app.py
# visit http://localhost:8501
```

**Data:** Download `train.csv` from [Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic/data), then run the EDA notebook first to generate `titanic_eda.csv`.

---

## API Usage

**POST** `/predict`

```json
{
  "Pclass": 1,
  "Sex": 1,
  "Age": 29.0,
  "SibSp": 0,
  "Parch": 0,
  "total_fare": 211.0,
  "lone_traveler": 1,
  "family_size": 1,
  "fare_per_person": 211.0,
  "Embarked_S": 0,
  "Embarked_C": 1,
  "Embarked_Q": 0
}
```

Response:
```json
{ "survived": 1 }
```

`Sex`: 0 = male, 1 = female

---
Also added Interactive titanic lab which includes EDA, Classification matrix, PLots, Live app and API Docs URL  
 
## Tech Stack

Python · scikit-learn · pandas · NumPy · FastAPI · Streamlit · joblib · Seaborn · Matplotlib · Render · Streamlit Cloud
