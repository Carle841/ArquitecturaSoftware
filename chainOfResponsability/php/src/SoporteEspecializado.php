<?php
namespace SoporteTecnico;

class SoporteEspecializado implements Soporte {
    private ?Soporte $proximoNivel = null;

    public function setProximoNivel(Soporte $siguiente): void {
        $this->proximoNivel = $siguiente;
    }

    public function manejarSolicitud(string $solicitud): ?string {
        if (strpos($solicitud, 'complejo') !== false) {
            return "Soporte Especializado: Resolviendo problema complejo";
        }

        if ($this->proximoNivel !== null) {
            return $this->proximoNivel->manejarSolicitud($solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}