<?php
namespace Concrete;

require_once 'legacy/AdvancedMediaPlayer.php';
use Legacy\AdvancedMediaPlayer;

// Implementacion concreta de Adaptee
class VlcPlayer implements AdvancedMediaPlayer {
    public function playVlc($fileName) {
        echo "Reproduciendo archivo vlc. Nombre: " . $fileName . "\n";
    }
    public function playMp4($fileName) {
        // no hace nada
    }
}