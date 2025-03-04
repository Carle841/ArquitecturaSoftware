package adapter.java.concrete;

import adapter.java.interfaces.MediaPlayer;
import adapter.java.adapter.MediaAdapter;


// Cliente que usa el adaptador
public class AudioPlayer implements MediaPlayer{
    @Override
    public void play(String audioType, String fileName) {
        // Reproducir archivos mp3
        if(audioType.equalsIgnoreCase("mp3")){
            System.out.println("Reproduciendo archivo mp3. Nombre: " + fileName);
        } 
        // Reproducir archivos mp4 y vlc
        else if(audioType.equalsIgnoreCase("mp4") || audioType.equalsIgnoreCase("vlc")){
            MediaAdapter mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        } 
        // No se puede reproducir el archivo
        else{
            System.out.println("Formato de archivo no soportado: " + audioType);
        }
    }
}
