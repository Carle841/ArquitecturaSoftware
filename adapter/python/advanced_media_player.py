from abc import ABC, abstractmethod

# Interfaz Adaptee
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name):
        pass
    
    @abstractmethod
    def play_mp4(self, file_name):
        pass
    
# Implementacion concreta de Adaptee para VLC
class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        print(f"Reproduciendo archivo VLC: {file_name}")
        
    def play_mp4(self, file_name):
        # No hace nada
        pass
    
# Implementacion concreta de Adaptee para MP4
class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        # No hace nada
        pass
    
    def play_mp4(self, file_name):
        print(f"Reproduciendo archivo MP4: {file_name}")