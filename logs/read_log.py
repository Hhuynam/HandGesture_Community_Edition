# 📄 read_log.py - Đọc và hiển thị nội dung file log UTF-8

import os

log_file = "logs/app.log"

def read_log(file_path):
    """Đọc file log và hiển thị nội dung."""
    if not os.path.exists(file_path):
        print(f"❌ Không tìm thấy file log: {file_path}")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            log_content = f.readlines()

        if not log_content:
            print("📜 Log trống!")
            return

        print("\n📜 Nội dung Log:")
        for line in log_content:
            print(line.strip())

    except Exception as e:
        print(f"❌ Lỗi khi đọc log: {e}")

# 🏃‍♂️ Chạy đọc log
read_log(log_file)
