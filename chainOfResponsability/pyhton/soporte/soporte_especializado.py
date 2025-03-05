from soporte.soporte import Soporte

class SoporteEspecializado(Soporte):
    def manejar_solicitud(self, solicitud):
        if "complejo" in solicitud:
            return "Soporte Especializado: Resolviendo problema complejo"

        if self.proximo_nivel:
            return self.proximo_nivel.manejar_solicitud(solicitud)

        return "Ningún nivel de soporte puede manejar la solicitud"