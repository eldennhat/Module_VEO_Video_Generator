from veo_video_generator.video_generator import generate_video

if __name__ == "__main__":
    prompt = "Tạo video chú chó đang nhảy múa trong công viên"
    try:
        video_url = generate_video(prompt)
        print(f"✅ Video URL: {video_url}")
    except Exception as e:
        print(f"❌ Lỗi khi tạo video: {e}")
