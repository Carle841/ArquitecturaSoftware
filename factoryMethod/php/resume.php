<?php
require_once 'document.php';

//Implementacion concreta de document
class Resume implements Document {
    public function open() {
        echo 'Abriendo curriculum\n';
    }

    public function save() {
        echo 'Guardando curriculum\n';
    }
}