import cv2
import os
from pathlib import Path
from ffpyplayer.player import MediaPlayer

def list_video_files(directory):
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}
    video_files = [f for f in os.listdir(directory) if Path(f).suffix.lower() in video_extensions]
    return video_files

def find_file(file_name, search_directory):
    file_path = Path(search_directory) / file_name
    if file_path.exists():
        return file_path
    print(f"File '{file_name}' not found in directory '{search_directory}'.")
    return None

def play_video(video_path):
    video = cv2.VideoCapture(str(video_path))
    player = MediaPlayer(str(video_path))

    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()

        if not grabbed:
            print("End of video")
            break

        if cv2.waitKey(28) & 0xFF == ord('q'):
            break

        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, _ = audio_frame

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_directory = input("Enter the directory that contains the video files: ")
    video_directory = Path(video_directory)

    if not video_directory.is_dir():
        print(f"The directory '{video_directory}' does not exist.")
    else:
        video_files = list_video_files(video_directory)

        if not video_files:
            print("No video files found in the directory.")
        else:
            print("Video files found:")
            for idx, video_file in enumerate(video_files):
                print(f"{idx + 1}: {video_file}")

            choice = int(input("Enter the number of the video file you want to play: ")) - 1

            if 0 <= choice < len(video_files):
                selected_video = video_files[choice]
                video_path = find_file(selected_video, video_directory)

                if video_path:
                    play_video(video_path)
                else:
                    print("Unable to play the video.")
            else:
                print("Invalid selection.")
