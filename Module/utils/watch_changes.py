import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, process, script_path):
        self.process = process  # Để có thể dừng tiến trình cũ khi có sự thay đổi
        self.script_path = script_path

    def on_modified(self, event):
        if event.src_path.endswith("main.py"):
            print(f"{event.src_path} đã thay đổi. Đang reload lại chương trình...")
            self.process.terminate()  # Dừng chương trình cũ
            self.process.wait()  # Chờ chương trình cũ dừng hoàn toàn
            self.start_new_process()  # Khởi động lại chương trình

    def start_new_process(self):
        # Chỉ rõ Python executable và script path
        self.process = subprocess.Popen([python_executable, self.script_path])  # Khởi động lại main.py


def start_program(script_path):
    # Chỉ rõ Python executable và script path
    return subprocess.Popen([python_executable, script_path])  # Khởi động lần đầu tiên


if __name__ == "__main__":
    # Đảm bảo bạn sử dụng đường dẫn tuyệt đối chính xác đến file main.py
    script_path = "D:/Project/HandGesture_Community_Edition/App/main.py"

    if not os.path.exists(script_path):
        print(f"Lỗi: Không thể tìm thấy tệp {script_path}")
        exit(1)

    # Xác định đường dẫn Python executable trong virtual environment
    python_executable = "D:/Project/HandGesture_Community_Edition/.venv/Scripts/python.exe"

    # Khởi động chương trình lần đầu tiên
    process = start_program(script_path)

    # Tạo một event handler cho watchdog
    event_handler = ReloadHandler(process, script_path)

    # Đặt đường dẫn giám sát
    path = "D:/Project/HandGesture_Community_Edition/App"
    
    # Tạo observer để theo dõi sự thay đổi trong thư mục
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    # Bắt đầu giám sát sự thay đổi
    observer.start()

    try:
        while True:
            time.sleep(1)  # Giữ chương trình chạy
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
