package factoryMethod.java;

public class Report implements Document {
    @Override
    public void open() {
        System.out.println("Abriendo reporte");
    }

    @Override
    public void save() {
        System.out.println("Guardando reporte");
    }
    
}
