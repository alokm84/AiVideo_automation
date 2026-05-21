import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip

def create_video_clip():
    audio_path = "data/audio/narration.mp3"
    music_path = "data/music/background.mp3"
    broll_dir = "data/broll"
    output_dir = "data/output"
    output_path = os.path.join(output_dir, "final_output.mp4")
    
    os.makedirs(output_dir, exist_ok=True)
        
    if not os.path.exists(audio_path):
        print(f"❌ Voice audio file not found at {audio_path}")
        return False

    print("🎬 Loading main voice track...")
    voice_clip = AudioFileClip(audio_path)
    total_duration = voice_clip.duration
    print(f"🎵 Voice duration: {total_duration:.2f} seconds")

    print("🎞️ Gathering and processing B-roll clips...")
    clips = []
    broll_files = sorted([f for f in os.listdir(broll_dir) if f.endswith(".mp4")])
    
    if not broll_files:
        print("❌ No B-roll clips found to stitch!")
        return False

    for file_name in broll_files:
        file_path = os.path.join(broll_dir, file_name)
        clip = VideoFileClip(file_path).with_audio(None)
        clips.append(clip)

    print("🪡 Stitching video clips together...")
    full_bg_sequence = concatenate_videoclips(clips, method="compose")

    # Sync visual timeline with voice length
    if full_bg_sequence.duration > total_duration:
        full_bg_sequence = full_bg_sequence.with_duration(total_duration)
    else:
        full_bg_sequence = full_bg_sequence.with_duration(total_duration)

    # Add background music if available
    if os.path.exists(music_path):
        print("🎵 Mixing background music track...")
        # Load music, trim it to match video duration, and reduce volume significantly (8%)
        bg_music = AudioFileClip(music_path).with_duration(total_duration).with_multiply_volume(0.08)
        
        # Combine voice and background music together into a single layered audio track
        final_audio = CompositeAudioClip([voice_clip, bg_music])
    else:
        print("⚠️ Background music track missing, rendering with voice only.")
        final_audio = voice_clip

    print("🎛️ Merging mixed audio timeline into the video...")
    final_video = full_bg_sequence.with_audio(final_audio)

    print("🚀 Rendering final video with background music...")
    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        logger=None
    )
    
    # Close assets cleanly
    voice_clip.close()
    if os.path.exists(music_path):
        bg_music.close()
    final_audio.close()
    full_bg_sequence.close()
    final_video.close()
    for c in clips:
        c.close()
        
    print(f"✅ Video successfully created at: {output_path}")
    return True

if __name__ == "__main__":
    create_video_clip()
