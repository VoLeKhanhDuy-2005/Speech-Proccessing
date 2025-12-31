import os

def rename_files(folder_path, new_name):
    # Kiểm tra đường dẫn thư mục
    if not os.path.exists(folder_path):
        print("Đường dẫn thư mục không tồn tại!")
        return

    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(folder_path)
    
    # Sắp xếp để đảm bảo thứ tự (tùy chọn)
    files.sort()

    count = 1
    for filename in files:
        # Tách tên file và phần mở rộng (extension)
        file_name, file_ext = os.path.splitext(filename)
        
        # Tạo tên mới: TenMoi_SốThứTự.PhầnMởRộng
        new_filename = f"{new_name}_{count}{file_ext}"
        
        # Đường dẫn đầy đủ của file cũ và file mới
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        # Thực hiện đổi tên (chỉ đổi nếu là file, bỏ qua thư mục con)
        if os.path.isfile(old_path):
            os.rename(old_path, new_path)
            print(f"Đã đổi: {filename} -> {new_filename}")
            count += 1

# --- Cấu hình ở đây ---
path = r'C:\Users\Admin\Pictures\Anh_Du_Lich'  # Thay bằng đường dẫn thư mục
name_format = 'Da_Lat_2024'                   # Tên mới muốn đặt

rename_files(path, name_format)