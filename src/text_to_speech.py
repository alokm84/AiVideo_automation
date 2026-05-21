import os
from gtts import gTTS

def convert_text_to_audio(text: str, output_filename: str):
    """
    Converts the given text to an audio file using gTTS and saves it
    in the 'data/audio/' directory.

    Args:
        text (str): The text content to convert to speech.
        output_filename (str): The desired filename for the audio file (e.g., "script_part_1.mp3").
    """
    if not text:
        print("Warning: No text provided for audio conversion.")
        return

    audio_dir = "data/audio/"
    os.makedirs(audio_dir, exist_ok=True)

    output_path = os.path.join(audio_dir, output_filename)

    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)
        print(f"Audio saved successfully to {output_path}")
    except Exception as e:
        print(f"Error converting text to audio: {e}")

if __name__ == '__main__':
    # Example usage:
    sample_text = "Hello, this is a test of the text to speech conversion using gTTS. It's quite simple and effective."
    convert_text_to_audio(sample_text, "sample_audio.mp3")

    sample_text_2 = "This is another piece of text to demonstrate saving multiple files."
    convert_text_to_audio(sample_text_2, "another_sample.mp3")

    # Test with an empty string
    convert_text_to_audio("", "empty_test.mp3")
