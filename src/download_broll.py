import os
import json
import requests
from dotenv import load_dotenv

# Load API keys
load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def download_broll_clips():
    keywords_path = "data/text/keywords.json"
    output_dir = "data/broll"
    
    if not PEXELS_API_KEY:
        print("❌ Error: PEXELS_API_KEY not found in environment variables.")
        return False
        
    if not os.path.exists(keywords_path):
        print(f"❌ Error: Keywords file not found at {keywords_path}")
        return False
        
    os.makedirs(output_dir, exist_ok=True)
    
    with open(keywords_path, "r") as f:
        keywords = json.load(f)
        
    headers = {"Authorization": PEXELS_API_KEY}
    
    print(f"🎬 Starting B-Roll search for keywords: {keywords}")
    
    for idx, keyword in enumerate(keywords):
        print(f"🔍 Searching Pexels for: '{keyword}'...")
        url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=1&orientation=landscape"
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                if videos:
                    # Grab the lowest-resolution HD video link to save bandwidth and compile faster
                    video_files = videos[0].get("video_files", [])
                    # Filter for HD or standard size instead of massive 4K
                    best_file = min(video_files, key=lambda x: x.get("width", 1920))
                    download_url = best_file.get("link")
                    
                    print(f"📥 Downloading clip {idx+1}...")
                    video_data = requests.get(download_url).content
                    clip_name = f"clip_{idx+1}.mp4"
                    
                    with open(os.path.join(output_dir, clip_name), "wb") as file:
                        file.write(video_data)
                    print(f"✅ Saved {clip_name}")
                else:
                    print(f"⚠️ No videos found on Pexels for '{keyword}'")
            else:
                print(f"❌ Pexels API responded with status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Failed to fetch assets for '{keyword}': {e}")
            
    return True

if __name__ == "__main__":
    download_broll_clips()
