import numpy as np
from scipy.interpolate import interp1d

def normalize_feature_length(feature_sequence, target_length):
    """
    Sử dụng nội suy tuyến tính để thay đổi độ dài của chuỗi đặc trưng 
    về độ dài mong muốn.

    Args:
        feature_sequence (np.ndarray): Mảng đặc trưng 2D, 
                                       dạng (số_khung, số_chiều_đặc_trưng).
        target_length (int): Độ dài mới (số khung) mong muốn.

    Returns:
        np.ndarray: Chuỗi đặc trưng đã được chuẩn hóa độ dài, 
                    dạng (target_length, số_chiều_đặc_trưng).
    """
    
    # 1. Xác định kích thước
    N_original = feature_sequence.shape[0]  # Số khung ban đầu
    D_features = feature_sequence.shape[1]  # Số chiều đặc trưng (ví dụ: 13 MFCC)

    # 2. Tạo trục thời gian/chỉ số ban đầu (từ 0 đến N_original - 1)
    # Đây là trục X của hàm gốc
    original_indices = np.arange(N_original)
    
    # 3. Tạo trục thời gian/chỉ số mới (từ 0 đến target_length - 1)
    # Đây là trục X mà chúng ta muốn lấy mẫu
    target_indices = np.linspace(0, N_original - 1, target_length)

    # Khởi tạo mảng kết quả
    normalized_sequence = np.zeros((target_length, D_features))

    # 4. Thực hiện nội suy cho TỪNG chiều đặc trưng
    for d in range(D_features):
        # Lấy mảng 1D cho chiều đặc trưng hiện tại
        original_values = feature_sequence[:, d]
        
        # Xây dựng hàm nội suy 1 chiều từ dữ liệu gốc
        # kind='linear' là nội suy tuyến tính
        # bounds_error=False cho phép ngoại suy, fill_value='extrapolate' 
        # đảm bảo giá trị tại biên được xử lý đúng (mặc dù với linspace, 
        # nó hiếm khi xảy ra)
        interp_func = interp1d(original_indices, original_values, 
                               kind='linear', bounds_error=False, 
                               fill_value='extrapolate')
        
        # Áp dụng hàm nội suy lên trục thời gian mới để có các giá trị mới
        normalized_values = interp_func(target_indices)
        
        # Gán vào mảng kết quả
        normalized_sequence[:, d] = normalized_values

    return normalized_sequence

# --- DỮ LIỆU MÔ PHỎNG (VÍ DỤ) ---

# Giả sử chúng ta có 2 đoạn tiếng nói đã được trích xuất MFCC
# Kích thước đặc trưng: 13 chiều (D=13)

D_features = 13
TARGET_LENGTH = 100 # Độ dài chuẩn mong muốn (100 khung)

# Đoạn tiếng nói 1: Dài 85 khung
N1 = 85 
voice_features_A = np.random.rand(N1, D_features) 

# Đoạn tiếng nói 2: Dài 130 khung
N2 = 130 
voice_features_B = np.random.rand(N2, D_features) 

print(f"**Trạng thái ban đầu:**")
print(f"Đoạn A: {voice_features_A.shape[0]} khung, {voice_features_A.shape[1]} chiều")
print(f"Đoạn B: {voice_features_B.shape[0]} khung, {voice_features_B.shape[1]} chiều")
print(voice_features_A)
print("-" * 30)

# --- THỰC HIỆN CHUẨN HÓA ---

normalized_A = normalize_feature_length(voice_features_A, TARGET_LENGTH)
normalized_B = normalize_feature_length(voice_features_B, TARGET_LENGTH)

print(f"**Kết quả sau khi Chuẩn hóa (Target Length: {TARGET_LENGTH}):**")
print(f"Đoạn A (chuẩn hóa): {normalized_A.shape[0]} khung, {normalized_A.shape[1]} chiều")
print(f"Đoạn B (chuẩn hóa): {normalized_B.shape[0]} khung, {normalized_B.shape[1]} chiều")
print(normalized_A)