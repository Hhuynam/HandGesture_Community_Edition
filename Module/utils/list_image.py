import os

def list_images(directory: str):
    """
        Liệt kê số lượng file ảnh trong thư mục. Hãy chạy và paste đường dẫn của folder (phải chứa ảnh)
    Args:
        directory (str): Đường dẫn đến thư mục chứa các file ảnh.
    Returns:
        int: Số lượng file ảnh trong thư mục.
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    image_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in image_extensions]
    
    # In ra danh sách file ảnh
    print("Danh sách file ảnh:", image_files)
    
    return len(image_files)

if __name__ == "__main__":
    directory = input("Nhập đường dẫn đến thư mục ảnh: ")  # Nhập đường dẫn thư mục ảnh
    if os.path.exists(directory) and os.path.isdir(directory):  # Kiểm tra thư mục hợp lệ
        image_count = list_images(directory)
        print(f"Số lượng file ảnh trong thư mục {directory}: {image_count}")
    else:
        print("Thư mục không tồn tại hoặc không hợp lệ!")
