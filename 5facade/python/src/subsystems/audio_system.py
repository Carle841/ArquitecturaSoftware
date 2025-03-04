from typing import Optional

class AudioSystem:
    
    def __init__(self, volume: Optional[int] = None):
        self.volume = volume or 50  # Default volume at 50%
    
    def initialize_audio(self) -> None:
        print(f"Inicializando sistema de audio (Volumen: {self.volume}%)")
    
    def play_audio(self, audio_path: str) -> None:
        print(f"Reproduciendo audio desde: {audio_path}")