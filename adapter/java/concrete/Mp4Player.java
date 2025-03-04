package adapter.java.concrete;

import adapter.java.legacy.AdvancedMediaPlayer;

public class Mp4Player implements AdvancedMediaPlayer{
    // Implementacion concreta de Adaptee
    @Override
    public void playVlc(String fileName) {
        // No hace nada
    }

    @Override
    public void playMp4(String fileName) {
        System.out.println("Reproduciendo archivo mp4. Nombre: " + fileName);
    }
}
