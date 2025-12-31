import os
import pandas as pd
import librosa
import numpy as np

def endpoint_detection(file_path):
    # Nạp tín hiệu và thiết lập tham số
    y, sr = librosa.load(file_path, sr=None) 
    frame_length = int(0.025 * sr)
    hop_length = int(0.010 * sr)

    # Tính toán năng lượng ngắn hạn
    energy = []
    for i in range(0, len(y), hop_length):
        energy.append(np.sum(np.square(y[i:i+frame_length])))
    energy = np.array(energy)

    # Chuẩn hóa và đặt ngưỡng
    energy = energy / np.max(energy)
    threshold = 0.1

    # Xác định vùng tiếng nói
    frames = np.where(energy > threshold)[0]
    start_frame = frames[0]
    end_frame = frames[-1]

    # Quy đổi ngược về đơn vị thời gian
    start_time = start_frame * hop_length / sr
    end_time = end_frame * hop_length / sr

    return start_time, end_time
    

DATASET_DIR = "dataset"        
OUTPUT_CSV = "metadata.csv"

# LẤY DANH SÁCH CLASS
class_names = sorted([
    d for d in os.listdir(DATASET_DIR)
    if os.path.isdir(os.path.join(DATASET_DIR, d))
])

class_to_id = {cls: idx for idx, cls in enumerate(class_names)}

# DUYỆT FILE ÂM THANH
rows = []

for class_name in class_names:
    class_dir = os.path.join(DATASET_DIR, class_name)

    for file in os.listdir(class_dir):
        if file.endswith(".wav"):
            file_path = os.path.join(class_dir, file)

            start_time, end_time = endpoint_detection(file_path)

            rows.append({
                "slice_file_name": file,
                "start": start_time,
                "end": round(end_time, 6),
                "class": class_name
            })


# TẠO DATAFRAME & CSV
df = pd.DataFrame(rows)
df.to_csv(OUTPUT_CSV, index=False)

print("Đã tạo file:", OUTPUT_CSV)
print(df.head())
