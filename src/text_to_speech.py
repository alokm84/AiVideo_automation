import os
from gtts import gTTS

def convert_text_to_audio(text, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"🔊 Converting text to speech...")
    tts = gTTS(text=text, lang='en', tld='com')
    tts.save(output_path)
    print(f"✅ Audio saved successfully at: {output_path}")

if __name__ == "__main__":
    test_text = "Testing our free text to speech engine."
    test_output = "data/audio/narration.mp3"
    convert_text_to_audio(test_text, test_output)
