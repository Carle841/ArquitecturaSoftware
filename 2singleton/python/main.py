from logger import Logger, get_logger

# Usando la clase Singleton
print("Creando primer logger...")
logger1 = Logger()
logger1.log("Este es un mensaje del primer logger")

print("\nCreando segundo logger...")
logger2 = Logger()
logger2.log("Este es un mensaje del segundo logger")

# Cambiando configuracion en un logger y verificando que afecta a ambos
print("\nCambiando configuracion")
logger1.set_level("DEBUG")
logger1.set_log_file("debug.log")

print("\nVerificando cambios en el segundo logger")
logger2.log("Este mensaje deberia estar en nivel DEBUG y en debug.log")

# Verificar que son la misma instancia
print("\nVerificando instancias: ", "Misma instancia" if logger1 is logger2 else "Instancias diferentes")

# Usando la implementacion alternativa
print("\nUsando implementacion alternativa...")
logger3 = get_logger()
logger3.log("Este mensaje es del logger 3 (debe ser el mismo que los anteriores)")

print("\nVerificando instancia alternativa: ", "Misma instancia" if logger1 is logger3 else "Instancias diferentes")