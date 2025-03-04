package adapter.java.concrete;

import adapter.java.legacy.AdvancedMediaPlayer;

public class VlcPlayer implements AdvancedMediaPlayer{
    @Override
    public void playVlc(String fileName) {
        System.out.println("Reproduciendo archivo vlc. Nombre: " + fileName);
    }

    @Override
    public void playMp4(String fileName) {
        // No hace nada
    }
}
