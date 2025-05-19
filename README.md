# ĐỀ TÀI: DỰ ĐOÁN LƯỢNG TIÊU THỤ ĐIỆN NĂNG BẰNG MACHINE LEARNING

> **NHÓM:** NHÓM TESTTEST

> **THÀNH VIÊN:**

- NGUYỄN ANH QUÂN - MSSV: 3123410294
- ĐỖ XUÂN QUÝ DƯƠNG - MSSV: 3120410101
- ĐẶNG NGỌC ĐOAN TRANG - MSSV: 3121410515
- ĐINH ĐÀO THÁI SƠN - MSSV: 3123410306

> **TRƯỜNG:** ĐẠI HỌC SÀI GÒN

## GIỚI THIỆU NGHIÊN CỨU

Dự án này nhằm xây dựng mô hình Machine Learning để dự đoán lượng điện năng tiêu thụ dựa trên các yếu tố như thời tiết, thời gian trong ngày, v.v. Đồng thời, chúng tôi cũng phát triển API để cung cấp dự đoán này dưới dạng dịch vụ.

## MỤC TIÊU NGHIÊN CỨU

- Phân tích các yếu tố ảnh hưởng đến tiêu thụ điện năng như nhiệt độ, độ ẩm, thời gian, ngày trong tuần,...
- Xây dựng và huấn luyện các mô hình Machine Learning nhằm dự đoán chính xác lượng điện năng tiêu thụ.
- So sánh hiệu suất giữa các mô hình như Linear Regression, Random Forest và XGBoost.
- Tích hợp mô hình tốt nhất vào một API RESTful để triển khai như một dịch vụ.

---

## PHƯƠNG PHÁP NGHIÊN CỨU

- **Thu thập dữ liệu**: Sử dụng dữ liệu tiêu thụ điện năng thực tế kết hợp với dữ liệu thời tiết.
- **Tiền xử lý dữ liệu**: Làm sạch, xử lý giá trị thiếu, chuẩn hóa dữ liệu và tạo các đặc trưng mới (feature engineering).
- **Huấn luyện mô hình**: Áp dụng các mô hình như Linear Regression, Random Forest và XGBoost để huấn luyện và đánh giá.
- **Đánh giá mô hình**: Sử dụng các chỉ số như RMSE, MAPE, MAE và R² để so sánh hiệu suất giữa các mô hình.
- **Triển khai mô hình**: Mô hình được đóng gói và cung cấp thông qua một API có thể gọi từ ứng dụng khác.

## KẾT QUẢ ĐẠT ĐƯỢC

- Đã hoàn thành tiền xử lý và phân tích dữ liệu (EDA).
- Huấn luyện và đánh giá 3 mô hình:
  - **Linear Regression**: Dễ triển khai, kết quả cơ bản.
  - **Random Forest**: Kết quả ổn định hơn.
  - **XGBoost**: Hiệu suất cao nhất, RMSE thấp nhất, R² cao nhất.
- Tích hợp mô hình Random Forest vào một API RESTful.
- Giao diện API hoạt động ổn định, cho phép dự đoán theo đầu vào người dùng cung cấp.

## CÂÚ TRÚC SRC CODECODE

.
├── README.md
├── api
│   └── app.py
├── data
│   ├── continuous_dataset.csv
│   └── dataset
│   ├── cleaning_dataset.csv
│   └── continuous dataset.csv
├── docs
│   ├── BT6_PhanTichLuanVan_N3.docx
│   ├── De_Cuong_NCKH.docx
│   ├── NhomTest_ProjectProposal.docx
│   ├── Surveydataset.md
│   └── project_status.txt
├── img
├── logs
│   ├── 12_04_2025_experiment_log.md
│   └── 21_04_2025_experiment.log.md
├── models
│   ├── model_random_forest.pkl
│   └── model_rf_metadata.json
├── notebook
│   ├── cleaning_data.ipynb
│   ├── eda.ipynb
│   └── testing_data.ipynb
├── project_related_papers
│   ├── README.md
│   ├── files
│   │   ├── 62
│   │   │   └── Project related works.pdf
│   │   ├── 63
│   │   │   └── 2021_Index_IEEE_Transactions_on_Power_Systems_Vol.\_36.pdf
│   │   ├── 64
│   │   │   └── energies-15-03566.pdf
│   │   └── 65
│   │   └── Short-Term_Electricity_Load_Forecasting_with_Machi.pdf
│   └── project_related_papers.rdf
├── requirements.txt
├── train
│   ├── train_LR.py
│   ├── train_RF.py
│   └── train_xgboot.py

## HƯỚNG DẪN CHẠY

### 1. Cài đặt thư viện

Trước tiên, đảm bảo rằng bạn đang sử dụng Python 3.7 trở lên.

Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt

# Huấn luyện Linear Regression
python train/train_LR.py

# Huấn luyện Random Forest
python train/train_RF.py

# Huấn luyện XGBoost
python train/train_xgboot.py
```
