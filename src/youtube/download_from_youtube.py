import yt_dlp
import os
import subprocess

# Function to download video from a YouTube link
def download_video(video_url, download_folder):
    try:
        # Set options for yt-dlp to download the highest quality available
        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save the video in the specified folder with the video title
            'format': 'bestvideo+bestaudio/best',  # Download the best video + best audio or best overall if no separate streams
        }
        
        # Initialize yt-dlp and extract video info
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            video_title = video_info.get('title', 'Untitled')  # Get video title
            print(f"Downloading: {video_title}")

            # Now download the video
            ydl.download([video_url])
            print(f"Download complete for: {video_title}")
        
        # Get the downloaded file name (based on title and format)
        downloaded_file = os.path.join(download_folder, f"{video_title}.webm")  # Assuming WebM format is downloaded
        mp4_file = os.path.join(download_folder, f"{video_title}.mp4")  # Output MP4 file
        
        # Convert to MP4 using ffmpeg if the file is in WebM format
        if os.path.exists(downloaded_file):
            print(f"Converting {downloaded_file} to MP4...")
            convert_to_mp4(downloaded_file, mp4_file)
            print(f"Conversion complete: {mp4_file}")
            
            # Remove the original WebM file after conversion (optional)
            os.remove(downloaded_file)
            print(f"Removed the original WebM file: {downloaded_file}")
    
    except Exception as e:
        print(f"Error downloading or converting {video_url}: {e}")

# Function to convert video to MP4 using ffmpeg
def convert_to_mp4(input_file, output_file):
    try:
        # Use ffmpeg to convert the file to MP4 format
        command = ['ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-acodec', 'aac', output_file]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"An error occurred while converting: {e}")

# Main function to process the file
def download_videos_from_file(file_name, download_folder):
    try:
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)  # Create download folder if it doesn't exist
        
        with open(file_name, 'r') as file:
            video_links = file.readlines()
            
            for link in video_links:
                link = link.strip()  # Remove any extra whitespace or newlines
                if link:  # Only proceed if the link is not empty
                    download_video(link, download_folder)
                
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File containing YouTube links (one per line)
file_name = 'videos.txt'
download_folder = 'downloaded_videos'  # Folder to save downloaded videos

# Start the download and conversion process
download_videos_from_file(file_name, download_folder)
