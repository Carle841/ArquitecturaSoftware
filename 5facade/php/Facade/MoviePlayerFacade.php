<?php
namespace php\Facade;

use php\Subsystems\VideoDecoder;
use php\Subsystems\AudioSystem;
use php\Subsystems\SubtitleProcessor;

class MoviePlayerFacade{
    private $videoDecoder;
    private $audioSystem;
    private $subtitleProcessor;

    public function __construct(){
        
        $this->videoDecoder = new VideoDecoder();
        $this->audioSystem = new AudioSystem();
        $this->subtitleProcessor = new SubtitleProcessor();
    }

    public function playMovie($moviePath, $audioPath, $subtitlesPath){
        // Coordinacion de subsistemas
        $this->videoDecoder->initializeDecoder();
        $this->videoDecoder->decodeVideo($moviePath);

        $this->audioSystem->initializeAudio();
        $this->audioSystem->playAudio($audioPath);

        $this->subtitleProcessor->loadSubtitles();
        $this->subtitleProcessor->renderSubtitles($subtitlesPath);

        echo "Reproduciendo película completa: $moviePath\n";
    }
}