import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import json

# Đọc dữ liệu
PATH = "/home/black_hawk/workspace/PPNCKH/data/dataset/cleaning_dataset.csv"
try:
    df = pd.read_csv(PATH)
except FileNotFoundError:
    print(f"File {PATH} không tồn tại!")
    exit()

# Tách X và y
X = df.drop(["nat_demand", "datetime"], axis=1)
y = df["nat_demand"]

# Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình Random Forest
model = RandomForestRegressor(
    n_estimators=100,  
    max_depth=6,       
    random_state=42
)
model.fit(X_train, y_train)

# Đánh giá chéo
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("Độ chính xác trung bình CV (RMSE):", np.sqrt(-cv_scores.mean()))

# Dự đoán và đánh giá
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

# Lưu mô hình và metadata
joblib.dump(model, "./models/model_random_forest.pkl")
print("Đã lưu mô hình thành công vào file model_random_forest.pkl")

metadata = {
    "date_trained": pd.Timestamp.now().isoformat(),
    "model_type": "RandomForestRegressor",
    "params": {
        "n_estimators": 100,
        "max_depth": 6,
        "random_state": 42
    },
    "mae_test": mae,
    "mae_train": train_mae,
    "r2": r2,
    "mape": mape,
    "rmse_test": rmse,
    "rmse_train": train_rmse
}
with open("./models/model_rf_metadata.json", "w") as f:
    json.dump(metadata, f)
print("Đã lưu metadata thành công!")