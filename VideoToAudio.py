import os
import sys
from moviepy.editor import VideoFileClip

# Ensure that the script uses UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Path to the directory containing the videos (source path)
rawPath = r"D:\TEST 2\Data\YT"

# Path to the directory where the audio files will be saved (destination path)
resultPath = r"D:\TEST 2\Data\YT\Extracted_Audio"

# Supported video formats (you can add more if needed)
supported_formats = [".mp4", ".mkv", ".avi", ".mov"]

# Create the result directory if it doesn't exist
if not os.path.exists(resultPath):
    os.makedirs(resultPath)

# Loop through all files in the rawPath directory
for filename in os.listdir(rawPath):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1].lower()
    
    # Check if the file is a supported video format
    if file_extension in supported_formats:
        # Define the path for the output audio file in the resultPath
        audio_filename = os.path.splitext(filename)[0] + ".mp3"
        audio_path = os.path.join(resultPath, audio_filename)
        
        # Check if the audio file already exists in the resultPath
        if os.path.exists(audio_path):
            print(f"Audio file '{audio_filename}' already exists. Skipping...")
            continue  # Skip this file and move to the next one
        
        # Load the video file from rawPath
        video_path = os.path.join(rawPath, filename)
        video_clip = VideoFileClip(video_path)
        
        # Extract audio
        audio_clip = video_clip.audio
        
        # Write the audio file to the output path in resultPath
        audio_clip.write_audiofile(audio_path)
        
        # Close the clips to release resources
        audio_clip.close()
        video_clip.close()

print("All videos have been converted to audio!")
