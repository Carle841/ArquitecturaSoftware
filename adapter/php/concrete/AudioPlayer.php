<?php
namespace Concrete;

require_once 'legacy/AdvancedMediaPlayer.php';
require_once 'adapter/MediaAdapter.php';

use Interfaces\MediaPlayer;
use Adapter\MediaAdapter;

// Cliente que usa el adaptador
class AudioPlayer implements MediaPlayer{
    public function play($audioType, $fileName)
    {
        // Reproductor nativo soporta mp3
        if ($audioType == "mp3") {
            echo "Reproduciendo archivo mp3. Nombre: " . $fileName . "\n";
        } else if ($audioType == "vlc" || $audioType == "mp4") {
            $mediaAdapter = new MediaAdapter($audioType);
            $mediaAdapter->play($audioType, $fileName);
        } else {
            echo "Formato de audio no soportado\n";
        }
    }
}