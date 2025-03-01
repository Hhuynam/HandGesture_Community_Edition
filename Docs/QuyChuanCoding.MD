# QuyChuanCoding.MD: Quy chuẩn lập trình và quản lý dự án, quy định về cấu trúc, đặt tên, comment, logging, kiểm soát phiên bản
# QUY CHUẨN LẬP TRÌNH & QUẢN LÝ PROJECT
## 1.CẤU TRÚC DỰ ÁN
- **Mỗi project phải có cấu trúc rõ ràng**, gồm các thư mục chính:
  - `App/` - Chứa file chạy chính của ứng dụng
  - `Module/` - Chứa các module, thư viện hỗ trợ
  - `Dataset/` - Chứa dữ liệu huấn luyện hoặc dữ liệu test
  - `Logs/` - Chứa file log ghi lại hoạt động
  - `Tests/` - Chứa các file test
  - `Docs/` - Chứa tài liệu hướng dẫn, mô tả hệ thống
  - `.venv/` - Môi trường ảo Python (nếu có)
  - `README.md` - Mô tả tổng quan về project
## 2.QUY CHUẨN VIẾT CODE
### 2.1.Quy tắc đặt tên
- **Thư mục:** Viết chữ thường, có thể dùng dấu gạch dưới `_` nếu cần
- **File Python:** Viết chữ thường, có `_` nếu nhiều từ (VD: `process_data.py`)
- **Biến và Hàm:** Dùng `snake_case` (VD: `load_model()` hoặc `data_path`)
- **Lớp (Class):** Dùng `PascalCase` (VD: `ImageProcessor`)
### 2.2.Quy chuẩn comment
- **Mỗi file phải có comment đầu tiên ngắn gọn (comment first line)**, giải thích file làm gì
- **Mỗi comment không kết thúc bằng dấu chấm**
- **Hàm, class quan trọng phải có docstring(Comment giúp giải thích mục đích của các biến hoặc logic phức tạp)** theo format:
  ```python
  def add_numbers(a: int, b: int) -> int:
      """
      Cộng hai số nguyên
      Args:
          a (int): Số nguyên thứ nhất
          b (int): Số nguyên thứ hai
      Returns:
          int: Tổng của a và b
      """
      return a + b
  ```
### 2.2.Quy chuẩn spacing 
- Với mọi trường hợp, không được để xuất hiện cách dòng 
## 3.GHI LOG
- Log phải được ghi vào file trong `Logs/`
- **Dùng kiểu ghi tiếp (`append`)**, không ghi đè file cũ
- Log cần có timestamp và cấp độ (INFO, WARNING, ERROR)
- Khi đọc log, đảm bảo file được mở với `utf-8` để tránh lỗi mã hóa
## 4.KIỂM SOÁT PHIÊN BẢN
- **Dùng Git để quản lý mã nguồn**
- Mỗi project phải có `.gitignore` để tránh commit file không cần thiết
- Khi sửa code lớn, làm trên branch riêng, sau đó merge vào `main`
## 5.CHẠY VÀ TEST
- Mỗi dự án phải có ít nhất một file test trong `Tests/`
- **Trước khi push code, phải kiểm tra lỗi và chạy test**
- Nếu project có môi trường ảo, chạy trong `.venv` để tránh xung đột thư viện
## 6.QUY TẮC KHÁC
- **Không dùng icon trong code, trừ giao diện UI/UX hoặc log nếu thực sự cần**
- **Không viết code rời rạc, phải có cấu trúc rõ ràng**
- **Luôn viết code dễ hiểu, không viết tắt quá mức gây khó đọc**
## 7.LỊCH SỬ CẬP NHẬT
- **01/03/2025**: Tạo quy chuẩn ban đầu
---
### Standard by HaHuyNam - K215480106063  
Mọi dự án phải tuân thủ quy chuẩn này nhằm đảm bảo tính thống nhất, hiệu quả và dễ dàng bảo trì  
Quy định sẽ được cập nhật liên tục để phù hợp với yêu cầu thực tế  
🔗 **GitHub:** [Hhuynam](https://github.com/Hhuynam)

