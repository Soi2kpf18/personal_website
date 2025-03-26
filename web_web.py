from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho trang chủ
@app.route('/')
def home():
    # Trả về giao diện từ file HTML
    return render_template('index.html')

# Chạy ứng dụng Flask ở chế độ debug
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Lấy PORT từ biến môi trường


# Hướng dẫn cấu trúc thư mục:
# - Thư mục chính (chứa file app.py)
# - Thư mục templates (chứa index.html)
# - Thư mục static (chứa style.css)
#tạo môi trường ảo: python -m venv venv
#chạy mtruong ảo: venv\Scripts\activate
#tắt mtruong ảo: deactivate
#chạy chtrinh: python C:\personal_website\web_web.py
