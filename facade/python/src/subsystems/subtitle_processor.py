from typing import Optional

class SubtitleProcessor:
    
    def __init__(self, subtitle_format: Optional[str] = None):
        self.subtitle_format = subtitle_format or "srt"
    
    def load_subtitles(self, subtitle_path: str) -> None:
        print(f"Cargando subtítulos desde: {subtitle_path} (Formato: {self.subtitle_format})")
    
    def render_subtitles(self) -> None:
        print("Renderizando subtítulos")