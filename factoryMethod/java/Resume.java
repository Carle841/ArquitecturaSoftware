package factoryMethod.java;

public class Resume implements Document {
    @Override
    public void open() {
        System.out.println("Abriendo curriculum");
    }

    @Override
    public void save() {
        System.out.println("Guardando curriculum");
    }
    
}
