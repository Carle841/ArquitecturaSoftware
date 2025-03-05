package chainOfResponsability.java.src.main.java.soportetecnico;

public class SoportePrimerNivel implements Soporte {
    private Soporte proximoNivel;

    @Override
    public void establecerProximoNivel(Soporte siguiente) {
        this.proximoNivel = siguiente;
    }

    @Override
    public String manejarSolicitud(String solicitud) {
        if (solicitud.contains("reinicio")) {
            return "Soporte Básico: Realizando reinicio de sistema";
        }

        if (proximoNivel != null) {
            return proximoNivel.manejarSolicitud(solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}
