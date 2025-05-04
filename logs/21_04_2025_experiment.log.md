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

- Độ chính xác trung bình CV (RMSE): 114.44723598631643
- MAE trên tập test: 91.64537470845401
- MAE trên tập train: 91.34617786516536
- R2 Score: 0.6442074008093925
- MAPE: 8.06267271504719
- RMSE trên tập test: 114.59554965962873
- RMSE trên tập train: 114.3674734042744
- Độ chính xác của mô hình: 0.6442074008093925

## 📌 Kế hoạch tiếp theo

- Chuyển sang thử Linear Regression
- So sánh biểu đồ dự đoán của các mô hình
