
# Streamlit Crop Recommendation demo
import streamlit as st
import joblib, numpy as np, pandas as pd
st.title("Crop Recommendation App")

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # current folder
bundle_path = os.path.join(BASE_DIR, "best_model_RandomForest.pkl")
bundle = joblib.load(bundle_path)


model = bundle['model']
le = bundle['label_encoder']
preprocessor = bundle['preprocessor']
features = bundle['features']

st.sidebar.header("Input sensor values")
inputs = {}
for feat in features:
    inputs[feat] = st.sidebar.number_input(str(feat), value=0.0)

if st.button("Predict"):
    df = pd.DataFrame([inputs])
    try:
        X_proc = preprocessor.transform(df)
    except Exception as e:
        st.error("Preprocessor error: " + str(e))
    pred_idx = model.predict(X_proc)
    pred_label = le.inverse_transform(pred_idx)[0]
    st.success(f"Recommended crop: {pred_label}")
