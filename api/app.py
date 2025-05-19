from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

# Khởi tạo FastAPI app
app = FastAPI()

# Tải mô hình Random Forest
model_path = "../models/model_xgb.pkl"
if not os.path.exists(model_path):
    raise HTTPException(status_code=500, detail="Mô hình không tồn tại!")
model = joblib.load(model_path)

# Định nghĩa schema đầu vào
class PredictionInput(BaseModel):
    hour: float
    day_of_week: float
    Holiday_ID: float
    T2M_dav: float
    T2M_san: float
    T2M_toc: float
    T2M_max: float
    T2M_min: float
    T2M_range: float
    T2M_mav: float
    QV2M_dav: float
    QV2M_san: float
    QV2M_toc: float
    WS10M: float
    PS: float
    TQL_toc: float
    W2M_toc: float
    TQL_san: float
    W2M_san: float
    TQL_dav: float
    W2M_dav: float
    holiday: float
    school: float
    day: float
    month: float
    is_weekend: float


# Endpoint dự đoán
@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Tạo DataFrame từ input
        input_df = pd.DataFrame([input_data.dict()])

        # Kiểm tra thứ tự cột
        expected_features = list(model.feature_names_in_)
        input_df = input_df[expected_features]

        # Dự đoán
        prediction = model.predict(input_df)[0]

        return {"prediction": float(prediction)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lỗi dự đoán: {str(e)}")

# Kiểm tra API
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
