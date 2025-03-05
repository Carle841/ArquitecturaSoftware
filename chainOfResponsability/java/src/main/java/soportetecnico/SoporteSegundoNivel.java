package chainOfResponsability.java.src.main.java.soportetecnico;

public class SoporteSegundoNivel implements Soporte {
    private Soporte proximoNivel;

    @Override
    public void establecerProximoNivel(Soporte siguiente) {
        this.proximoNivel = siguiente;
    }

    @Override
    public String manejarSolicitud(String solicitud) {
        if (solicitud.contains("hardware")) {
            return "Soporte Técnico: Diagnosticando problema de hardware";
        }

        if (proximoNivel != null) {
            return proximoNivel.manejarSolicitud(solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}
