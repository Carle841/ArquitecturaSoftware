<?php
require_once __DIR__ . '/implementations/PhysicalBook.php';
require_once __DIR__ . '/implementations/PhysicalBookIterator.php';
require_once __DIR__ . '/implementations/PhysicalBookCollection.php';
require_once __DIR__ . '/implementations/Library.php';

$collection = new PhysicalBookCollection();
$collection->addBook(new PhysicalBook("Don Quijote", "Miguel de Cervantes"));
$collection->addBook(new PhysicalBook("Cien Años de Soledad", "Gabriel García Márquez"));

$iterator = $collection->createIterator();
Library::displayBooks($iterator);