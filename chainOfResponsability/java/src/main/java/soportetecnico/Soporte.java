package chainOfResponsability.java.src.main.java.soportetecnico;

public interface Soporte {
    void establecerProximoNivel(Soporte siguiente);
    String manejarSolicitud(String solicitud);
}
