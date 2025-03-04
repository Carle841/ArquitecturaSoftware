package composite.java;

interface FileSystemComponent {
    String getName();
    int getSize();
    void add(FileSystemComponent component);
    void remove(FileSystemComponent component);
}
