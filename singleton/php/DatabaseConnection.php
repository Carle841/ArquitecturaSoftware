<?php
class DatabaseConnection{
    // Instancia unica
    private static $instance = null;

    // Configuracion de la conexion
    private $host;
    private $username;
    private $password;
    private $database;
    private $connection;

    // Constructor privado
    private function __construct(){
        // Valores por defecto o cargados desde configuracion
        $this->host = 'localhost';
        $this->username = 'root';
        $this->password = 'password';
        $this->database = 'mydb';

        // Simular conexion
        echo "Conectando a la base de datos {$this->database} en {$this->host} con el usuario {$this->username} y la contraseña {$this->password}.\n";
        $this->connection = "Conexion a BD simulada";
    }

    // Metodo para obtener la instancia
    public static function getInstance(){
        if(self::$instance == null){
            self::$instance = new self();
        }
        return self::$instance;
    }

    // Evitar clonar la instancia
    private function __clone(){}

    // Evitar deserializacion
    private function __wakeup(){}

    // Metodo para consultas
    public function query($sql){
        echo "Ejecutando consulta: {$sql}\n";
        return "Resultados simulados para: {$sql}\n";
    }

    // Obtener la conexion
    public function getConnection(){
        return $this->connection;
    }
}