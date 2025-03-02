package factoryMethod.java;

public abstract class DocumentCreator {
    public abstract Document createDocument();

    // Operacion que usa el factory method
    public Document doOperation() {
        Document document = createDocument();
        document.open();
        document.save();
        return document;
    }
}
