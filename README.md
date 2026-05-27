# Chat Simulation + Speech Pipeline

This project simulates multi-agent conversations, converts dialogue into structured data, and generates synchronized speech audio for a web-based UI.

---

# 🔧 Setup

## 1. API Configuration
Set your OpenAI API key in `oai_configuration` before running any scripts.

---

# 🚀 Pipeline Overview

## 1. Run Conversation Simulation
Generate a conversation log:


python run_negotiation_simulation.py
Output:

runs/<timestamp>/talk.json

2. Convert Log → Structured Dialogue

extracted.txt is parsed into structured JSON:

talk.json

From talk.json, each dialogue turn is processed into:

000.wav → generated speech audio (TTS)
000.json → metadata + Whisper word-level transcript

Output folder:

03_UI/voice/

4. Transcript Refinement

Refines word-level transcripts using original dialogue:

talk_voices_refined.json

Features:

punctuation restoration
improved word alignment
cleaner transcript output
🌐 Web Application (Flask UI)

A Flask-based web app provides an interactive interface for:

conversation playback
audio streaming
transcript visualization
media serving via REST API
Run server:
python app.py



✨ Features
Multi-agent conversation simulation
Automated text-to-speech pipeline
Word-level transcription (Whisper)
Punctuation restoration
Synchronized audio + text UI
Flask-based interactive frontend