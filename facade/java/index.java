package facade.java;

import facade.java.src.facade.ReproductorPelicula;

public class index {
    public static void main(String[] args) {
        ReproductorPelicula reproductor = new ReproductorPelicula();
        reproductor.reproducir("The Lord of the Rings.mp4");
    }
}
