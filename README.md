# Autonomous AI Video Generation & Subtitle Pipeline Engine 🎬🤖

An advanced, end-to-end Python automation framework that transforms plain-text educational topics into fully edited, multi-layered video tutorials complete with contextual B-roll, background music routing, and time-aligned burned subtitles.

---

## 💡 System Architecture & Core Features

This pipeline replaces a traditional video editor's multi-hour manual workflow by structuring content production into an automated engineering assembly line:

* **Dynamic Script Orchestration:** Utilizes `gemini-2.5-flash` to architect multi-chapter educational blueprints from simple terminal prompt inputs, avoiding token limits on long-form tutorials.
* **Contextual Media Sourcing:** Automatically extracts programmatic keyword visual tags and queries the Pexels API to pull relevant, silent stock background footage (`.mp4`).
* **Precise Word-Level Transcription:** Employs `stable-whisper` (an advanced, time-aligned wrapper around OpenAI's Whisper model) to listen to your custom voiceover (`narration.mp3`) and map spoken words to millisecond coordinates.
* **Multi-Layer Audio/Video Compositing:** Uses MoviePy (v2.0 framework architecture) to stack assets dynamically, loop background audio tracks cleanly at a muted 8% volume, mix a voice track, and burn outline-stroked subtitles directly onto the center-bottom frames.

---

## 🛠️ Project Workspace Layout

```text
├── data/
│   ├── audio/          # Drop your recorded narration.mp3 track here
│   ├── broll/          # Automated storage for downloaded silent Pexels clips
│   ├── text/           # Contains generated scripts and precise subtitles.srt timelines
│   └── output/         # Holds your ready-to-publish master video clip
├── src/
│   ├── generate_script.py    # Interfaces with Gemini API for dynamic script layouts
│   ├── download_broll.py     # Pulls semantic visual assets from Pexels API
│   ├── generate_subtitles.py # Drives Stable-Whisper local voice alignment
│   └── create_video.py       # Compiles assets using advanced MoviePy v2 rendering
├── .gitignore          # Prevents leaking private API keys or heavy media clips
└── requirements.txt    # System dependency manifest