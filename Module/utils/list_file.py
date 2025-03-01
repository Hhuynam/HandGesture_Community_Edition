# list_file.py: Code để hiển thị file bên trong folder, hiện tại là max=5, muốn tối đa bao nhiêu file hãy sửa max 
import os

def list_folders_with_files(folder_path, max_files=5): #max = 5
    """Liệt kê các thư mục con và tối đa max_files file trong mỗi thư mục"""
    if not os.path.exists(folder_path):
        print(f"❌ Folder không tồn tại: {folder_path}")
        return

    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    if folders:
        print(f"📂 Danh sách thư mục trong {folder_path}:")
        for folder in folders:
            folder_full_path = os.path.join(folder_path, folder)
            print(f"  📁 {folder}")

            files = [f for f in os.listdir(folder_full_path) if os.path.isfile(os.path.join(folder_full_path, f))]
            if files:
                print(f"    📄 Files ({min(len(files), max_files)}): {', '.join(files[:max_files])}")
            else:
                print(f"    📂 Không có file nào trong {folder}")
    else:
        print(f"📂 Không có thư mục nào trong {folder_path}")

# Chạy hàm với đường dẫn folder của bạn
folder_path = r"D:\Project\HandGesture_Community_Edition"
list_folders_with_files(folder_path)
