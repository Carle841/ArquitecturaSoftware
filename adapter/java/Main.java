package adapter.java;

import adapter.java.concrete.AudioPlayer;


// Codigo cliente que usa AudioPlayer
public class Main {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();

        System.out.println("Probando diferentes formatos: ");
        audioPlayer.play("mp3", "cancion.mp3");
        audioPlayer.play("mp4", "video.mp4");
        audioPlayer.play("vlc", "pelicula.vlc");
        audioPlayer.play("avi", "video.avi");
    }
}
