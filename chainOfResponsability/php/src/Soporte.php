<?php
namespace SoporteTecnico;

interface Soporte {
    public function setProximoNivel(Soporte $siguiente): void;
    public function manejarSolicitud(string $solicitud): ?string;
}