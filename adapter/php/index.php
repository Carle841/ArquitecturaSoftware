<?php
require_once 'concrete/AudioPlayer.php';
use Concrete\AudioPlayer;

// Codigo cliente que usa AudioPlayer
$audioPlayer = new AudioPlayer();

echo "Probando diferentes formatos: \n";
$audioPlayer->play("mp3", "beyond the horizon.mp3");
$audioPlayer->play("mp4", "alone.mp4");
$audioPlayer->play("vlc", "far far away.vlc");
$audioPlayer->play("avi", "mind me.avi");