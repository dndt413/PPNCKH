import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import json

# 1. Đọc dữ liệu
PATH = "/home/black_hawk/workspace/PPNCKH/data/dataset/cleaning_dataset.csv"
try:
    df = pd.read_csv(PATH)
except FileNotFoundError:
    print(f"File {PATH} không tồn tại!")
    exit()


# 3. Tách X và y, thêm đặc trưng từ datetime (vì đây có thể là bài toán chuỗi thời gian)
X = df.drop(["nat_demand", "datetime"], axis=1)
y = df["nat_demand"]
# 4. Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Tạo và huấn luyện mô hình Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Đánh giá chéo
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("Độ chính xác trung bình CV (RMSE):", np.sqrt(-cv_scores.mean()))

# 7. Dự đoán và đánh giá
y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

mae = mean_absolute_error(y_test, y_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
r2 = r2_score(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
train_rmse = np.sqrt(np.mean((y_train - y_train_pred) ** 2))

print("MAE trên tập test:", mae)
print("MAE trên tập train:", train_mae)
print("R2 Score:", r2)
print("MAPE: ", mape)
print("RMSE trên tập test:", rmse)
print("RMSE trên tập train:", train_rmse)
print("Độ chính xác của mô hình:", model.score(X_test, y_test))

# 8. Lưu mô hình và metadata
joblib.dump(model, "./models/model_linear_regression.pkl")

metadata = {
    "date_trained": pd.Timestamp.now().isoformat(),
    "model_type": "LinearRegression",
    "mae_test": mae,
    "mae_train": train_mae,
    "r2": r2,
    "mape": mape,
    "rmse_test": rmse,
    "rmse_train": train_rmse
}
with open("./models/model_lr_metadata.json", "w") as f:
    json.dump(metadata, f)
print("Đã lưu metadata thành công!")