import pickle
import numpy as np
import streamlit as st

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title("LOAN APPROVAL CHECKER")
st.write("Developed and Deployed by Farhan Ali Khan")

genders = ("Male", "Female")
marriedStat = ("Yes", "No")
dependentsNo = ("0","1", "2", "3+")
educationStat = ("Graduate", "Not Graduate")
self_employedStat = ("Yes", "No")
prop_areatype = ("Rural", "Semiurban", "Urban")
credHist = ("1.0","0.0")

gender = st.selectbox("Gender",genders)
married = st.selectbox("Married",marriedStat)
dependents = st.selectbox("No. of dependents",dependentsNo)
education = st.selectbox("Education",educationStat)
employment = st.selectbox("Self employed",self_employedStat)
applicant_income = st.number_input("Applicant Income")
Co_applicant_income = st.number_input("Co-Applicant Income")
loan_amount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term")
creditHistory = st.selectbox("Credit history",credHist)
propertyArea = st.selectbox("Area", prop_areatype)

Done = st.button("Check Approval")

if Done:
    if gender == "Male":
        gender = 1
    else:
        gender = 0
    
    if married == "Yes":
        married = 1
    else:
        married = 0
    
    if dependents == "3+":
        dependents = 4
    else:
        dependents = int(dependents)
    
    if education == "Graduate":
        education = 1
    else:
        education = 0
    
    if employment == "Yes":
        employment = 1
    else:
        employment = 0
    
    if creditHistory == "1.0":
        creditHistory = 1.0
    else:
        creditHistory = 0.0

    if propertyArea == "Rural":
        propertyArea = 0
    elif propertyArea == "Semiurban":
        propertyArea = 1
    elif propertyArea == "Urban":
        propertyArea = 2

    input = (gender, married, dependents, education, employment, applicant_income, Co_applicant_income, loan_amount, loan_amount_term, creditHistory, propertyArea)
    model_data = np.asarray(input)
    model_data = model_data.reshape(1,-1)
    pred = loaded_model.predict(model_data)
    if pred[0] == 1:
        st.subheader("Loan is approved")
    else:
        st.subheader("Loan is not approved")
