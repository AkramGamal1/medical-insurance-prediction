import streamlit as st 
import pickle 
import numpy as np


rf = pickle.load(open("rf_model.pkl",'rb'))
one = pickle.load(open("one.pkl",'rb'))


def prediction_data(data, model):
  result = model.predict(data)
  return np.exp(result)[0]

st.title("Insurance Predictor")

age = st.number_input("Age",min_value=18,max_value=64)
bmi =st.number_input("BMI")
child  =st.number_input("children")

smoke = st.selectbox("Smoker", ('yes','no'))
sex = st.selectbox("sex", ('male','female'))
region = st.selectbox("region", ('southwest', 'southeast', 'northwest', 'northeast'))


temp = one.transform([[sex, smoke, region]]).toarray()

data = [age,bmi,child]
data.extend(temp[0])
res = prediction_data([data],rf)

if st.button('predict ') :
    st.text(res)
