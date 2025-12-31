import pandas as pd

# 1. Đọc file CSV vào DataFrame
df = pd.read_csv('metadata.csv')

# 2. Trộn ngẫu nhiên các dòng
# frac=1: Lấy ra 100% số dòng (trộn toàn bộ)
# random_state: Số cố định (ví dụ 99) để kết quả trộn giống nhau mỗi lần chạy (tùy chọn)
df_shuffled = df.sample(frac=1, random_state=99).reset_index(drop=True)

# 3. Lưu lại thành file mới
df_shuffled.to_csv('metadata.csv', index=False)

print("Đã trộn xong và lưu vào file 'metadata.csv'")