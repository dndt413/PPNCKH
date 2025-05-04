# Nhật ký thí nghiệm - 21/04/2025

## Mục tiêu

Thử mô hình Linear Regression để dự báo điện năng theo giờ.

## 📊 Dữ liệu sử dụng

- Dataset: [Electricity Load Forecasting](https://www.kaggle.com/datasets/saurabhshahane/electricity-load-forecasting) (Kaggle)

## ⚙️ Các bước thực hiện

- Xử lý dữ liệu cột datetime
- Tạo thêm các cột "day", "hour", "month", "day_of_week", "is_weekend"
- Xóa cột "datetime"
- Xóa cột "nat_demand"
- Chia tập datase thành 8/2

## PKG sử dụng

- XGBOOST, Scikit-learn, joblib, pandas

## 🤖 Mô hình: Linear Regression

- n_estimators = 100
- max_depth = 6
- MAE: 47.38
- R2: 0.89

## 📌 Kế hoạch tiếp theo

- Chuyển sang thử Linear Regression
- So sánh biểu đồ dự đoán của các mô hình
