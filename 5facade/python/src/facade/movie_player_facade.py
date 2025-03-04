from src.subsystems.video_decoder import VideoDecoder
from src.subsystems.audio_system import AudioSystem
from src.subsystems.subtitle_processor import SubtitleProcessor

class MoviePlayerFacade:
    
    def __init__(self):
        self.video_decoder = VideoDecoder()
        self.audio_system = AudioSystem()
        self.subtitle_processor = SubtitleProcessor()
    
    def play_movie(self, movie_path: str, subtitle_path: str) -> None:
        
        # Initialize subsystems
        self.video_decoder.initialize_decoder()
        self.audio_system.initialize_audio()
        
        # Decode and play video
        self.video_decoder.decode_video(movie_path)
        self.audio_system.play_audio(movie_path)
        
        # Process subtitles if provided
        if subtitle_path:
            self.subtitle_processor.load_subtitles(subtitle_path)
            self.subtitle_processor.render_subtitles()
        
        print("Reproducción de película completada")