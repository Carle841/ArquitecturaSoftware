package chainOfResponsability.java;

import chainOfResponsability.java.src.main.java.soportetecnico.SoportePrimerNivel;
import chainOfResponsability.java.src.main.java.soportetecnico.*;

public class Main {
    public static void main(String[] args) {

        SoportePrimerNivel soportePrimerNivel = new SoportePrimerNivel();
        SoporteSegundoNivel soporteSegundoNivel = new SoporteSegundoNivel();
        SoporteEspecializado soporteEspecializado = new SoporteEspecializado();

        soportePrimerNivel.establecerProximoNivel(soporteSegundoNivel);
        soporteSegundoNivel.establecerProximoNivel(soporteEspecializado);

        System.out.println(soportePrimerNivel.manejarSolicitud("necesito un reinicio"));
        System.out.println(soportePrimerNivel.manejarSolicitud("problema de hardware"));
        System.out.println(soportePrimerNivel.manejarSolicitud("problema complejo"));
        System.out.println(soportePrimerNivel.manejarSolicitud("otro problema"));
    }
}