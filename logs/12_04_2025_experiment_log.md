# Nhật ký thí nghiệm - 12/04/2025

## Mục tiêu

Thử mô hình XGBOOST để dự báo điện năng theo giờ.

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

## 🤖 Mô hình: XGBOOST

- MAE: 47.3769549831044
- R2 Score: 0.8925439585421593
- Độ chính xác của mô hình: 0.8925439585421593
- MAPE: 4.15566215517535
- RSME: 62.977398383445674

## 📌 Kế hoạch tiếp theo

- Chuyển sang thử Linear Regression
- So sánh biểu đồ dự đoán của các mô hình
