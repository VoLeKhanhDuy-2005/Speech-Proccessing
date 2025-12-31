import pandas as pd

# 1. Đọc file CSV
df = pd.read_csv('metadata.csv')

# 2. Thiết lập ngưỡng thời gian tối thiểu (ví dụ: 0.5 giây)
min_threshold = 0.5

# 3. Lọc bỏ các dòng có (end - start) nhỏ hơn ngưỡng
# Ta giữ lại những dòng có hiệu số >= min_threshold
df_filtered = df[(df['end'] - df['start']) >= min_threshold].copy()

# 4. Lưu lại kết quả vào file mới
df_filtered.to_csv('metadata.csv', index=False)

# In thông báo kiểm tra
removed_count = len(df) - len(df_filtered)
print(f"Đã loại bỏ: {removed_count} dòng quá ngắn.")
print(f"Số dòng còn lại: {len(df_filtered)}")