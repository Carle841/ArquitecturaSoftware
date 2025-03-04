package facade.java.src.subsistemas;

public class SistemaAudio {
    public void iniciar() {
        System.out.println("Sistema de audio activado...");
    }

    public void reproducir(String pelicula) {
        System.out.println("Reproduciendo audio de: " + pelicula);
    }
}
