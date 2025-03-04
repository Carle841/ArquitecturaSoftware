from media_player import MediaPlayer
from advanced_media_player import VlcPlayer, Mp4Player

# Clase Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        self.advanced_player = None
        
        if audio_type.lower() == "vlc":
            self.advanced_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_player = Mp4Player()
            
    def play(self, audio_type, file_name):
        if audio_type.lower() == "vlc":
            self.advanced_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            self.advanced_player.play_mp4(file_name)