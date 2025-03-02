package factoryMethod.java;

public class Main {
    public static void main(String[] args) {
        DocumentCreator resumeCreator = new ResumeCreator();
        DocumentCreator reportCreator = new ReportCreator();

        System.out.println("Creando curriculum");
        Document resume = resumeCreator.doOperation();

        System.out.println("\nCreando reporte");
        Document report = reportCreator.doOperation();
    }
}
