import requests

# Dictionary to define supported OTT platforms and their formats
OTT_PLATFORMS = {
    "Netflix": {
        "formats": ["mp4", "mkv"],
        "url_pattern": "https://www.netflix.com/download/{video_id}"
    },
    "Hotstar": {
        "formats": ["mp4", "avi"],
        "url_pattern": "https://www.hotstar.com/download/{video_id}"
    },
    "MXPlayer": {
        "formats": ["mp4", "webm"],
        "url_pattern": "https://www.mxplayer.in/download/{video_id}"
    },
    # Add other platforms here
}

def download_video(video_url, user_id, platform=None, format_choice="mp4"):
    try:
        # If platform is provided, check if it's supported
        if platform and platform in OTT_PLATFORMS:
            platform_data = OTT_PLATFORMS[platform]
            # Check if the selected format is supported for the platform
            if format_choice not in platform_data["formats"]:
                return {"success": False, "error": f"Format '{format_choice}' not supported for {platform}."}
            # Modify the video_url if needed based on the platform's pattern
            video_url = platform_data["url_pattern"].format(video_id=video_url)
        else:
            # If no platform is provided, assume the URL is direct
            if not video_url.endswith(format_choice):
                return {"success": False, "error": f"The video URL does not end with the selected format ({format_choice})."}

        # Define the file name based on user ID and chosen format
        video_file = f"{user_id}_video.{format_choice}"

        # Download video content
        video_data = requests.get(video_url, stream=True)
        
        # Check if the request was successful
        if video_data.status_code != 200:
            return {"success": False, "error": "Failed to download video, status code: " + str(video_data.status_code)}

        # Save the video to a file
        with open(video_file, "wb") as f:
            for chunk in video_data.iter_content(chunk_size=1024):
                f.write(chunk)

        return {"success": True, "file": video_file}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Example usage
video_url = "12345"  # This would be the video ID or actual URL depending on platform
user_id = 123456
platform = "Netflix"  # Example OTT platform
format_choice = "mp4"  # User's selected format

result = download_video(video_url, user_id, platform, format_choice)
print(result)
