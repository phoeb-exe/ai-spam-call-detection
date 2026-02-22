import torch
import librosa
import tempfile
import soundfile as sf
import os
from qwen_asr import Qwen3ASRModel


class ASRModel:
    def __init__(self):
        self.model = Qwen3ASRModel.from_pretrained(
            "Qwen/Qwen3-ASR-0.6B",
            dtype=torch.float32,
            device_map="cpu",   
        )

    def _trim_audio(self, file, max_seconds=30):
        audio, sr = librosa.load(file, sr=16000)

        max_samples = sr * max_seconds
        audio_trimmed = audio[:max_samples]

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

        sf.write(temp_file.name, audio_trimmed, sr)

        return temp_file.name

    def transcribe(self, file, language="English"):
        trimmed_path = self._trim_audio(file, max_seconds=30)

        result = self.model.transcribe(
            audio=trimmed_path,
            language=language
        )

        os.remove(trimmed_path)

        return result[0].text
