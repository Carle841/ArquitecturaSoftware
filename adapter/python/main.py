from media_player import AudioPlayer

# Codigo cliente que usa Audio Player
audio_player = AudioPlayer()

print("Probando diferentes formatos: ")
audio_player.play("mp3", "beyond the horizon.mp3")
audio_player.play("mp4", "alone.mp4")
audio_player.play("vlc", "far far away.vlc")
audio_player.play("avi", "mind me.avi")