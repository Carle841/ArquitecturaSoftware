<?php

class SMSSubscriber implements Observer {
    private $phoneNumber;

    public function __construct($phoneNumber) {
        $this->phoneNumber = $phoneNumber;
    }

    public function update($news) {
        echo "Enviando SMS al {$this->phoneNumber}: Noticias - {$news}\n";
    }
}