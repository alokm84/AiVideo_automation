import os
from gtts import gTTS

def generate_voiceover():
    script_path = "data/text/script.txt"
    output_path = "data/audio/narration.mp3"
    
    # Ensure audio directory exists
    os.makedirs("data/audio", exist_ok=True)
    
    if not os.path.exists(script_path):
        print(f"❌ Error: Script file not found at {script_path}")
        return False
        
    print("🎙️ Reading script text...")
    with open(script_path, "r") as f:
        text = f.read().strip()
        
    if not text:
        print("❌ Error: Script file is empty!")
        return False
        
    print("🗣️ Converting text to speech audio...")
    try:
        # Generate English speech audio
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)
        print(f"✅ Voiceover saved successfully to {output_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to generate voiceover: {e}")
        return False

if __name__ == "__main__":
    generate_voiceover()
