# VEO Video Generator 🎥

Module này cho phép bạn sinh video từ một câu lệnh văn bản (prompt) bằng cách gọi Google VEO API.

## Cấu trúc module

- `prompt_cleaner.py`: Làm sạch prompt đầu vào
- `prompt_formatter.py`: Format lại prompt theo cấu trúc mong muốn
- `api_config.py`: Lưu trữ endpoint và API Key
- `veo_api_caller.py`: Gửi request đến Google VEO
- `output_handler.py`: Trích xuất video URL từ kết quả
- `video_generator.py`: Giao diện chính điều phối tất cả

## Cách sử dụng

1. Cài `requests` nếu chưa có:
2. Chạy: python main.py
> Đừng quên thay thế `YOUR_API_KEY_HERE` và `YOUR_PROJECT_ID` trong `api_config.py`
