
# Flask API for Crop Recommendation
from flask import Flask, request, jsonify
import joblib, numpy as np, pandas as pd

app = Flask(__name__)
bundle = joblib.load("ml_artifacts\best_model_RandomForest.pkl")
model = bundle['model']
le = bundle['label_encoder']
preprocessor = bundle['preprocessor']
features = bundle['features']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # expects JSON with feature:value pairs
    df = pd.DataFrame([{f: data.get(f, 0) for f in features}])
    X_proc = preprocessor.transform(df)
    pred_idx = model.predict(X_proc)
    pred_label = le.inverse_transform(pred_idx)[0]
    return jsonify({'recommended_crop': pred_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
