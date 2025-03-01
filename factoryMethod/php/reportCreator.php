<?php
require_once 'documentCreator.php';
require_once 'report.php';

// Creador concreto para reporte
class reportCreator extends documentCreator {
    public function createDocument(): document {
        return new report();
    }
}