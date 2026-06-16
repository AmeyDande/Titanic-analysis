import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load('titanic_model.pkl')

class Passenger(BaseModel):
    Pclass: int
    Sex: int            # 0 = male, 1 = female
    Age: float
    SibSp: int
    Parch: int
    total_fare: float
    lone_traveler: int
    family_size: int
    fare_per_person: float
    Embarked_S: int
    Embarked_C: int
    Embarked_Q: int

@app.get('/')
def root():
    return {'status': 'Titanic model is live'}

@app.post('/predict')
def predict(passenger: Passenger):
    data = np.array([[
        passenger.Pclass, passenger.Sex, passenger.Age,
        passenger.SibSp, passenger.Parch, passenger.total_fare,
        passenger.lone_traveler, passenger.family_size, passenger.fare_per_person,
        passenger.Embarked_S, passenger.Embarked_C, passenger.Embarked_Q
    ]])
    prediction = model.predict(data)[0]
    return {'survived': int(prediction)}