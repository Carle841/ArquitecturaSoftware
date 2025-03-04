from typing import Optional

class VideoDecoder:
    
    def __init__(self, codec: Optional[str] = None):
        self.codec = codec or "default"
    
    def initialize_decoder(self) -> None:
        print(f"Inicializando decodificador de video con codec: {self.codec}")
    
    def decode_video(self, video_path: str) -> None:
        print(f"Decodificando video desde: {video_path}")