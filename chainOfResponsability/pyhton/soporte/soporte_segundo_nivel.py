from soporte.soporte import Soporte

class SoporteSegundoNivel(Soporte):
    def manejar_solicitud(self, solicitud):
        if "hardware" in solicitud:
            return "Soporte Técnico: Diagnosticando problema de hardware"

        if self.proximo_nivel:
            return self.proximo_nivel.manejar_solicitud(solicitud)

        return "Ningún nivel de soporte puede manejar la solicitud"