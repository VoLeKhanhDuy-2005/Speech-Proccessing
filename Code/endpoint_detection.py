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

    print(f"Start: {start_time:.4f}s, End: {end_time:.4f}s")
