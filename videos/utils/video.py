from pathlib import Path

import cv2
import os


class VideoSlicer:

    def __init__(self, frame_pause: int =22):
        self.frame_pause = frame_pause
        pass

    def parse_all_videos(
        self, video_dir: Path = "assets/videos/", img_dir: Path = "assets/images/"
    ) -> void:
        """
        Parses all video files in a given directory and saves frames as images in another directory.

        ### Args:
        - video_dir (Path, optional): Path to the directory containing video files. Defaults to "assets/videos/".
        - img_dir (Path, optional): Path to the directory where extracted images will be saved. Defaults to "assets/images/".
        """

        videos = [
            os.path.join(video_dir, f)
            for f in os.listdir(video_dir)
            if os.path.isfile(os.path.join(video_dir, f))
        ]

        for video in videos:
            self.parse_video(Path(video), img_dir)

    def parse_video_gpu(self, video_path: Path, img_dir: Path) -> void:
        """
        Parses frames from a single video file using GPU acceleration and saves them as images.

        ### Args:
        - video_path (Path): Path to the video file to be processed.
        - img_dir (Path): Path to the directory where extracted images will be saved.
        """

        filename, ext = os.path.basename(video_path).split(".")
        count, frame_number = 0, -1
        video_cap = cv2.cudacodec.createVideoReader(video_path)
        while True:
            frame_number += 1
            success, gpu_frame = video_cap.nextFrame()
            if not success:
                break
            if frame_number % self.frame_pause != 0:
                continue

            resized_image = cv2.resize(gpu_frame.download(), IMAGE_SIZE)

            cv2.imwrite(
                f"{img_dir}/{filename}_{str(count).zfill(5)}.jpg", resized_image
            )

            count += 1
            frame_number = 0


    def parse_video(self, video_path: Path, img_dir: Path) -> void:
        """
        Parses frames from a single video file using CPU and saves them as images.

        ### Args:
        - video_path (Path): Path to the video file to be processed.
        - img_dir (Path): Path to the directory where extracted images will be saved.
        """

        capture = cv2.VideoCapture(str(video_path))
        filename, ext = os.path.basename(video_path).split(".")
        frame = 0


        while True:
            _, image = capture.read()
            if image is None:
                break

            if frame % self.frame_pause == 0:
                image = cv2.resize(image, IMAGE_SIZE)
                cv2.imwrite(f"{img_dir}/{filename}_{str(frame).zfill(5)}.jpg", image)
            frame += 1

        capture.release()
