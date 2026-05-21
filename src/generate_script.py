import os
import json
from google import genai
from google.genai import types

def generate_video_assets():
    print("🤖 Prompting Gemini for script and B-roll keywords...")
    
    # Get user input for the tutorial topic
    topic = input("Please enter the tutorial topic (e.g., 'Python programming', 'Machine Learning basics'): ")
    
    # Get user input for video duration
    while True:
        try:
            duration_str = input("Please enter the desired video duration in seconds (e.g., '15', '30'): ")
            duration = int(duration_str)
            if duration <= 0:
                print("Duration must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for the duration.")

    # Initialize the standard Google GenAI client
    client = genai.Client()
    
    prompt = f"""
    Create a short, engaging {duration}-second motivational or educational script about {topic}.
    
    You must return your response as a valid JSON object with exactly two keys:
    1. 'narration_text': The spoken script text for the voiceover.
    2. 'search_keywords': A list of 3-4 highly specific visual keywords (e.g., 'coding laptop close up', 'abstract digital data', 'programmer working typing') that we can use to search for free B-roll stock video footage.
    
    Do not include any markdown formatting like ```json or ``` in your response. Return pure text JSON.
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Clean clean-up text if markdown leaked in
        clean_text = response.text.strip().lstrip("```json").rstrip("```").strip()
        data = json.loads(clean_text)
        
        # Ensure directories exist
        os.makedirs("data/text", exist_ok=True)
        
        # Save narration text for the voice generator
        with open("data/text/script.txt", "w") as f:
            f.write(data["narration_text"])
            
        # Save B-roll keywords for our asset downloader
        with open("data/text/keywords.json", "w") as f:
            json.dump(data["search_keywords"], f, indent=4)
            
        print("✅ Successfully generated script and B-roll keywords!")
        print(f"🔑 Target Keywords: {data['search_keywords']}")
        return True

    except Exception as e:
        print(f"❌ Failed to generate script: {e}")
        return False

if __name__ == "__main__":
    generate_video_assets()
