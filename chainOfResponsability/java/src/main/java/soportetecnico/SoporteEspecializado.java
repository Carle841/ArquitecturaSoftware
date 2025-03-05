package chainOfResponsability.java.src.main.java.soportetecnico;

public class SoporteEspecializado implements Soporte {
    private Soporte proximoNivel;

    @Override
    public void establecerProximoNivel(Soporte siguiente) {
        this.proximoNivel = siguiente;
    }

    @Override
    public String manejarSolicitud(String solicitud) {
        if (solicitud.contains("complejo")) {
            return "Soporte Especializado: Resolviendo problema complejo";
        }

        if (proximoNivel != null) {
            return proximoNivel.manejarSolicitud(solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}
