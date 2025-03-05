<?php

class EmailSubscriber implements Observer {
    private $email;

    public function __construct($email) {
        $this->email = $email;
    }

    public function update($news) {
        echo "Enviando email a {$this->email}: Noticias - {$news}\n";
    }
}