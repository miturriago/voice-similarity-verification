# verify_voice.py

from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import ffmpeg
import sys

def gsm_to_wav(input_path, output_path):
    (
        ffmpeg
        .input(input_path)
        .output(output_path, ar=16000, ac=1)
        .overwrite_output()
        .run(quiet=True)
    )

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python verify_voice.py audio1.gsm audio2.gsm")
        sys.exit(1)
    a1, a2 = sys.argv[1], sys.argv[2]
    w1, w2 = "a1.wav", "a2.wav"
    gsm_to_wav(a1, w1)
    gsm_to_wav(a2, w2)
    wav1 = preprocess_wav(w1)
    wav2 = preprocess_wav(w2)
    enc = VoiceEncoder()
    emb1 = enc.embed_utterance(wav1)
    emb2 = enc.embed_utterance(wav2)
    cos_sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1)*np.linalg.norm(emb2))
    print(f"Similitud coseno: {cos_sim:.3f}")