#!/bin/bash

echo "📁 Creating pristine folder architecture..."
mkdir -p src
mkdir -p data

echo "📝 Building requirements.txt..."
cat << 'EOF' > requirements.txt
google-genai
openai-whisper
requests
moviepy
EOF

echo "🔐 Generating .env configuration template..."
cat << 'EOF' > .env
GEMINI_API_KEY=your_api_key_here
OUTPUT_FORMAT=mp4
EOF

echo "🙈 Writing .gitignore to protect local credentials..."
cat << 'EOF' > .gitignore
.env
.venv/
__pycache__/
*.pyc
data/*
!data/.gitkeep
EOF

touch data/.gitkeep

echo "🌿 Initializing local Git repository..."
git init -q

echo "⚙️ Creating Python Virtual Environment (.venv)..."
python3 -m venv .venv

echo "✅ Success! Everything (including your .gitignore) is ready."