import yt_dlp

# Function to download video from a YouTube link
def download_video(video_url):
    try:
        # Set options for yt-dlp to download the highest quality available
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Set the output template to save with the video title
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
    
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

# Main function to process the file
def download_videos_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            video_links = file.readlines()
            
            for link in video_links:
                link = link.strip()  # Remove any extra whitespace or newlines
                if link:  # Only proceed if the link is not empty
                    download_video(link)
                
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File containing YouTube links (one per line)
file_name = 'videos.txt'

# Start the download process
download_videos_from_file(file_name)
