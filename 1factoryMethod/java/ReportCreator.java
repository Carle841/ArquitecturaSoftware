package factoryMethod.java;

public class ReportCreator extends DocumentCreator {
    @Override
    public Document createDocument() {
        return new Report();
    }
    
}
