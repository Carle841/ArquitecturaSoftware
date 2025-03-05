<?php
namespace SoporteTecnico;
require_once('Soporte.php');

use SoporteTecnico\Soporte;

class SoportePrimerNivel implements Soporte {
    private ?Soporte $proximoNivel = null;

    public function setProximoNivel(Soporte $siguiente): void {
        $this->proximoNivel = $siguiente;
    }

    public function manejarSolicitud(string $solicitud): ?string {
        if (strpos($solicitud, 'reinicio') !== false) {
            return "Soporte Básico: Realizando reinicio de sistema";
        }

        if ($this->proximoNivel !== null) {
            return $this->proximoNivel->manejarSolicitud($solicitud);
        }

        return "Ningún nivel de soporte puede manejar la solicitud";
    }
}
?>