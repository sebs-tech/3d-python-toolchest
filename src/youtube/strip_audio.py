import os
from moviepy.editor import VideoFileClip

# Function to strip audio from a video file
def strip_audio_from_video(input_file, output_file):
    try:
        # Load the video file
        video_clip = VideoFileClip(input_file)
        
        # Remove the audio from the video
        video_without_audio = video_clip.without_audio()
        
        # Write the result to the output file
        video_without_audio.write_videofile(output_file, codec="libx264", audio_codec="aac")
        
        print(f"Successfully processed: {input_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Function to process all video files in a directory
def process_video_directory(input_dir, output_dir):
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file path
        input_file = os.path.join(input_dir, filename)

        # Only process video files (you can add more formats if needed)
        if os.path.isfile(input_file) and filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            output_file = os.path.join(output_dir, f"no_audio_{filename}")
            strip_audio_from_video(input_file, output_file)

# Main function
if __name__ == "__main__":
    input_dir = "downloaded_videos/"  # Replace with the directory containing your video files
    output_dir = "videos_mutey"  # Replace with the directory where you want to save the output videos

    process_video_directory(input_dir, output_dir)
