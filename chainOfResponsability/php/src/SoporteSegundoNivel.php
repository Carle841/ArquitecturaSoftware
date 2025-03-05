<?php
namespace SoporteTecnico;

class SoporteSegundoNivel implements Soporte {
    private ?Soporte $proximoNivel = null;

    public function setProximoNivel(Soporte $siguiente): void {
        $this->proximoNivel = $siguiente;
    }

    public function manejarSolicitud(string $solicitud): ?string {
        if (strpos($solicitud, 'hardware') !== false) {
            return "Soporte Técnico: Diagnosticando problema de hardware";
        }

        if ($this->proximoNivel !== null) {
            return $this->proximoNivel->manejarSolicitud($solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}