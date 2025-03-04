class Logger:
    # Variable de clase para almacenar la instancia
    _instance = None
    
    def __new__(cls):
        # Implementacion de Singleton en el metodo __new__
        if cls._instance is None:
            print('Creando la instancia de Logger...')
            cls._instance = super(Logger, cls).__new__(cls)
            # Inicializacion de atributos
            cls._instance.log_file = "app.log"
            cls._instance.log_level = "INFO"
        return cls._instance
    
    def log(self, message, level=None):
        level = level or self.level
        print(f"[{level}] {message} (escribiedno en {self.log_file})")
        
    def set_level(self, level):
        self.level = level
        print(f"Nivel de log cambiado a {level}")
        
    def set_log_file(self, file_path):
        self.log_file = file_path
        print(f"Archivo de log cambiado a {file_path}")
        
# Implementacion alternativa como una funcion
def get_logger():
    if not hasattr(get_logger, "_instance"):
        print('Creando la instancia de Logger (mediante funcion)...')
        get_logger._instance = Logger()
    return get_logger._instance