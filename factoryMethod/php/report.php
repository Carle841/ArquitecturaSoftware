<?php
require_once 'document.php';

//Otra implementacion concreta de document
class report implements Document {
    public function open() {
        echo 'Abriendo reporte\n';
    }

    public function save() {
        echo 'Guardando reporte\n';
    }
}