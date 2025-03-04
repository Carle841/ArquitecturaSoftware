from abc import ABC, abstractmethod

# Interfaz Target
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type, file_name):
        pass
    
# Cliente que usa el adaptador
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        # Reproductor nativo soporta mp3
        if audio_type.lower() == "mp3":
            print(f"Reproduciendo archivo mp3: {file_name}")
            
        #Para otros formatos, usa el adaptador
        elif audio_type.lower() in ["vlc", "mp4"]:
            from media_adapter import MediaAdapter
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
            
        else:
            print(f"Formato no soportado: {audio_type}")