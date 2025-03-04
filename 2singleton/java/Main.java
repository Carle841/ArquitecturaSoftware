package singleton.java;

public class Main {
    public static void main(String[] args) {
        // Obtener instancia del ConfigManager
        System.out.println("Obteniendo primera instancia...");
        ConfigManager configManager1 = ConfigManager.getInstance();

        // Mostrar configuraciones iniciales
        configManager1.displayConfigs();

        // Modificar una configuracion
        System.out.println("\nModificando configuracion...");
        configManager1.setConfig("db.host", "192.168.1.1");

        // Obtener otra instancia y verificar que es la misma
        System.out.println("\nObteniendo segunda instancia...");
        ConfigManager configManager2 = ConfigManager.getInstance();

        // Mostrar configuraciones desde la segunda instancia
        System.out.println("\nMostrando configuraciones desde la segunda instancia...");
        configManager2.displayConfigs();

        // Verificar que ambas instancias son iguales
        System.out.println("\nVerificando instancias: " + (configManager1 == configManager2 ? "Son la misma instancia" : "Son instancias diferentes"));

        // Modificar desde las segunda instancia
        System.out.println("\nModificando configuracion desde la segunda instancia...");
        configManager2.setConfig("app.version", "1.1");

        // Mostrar desde la primera instancia para verificar cambios
        System.out.println("\nMostrando desde la primera instancia para verificar el cambio");
        configManager1.displayConfigs();
    }
    
}