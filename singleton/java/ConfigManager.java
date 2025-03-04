package singleton.java;
import java.util.HashMap;
import java.util.Map;

public class ConfigManager {
    // Instancia estatica unica
    private static ConfigManager instance;

    // Configuraciones almacenadas
    private Map<String, String> configs;

    // Constructor privado
    private ConfigManager() {
        configs = new HashMap<>();
        System.out.println("Inicializando ConfigManager");
        // Cargar configuraciones por defecto
        configs.put("app.name", "MyApp");
        configs.put("app.version", "1.0");
        configs.put("db.host", "localhost");
    }

    // Metodo estatico sincronizado para obtener la instancia
    // Implementacion con inicializacion perezosa thread-safe
    public static synchronized ConfigManager getInstance() {
        if (instance == null) {
            instance = new ConfigManager();
        }
        return instance;
    }

    // Variante con Double-Checked Locking (mas eficiente)
    /*
     * public static ConfigManager getInstance() { 
     *  if (instance == null) { 
     *      synchronized (ConfigManager.class) { 
     *          if (instance == null) { 
     *              instance = new ConfigManager(); 
     *          } 
     *      } 
     *  } 
     *  return instance; 
     * }
     */

     // Inicializacion temprana (thread-safe sin sincronizacion)
    /*
     * private static ConfigManager instance = new ConfigManager();
     * 
     * public static ConfigManager getInstance() { 
     *  return instance; 
     * }
     */

     // Metodo para obtener una configuracion
    public String getConfig(String key) {
        return configs.get(key);
    }

    // Metodo para establecer una configuracion
    public void setConfig(String key, String value) {
        configs.put(key, value);
        System.out.println("Configuracion actualizada: " + key + " = " + value);
    }

    // Metodo para mostrar todas las configuraciones
    public void displayConfigs() {
        System.out.println("Configuraciones actuales:");
        for (String key : configs.keySet()) {
            System.out.println(key + " = " + configs.get(key));
        }
    }
}
