import streamlit as st
import pandas as pd

st.set_page_config(page_title="HI780 Final Project", layout="wide")

st.title("📊 Youth E-Cigarette Prediction Analysis")
st.subheader("George Mason University - HI780 Data Mining in Healthcare")

# Display Project Info
st.info("This application is deployed on Azure App Service using Continuous Integration from GitHub.")

# Load and Display Data
try:
    df = pd.read_csv("nyts2022_ecig_ml_complete.csv")
    st.success("✅ Dataset loaded successfully from Azure storage.")
    
    st.write("### Data Preview")
    st.dataframe(df.head(10))
    
    st.write("### Project Goals")
    st.write("- Predict 'Ever Use' of electronic cigarettes among youth.")
    st.write("- Analyze key predictors using Logistic Regression, Decision Trees, and Random Forest.")
    
except Exception as e:
    st.error(f"Error loading data: {e}")
