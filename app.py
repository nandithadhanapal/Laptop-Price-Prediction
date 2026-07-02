import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Laptop Price Prediction", page_icon="💻")

st.title("💻 Laptop Price Prediction")
st.write("Enter the laptop specifications to predict its price.")

# User Inputs
company = st.selectbox(
    "Company",
    ["Apple", "HP", "Acer", "Asus", "Dell", "Lenovo", "MSI", "Toshiba", "Samsung", "Microsoft", "Huawei", "Xiaomi", "Vero", "Chuwi", "Mediacom", "Google", "Fujitsu", "LG"]
)

product = st.text_input("Product Name")

typename = st.selectbox(
    "Laptop Type",
    ["Notebook", "Gaming", "Ultrabook", "2 in 1 Convertible", "Workstation", "Netbook"]
)

inches = st.number_input("Screen Size (Inches)", min_value=10.0, max_value=20.0)

screen = st.text_input("Screen Resolution")

cpu = st.text_input("CPU")

ram = st.number_input("RAM (GB)", min_value=2, max_value=64)

memory = st.text_input("Memory")

gpu = st.text_input("GPU")

os = st.selectbox(
    "Operating System",
    ["Windows 10", "Windows 11", "Mac OS X", "macOS", "Linux", "No OS", "Chrome OS"]
)

weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0)

# Prediction
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Company": [company],
        "Product": [product],
        "TypeName": [typename],
        "Inches": [inches],
        "ScreenResolution": [screen],
        "Cpu": [cpu],
        "Ram": [ram],
        "Memory": [memory],
        "Gpu": [gpu],
        "OpSys": [os],
        "Weight": [weight]
    })

    prediction = model.predict(input_df)

    euro_to_inr = 100
    price_inr = prediction[0] * euro_to_inr

    st.success(f"💰 Estimated Laptop Price: ₹ {price_inr:,.0f}")