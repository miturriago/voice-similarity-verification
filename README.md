# Voice Similarity Verification

This script compares two `.gsm` audio files to determine if they belong to the same speaker, using Resemblyzer and cosine similarity.

## Installation

Install the required Python packages:

```bash
pip install resemblyzer numpy ffmpeg-python
```

## Usage

1. **Place** your two `.gsm` audio files in the root of the project folder and name them `audio1.gsm` and `audio2.gsm`.
2. **Run** the script:

   ```bash
   python verify_voice.py audio1.gsm audio2.gsm
   ```

> **Expected output:**
> ```
> Cosine similarity: 0.983
> ```

## Project Structure

```
voice-similarity-verification/
├── verify_voice.py
├── README.md
└── .gitignore
```

## .gitignore

```
__pycache__/
*.wav
venv/
.env
```

