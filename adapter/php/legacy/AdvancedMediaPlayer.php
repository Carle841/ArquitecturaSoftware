<?php
namespace Legacy;

// Interfaz Adaptee

interface AdvancedMediaPlayer {
    public function playVlc($fileName);
    public function playMp4($fileName);
}