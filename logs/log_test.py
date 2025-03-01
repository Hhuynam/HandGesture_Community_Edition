# 📄 log_test.py - Ghi log test vào file app.log (UTF-8, ghi tiếp)

import logging
import os

# Đảm bảo thư mục logs tồn tại
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")

# Cấu hình logging (ghi tiếp, UTF-8)
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    filemode="a",  # Ghi tiếp vào log
)

# Ghi log test
logging.info("Start: Chuong trinh khoi dong")
logging.warning("Warning: Day la canh bao test")
logging.error("Error: Loi gia lap de kiem tra test")

print(f"✅ Log đã được ghi vào {log_file}")
