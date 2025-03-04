<?php
require_once 'resumeCreator.php';
require_once 'reportCreator.php';

//Cliente que usa el patron Factory Method
$resumeCreator = new resumeCreator();
$reportCreator = new reportCreator();

//Crear y usar un curriculum
echo "Creando curriculum\n";
$resume = $resumeCreator->doOperation();

echo "\nCreando reporte:\n";
$report = $reportCreator->doOperation();