<?php
require_once('vendor/autoload.php');

use php\Facade\MoviePlayerFacade;

// Cliente
$moviePlayer = new MoviePlayerFacade();
$moviePlayer->playMovie('movie.mkv', 'audio.mp3', 'subtitles.srt');