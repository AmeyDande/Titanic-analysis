import streamlit as st
import requests

st.title('🚢 Titanic Survival Predictor')
st.write('Fill in the passenger details to predict survival.')

pclass = st.selectbox('Passenger Class', [1, 2, 3])
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.slider('Age', 1, 80, 25)
sibsp = st.number_input('Siblings/Spouses on board', 0, 8, 0)
parch = st.number_input('Parents/Children on board', 0, 6, 0)
total_fare = st.number_input('Total Fare', 0.0, 500.0, 32.0)
embarked = st.selectbox('Embarked', ['S', 'C', 'Q'])
family_size = sibsp + parch + 1
lone_traveler = 1 if family_size == 1 else 0
fare_per_person = total_fare / family_size

if st.button('Predict'):
    payload = {
        "Pclass": pclass,
        "Sex": 0 if sex == 'Male' else 1,
        "Age": float(age),
        "SibSp": int(sibsp),
        "Parch": int(parch),
        "total_fare": float(total_fare),
        "lone_traveler": lone_traveler,
        "family_size": family_size,
        "fare_per_person": fare_per_person,
        "Embarked_S": 1 if embarked == 'S' else 0,
        "Embarked_C": 1 if embarked == 'C' else 0,
        "Embarked_Q": 1 if embarked == 'Q' else 0
    }

    try:
        response = requests.post(
            'https://titanic-api-2tpg.onrender.com/predict',
            json=payload,
            timeout=15
        )
        response.raise_for_status()
        result = response.json()

        if result['survived'] == 1:
            st.success('✅ This passenger would have SURVIVED')
        else:
            st.error('❌ This passenger would NOT have survived')
    except requests.exceptions.Timeout:
        st.warning('⏳ The API is waking up (free tier cold start). Wait 10 seconds and try again.')
    except requests.exceptions.ConnectionError:
        st.error('🔌 Could not reach the API. Check your internet or Render deployment status.')
    except Exception as e:
        st.error(f'Something went wrong: {e}')       