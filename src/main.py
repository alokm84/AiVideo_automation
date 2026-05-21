import subprocess
import sys
import os

def run_step(step_name, command):
    print("\n" + "="*60)
    print(f"🚀 Running: {step_name}")
    print("="*60)
    
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(f"\n❌ {step_name} failed (exit code {result.returncode}).")
        print("❌ Pipeline aborted — fix the error above and re-run main.py.")
        sys.exit(1)
    print(f"✅ {step_name} completed successfully!")

def main():
    print("🏁 STARTING VIDEO AUTOMATION PIPELINE 🏁")
    
    # Ensure raw data directories exist
    os.makedirs("data/text", exist_ok=True)
    os.makedirs("data/audio", exist_ok=True)
    os.makedirs("data/broll", exist_ok=True)
    os.makedirs("data/output", exist_ok=True)

    # 1. Generate Script and Keywords
    run_step("Script & Keyword Generation", "python src/generate_script.py")
    
    # 2. Convert Script Text to Audio Narration
    run_step("Voiceover Generation", "python src/generate_voice.py")
    
    # 3. Download Matching B-Roll Clips
    run_step("B-Roll Asset Downloading", "python src/download_broll.py")
    
    # 4. Stitch Videos and Render Final MP4
    run_step("Video Compositing & Rendering", "python src/create_video.py")

    print("\n" + "#"*60)
    print("#  🏁  PIPELINE COMPLETE SUCCESS")
    print("#" * 60)
    print(f"✅ Final video with B-Roll → data/output/final_output.mp4\n")

if __name__ == "__main__":
    main()
