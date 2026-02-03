import cv2
import os

# 视频文件所在的文件夹路径
video_folder = r"C:\Users\drasue\Desktop\dataset\videos"
# 图片保存的文件夹路径
image_folder = r"C:\Users\drasue\Desktop\dataset\images"

# 创建图片保存文件夹（如果不存在的话）
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 设置提取参数
fps_extract = 1  # 每秒提取多少帧，你可以调整这个参数
# 例如：fps_extract = 1 表示每秒提取1帧
#       fps_extract = 5 表示每秒提取5帧

# 获取视频文件夹中的所有视频文件
video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

print(f"找到 {len(video_files)} 个视频文件")

# 遍历每个视频文件
for video_file in video_files:
    # 构建完整的视频文件路径
    video_path = os.path.join(video_folder, video_file)

    # 获取视频文件名（不含扩展名）
    video_name = os.path.splitext(video_file)[0]

    print(f"正在处理视频: {video_file}")

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频的原始帧率
    original_fps = cap.get(cv2.CAP_PROP_FPS)

    # 计算每隔多少帧提取一张图片
    # 例如：原视频30fps，想每秒提取1帧，就每隔30帧提取一张
    frame_interval = int(original_fps / fps_extract)

    # 初始化帧计数器
    frame_count = 0
    saved_count = 0

    # 开始读取视频帧
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 如果读取失败（视频结束），退出循环
        if not ret:
            break

        # 检查是否到了该保存的帧
        if frame_count % frame_interval == 0:
            # 增加保存计数
            saved_count += 1

            # 生成图片文件名（三位数字序号）
            image_filename = f"{video_name}_{saved_count:03d}.jpg"

            # 构建完整的图片保存路径
            image_path = os.path.join(image_folder, image_filename)

            # 保存图片
            cv2.imwrite(image_path, frame)

            print(f"  已保存: {image_filename}")

        # 帧计数器加1
        frame_count += 1

    # 释放视频资源
    cap.release()

    print(f"视频 {video_file} 处理完成，共保存 {saved_count} 张图片")

print("所有视频处理完成！")