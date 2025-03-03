<?php
require_once 'DatabaseConnection.php';

// Obtenemos la instancia del Singleton
$db1 = DatabaseConnection::getInstance();
echo "Realizando primera consulta...\n";
$result1 = $db1->query("SELECT * FROM users");

echo "\n";

// Obtebemos otra "instancia" (realmente es la misma)
$db2 = DatabaseConnection::getInstance();
echo "Realizando segunda consulta...\n";
$result2 = $db2->query("SELECT * FROM products");

//Verificar que son la misma instancia
echo "\nVerificando instancias: " . ($db1 === $db2 ? "Son la misma instancia" : "No son la misma instancia") . "\n";