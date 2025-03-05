from soporte.soporte_primer_nivel import SoportePrimerNivel
from soporte.soporte_segundo_nivel import SoporteSegundoNivel
from soporte.soporte_especializado import SoporteEspecializado

def main():
    soporte_primer_nivel = SoportePrimerNivel()
    soporte_segundo_nivel = SoporteSegundoNivel()
    soporte_especializado = SoporteEspecializado()

    soporte_primer_nivel.establecer_proximo_nivel(soporte_segundo_nivel)
    soporte_segundo_nivel.establecer_proximo_nivel(soporte_especializado)

    print(soporte_primer_nivel.manejar_solicitud("necesito un reinicio"))
    print(soporte_primer_nivel.manejar_solicitud("problema de hardware"))
    print(soporte_primer_nivel.manejar_solicitud("problema complejo"))
    print(soporte_primer_nivel.manejar_solicitud("otro problema"))

if __name__ == "__main__":
    main()