<?php
namespace Concrete;

require_once 'legacy/AdvancedMediaPlayer.php';
use Legacy\AdvancedMediaPlayer;

//Implementacion concreta de Adaptee
class Mp4Player implements AdvancedMediaPlayer {
    public function playVlc($fileName) {
        // no hace nada
    }
    public function playMp4($fileName) {
        echo "Reproduciendo archivo mp4. Nombre: " . $fileName . "\n";
    }
}