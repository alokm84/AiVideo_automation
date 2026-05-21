import os
from google import genai

def generate_video_script(topic: str, output_path: str):
    """Generates a short video script using Gemini 2.5 Flash."""
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Initialize the standard client (automatically picks up GEMINI_API_KEY from .env)
    client = genai.Client()
    
    prompt = f"Write a highly engaging, 30-second video voiceover script about: {topic}. Do not include stage directions or brackets, just the spoken text."
    
    print(f"🤖 Asking Gemini to write a script about: {topic}...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    script_text = response.text
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(script_text)
        
    print(f"✅ Script saved successfully at: {output_path}")
    return script_text

if __name__ == "__main__":
    test_topic = "Why Python is the king of automation"
    test_output = "data/scripts/test_script.txt"
    generate_video_script(test_topic, test_output)
