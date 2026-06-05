# Chat Simulation + Speech Pipeline

This project from Fraunhofer simulates multi-agent conversations, converts dialogue into structured data, and generates synchronized speech audio for a web-based UI.

**---

### Project Structure
project-root/
│
├── 00_Beispieldateien/     # Sample input and reference data
│
├── 01_create_chat/         # Zwei agents conversation simulation module
│                            # Generates synthetic dialogue data using zwei agents
│
├── 02_Pipeline/            # Dialogue processing and speech generation pipeline
│                            # Handles text processing, transformation, and output generation
│
└── 03_UI/                  # Flask-based web application interface
                             # Provides interactive frontend for system demonstration

---



### API Configuration
Set your OpenAI API key in `oai_configuration` before running any scripts:

```python
# oai_configuration
OPENAI_API_KEY = "your-api-key-here"
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

##  Usage

### Step 1 — Run Conversation Simulation

Generates a multi-agent negotiation conversation log:

```bash
python 01_create_chat/run_negotiation_simulation.py
```

**Output:** `runs/<run_id>/talk.json`

---

### Step 2 — Convert Log → Structured Dialogue

`extracted.txt` is parsed into structured JSON (`talk.json`). Then each dialogue turn is processed via text-to-speech:

```bash
python 02_Pipeline/01_text_to_json.py
python 02_Pipeline/02_text_to_speech.py
```

**Output per dialogue turn:**

| File | Description |
|------|-------------|
| `000.wav` | Generated speech audio (TTS) |
| `000.json` | Metadata + Whisper word-level transcript |

---

### Step 3 — Transcript Refinement

Refines word-level transcripts against the original dialogue for accuracy:

```bash
python 02_Pipeline/03_fine_transcript.py
```

**Output:** `talk_voices_refined.json`

---

### Step 4 — Launch Web Application

A Flask-based UI provides an interactive interface to explore the simulated conversation and playback synchronized speech:

```bash
python 03_UI/app.py
```

Then open your browser at `http://localhost:5000`

---

## 🔄 Pipeline Overview

```
run_negotiation_simulation.py
        │
        ▼
    talk.json  ◄──  extracted.txt
        │
        ▼
  text_to_speech.py
        │
        ├──► 000.wav  (TTS audio)
        └──► 000.json (Whisper transcript)
                │
                ▼
      fine_transcript.py
                │
                ▼
  talk_voices_refined.json
                │
                ▼
           Flask UI (app.py)
```
