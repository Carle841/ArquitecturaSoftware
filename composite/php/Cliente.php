<?php
$file1 = new File("documento1.txt", 100);
$file2 = new File("documento2.txt", 200);

$subDirectory = new Directory("Subdiretorio");
$subDirectory->add($file1);

$mainDirectory = new Directory("Diretorio Principal");
$mainDirectory->add($subDirectory);
$mainDirectory->add($file2);

echo "Tamanho total: " . $mainDirectory->getSize(); // 300