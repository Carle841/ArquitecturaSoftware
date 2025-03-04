package facade.java.src.facade;

import facade.java.src.subsistemas.DecodicadorVideo;
import facade.java.src.subsistemas.SistemaAudio;

public class ReproductorPelicula {
    private DecodicadorVideo video;
    private SistemaAudio audio;

    public ReproductorPelicula() {
        video = new DecodicadorVideo();
        audio = new SistemaAudio();
    }

    public void reproducir(String pelicula){
        audio.iniciar();
        audio.reproducir(pelicula);
        video.reproducir(pelicula);
    }
}
