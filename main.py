from utilis import extra_frames,capture_frames

if __name__ == '__main__':

        base_folder = r'.\videos'
        output_Folder = r'.\frames'
        frame_interval = 200

        extra_frames(base_folder, output_Folder, frame_interval)