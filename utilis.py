import os
import cv2


def capture_frames(video_path, output_folder, frame_interval, num_files_in_output_folder,smoke_name):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        success, frame = cap.read()

        if not success:
            break

        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_folder, smoke_name+'_' + f"frame_{num_files_in_output_folder}.jpg")
            print(output_path)
            cv2.imwrite(output_path, frame)
            num_files_in_output_folder += 1
        frame_count += 1
    cap.release()


def extra_frames(base_folder, output_Folder, frame_interval):
    for root, dirs, files in os.walk(base_folder):
        if root != base_folder:
            smoke_name = root.replace(base_folder, '')
            smoke_index = 0

            for file in files:
                video_path = os.path.join(root, file)

                # 视频重命名---------------------------------------------------------
                current_file_name = video_path
                new_file_name = root + smoke_name + '%s' % smoke_index + '.mp4'
                if current_file_name != new_file_name:
                    if os.path.exists(current_file_name):
                        os.rename(current_file_name, new_file_name)
                smoke_index += 1
                # 重命名结束---------------------------------------------------------

                if file.endswith('.mp4'):  # 其他格式修改即可
                    video_path = new_file_name
                    output_folder = os.path.join(output_Folder, os.path.basename(root))
                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder)

                    files = [f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))]
                    num_files_in_output_folder = len(files)

                    output_folder = output_folder
                    frame_interval = frame_interval
                    capture_frames(video_path=video_path,
                                   output_folder=output_folder,
                                   frame_interval=frame_interval,
                                   num_files_in_output_folder=num_files_in_output_folder,
                                   smoke_name=smoke_name)
