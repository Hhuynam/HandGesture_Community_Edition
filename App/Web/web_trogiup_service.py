import win32serviceutil
import win32service
import win32event
import servicemanager
import subprocess
import os
import time 
class WebTroGiupService(win32serviceutil.ServiceFramework):
    _svc_name_ = "WebTroGiupService"  # Tên dịch vụ (Unique)
    _svc_display_name_ = "Web Tro Giup Service"  # Tên hiển thị trong Windows Services
    _svc_description_ = "Chạy Flask app từ web_trogiup.py như một Windows Service."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.process = None  # Biến giữ tiến trình Flask app

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        if self.process:
            self.process.terminate()  # Dừng tiến trình Flask app
            self.process = None

    def SvcDoRun(self):
        python_path = r"D:\Project\HandGesture_Community_Edition\.venv\Scripts\python.exe"
        script_path = r"D:\Project\HandGesture_Community_Edition\App\Web\web_trogiup.py"
        import logging
        logging.basicConfig(filename=r'D:\service_debug.log', level=logging.DEBUG)
        try:
            logging.debug("Starting Flask app...")
            self.process = subprocess.Popen(["python", r"D:\Project\HandGesture_Community_Edition\App\Web\web_trogiup.py"], shell=False)
            
            # Tăng thời gian chờ để Flask app khởi động
            time.sleep(20)
            
            logging.debug("Flask app started successfully.")
            win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
        except Exception as e:
            logging.error(f"Error: {e}")
            self.SvcStop()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(WebTroGiupService)
