import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# 1. Đọc dữ liệu
PATH = "/home/black_hawk/workspace/PPNCKH/data/dataset/cleaning_dataset.csv"
df = pd.read_csv(PATH)

# 2. Tách X và y
X = df.drop(["nat_demand", "datetime"], axis=1)
y = df["nat_demand"]

# 3. Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Tạo mô hình XGBoost
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=6)

# 5. Huấn luyện mô hình
model.fit(X_train, y_train)

# 6. Dự đoán và đánh giá
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2 Score:", r2)

# 7. Lưu mô hình
joblib.dump(model, "model_xgb.pkl")
print("✅ Đã lưu mô hình thành công vào file model.pkl")
