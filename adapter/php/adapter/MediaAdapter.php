<?php
namespace Adapter;

require_once 'interfaces/MediaPlayer.php';
require_once 'legacy/AdvancedMediaPlayer.php';
require_once 'concrete/VlcPlayer.php';
require_once 'concrete/Mp4Player.php';

use Interfaces\MediaPlayer;
use Legacy\AdvancedMediaPlayer;
use Concrete\VlcPlayer;
use Concrete\Mp4Player;

// Clase Adapter
class MediaAdapter implements MediaPlayer {
    private $advancedMediaPlayer;

    public function __construct($audioType) {
        if ($audioType == "vlc") {
            $this->advancedMediaPlayer = new VlcPlayer();
        } else if ($audioType == "mp4") {
            $this->advancedMediaPlayer = new Mp4Player();
        }
    }

    public function play($audioType, $fileName)
    {
        if ($audioType == "vlc") {
            $this->advancedMediaPlayer->playVlc($fileName);
        } else if ($audioType == "mp4") {
            $this->advancedMediaPlayer->playMp4($fileName);
        }
    }
}