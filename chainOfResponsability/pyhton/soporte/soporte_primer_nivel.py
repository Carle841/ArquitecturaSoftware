from soporte.soporte import Soporte

class SoportePrimerNivel(Soporte):
    def manejar_solicitud(self, solicitud):
        if "reinicio" in solicitud:
            return "Soporte Básico: Realizando reinicio de sistema"

        if self.proximo_nivel:
            return self.proximo_nivel.manejar_solicitud(solicitud)

        return "Ningún nivel de soporte puede manejar la solicitud"