<?php
require 'vendor/autoload.php';

use SoporteTecnico\SoportePrimerNivel;
use SoporteTecnico\SoporteSegundoNivel;
use SoporteTecnico\SoporteEspecializado;

$soportePrimerNivel = new SoportePrimerNivel();
$soporteSegundoNivel = new SoporteSegundoNivel();
$soporteEspecializado = new SoporteEspecializado();

$soportePrimerNivel->setProximoNivel($soporteSegundoNivel);
$soporteSegundoNivel->setProximoNivel($soporteEspecializado);

echo $soportePrimerNivel->manejarSolicitud("necesito un reinicio") . "\n";
echo $soportePrimerNivel->manejarSolicitud("problema de hardware") . "\n";
echo $soportePrimerNivel->manejarSolicitud("problema complejo") . "\n";
echo $soportePrimerNivel->manejarSolicitud("otro problema") . "\n";