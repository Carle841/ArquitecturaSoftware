package composite.java;

public class Cliente {
    public static void main(String[] args) {
        File file1 = new File("documento1.txt", 100);
        File file2 = new File("documento2.txt", 200);

        Directory subDirectory = new Directory("Subdirectorio");
        subDirectory.add(file1);

        Directory mainDirectory = new Directory("Directorio Principal");
        mainDirectory.add(subDirectory);
        mainDirectory.add(file2);

        System.out.println("Tamaño total: " + mainDirectory.getSize()); // 300
    }
}