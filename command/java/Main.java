package command.java;

import command.java.commands.CopyCommand;
import command.java.receivers.Clipboard;
import command.java.receivers.TextEditor;

public class Main {
    public static void main(String[] args) {
        TextEditor textEditor = new TextEditor();
        Clipboard clipboard = new Clipboard();
        Invoker invoker = new Invoker();

        textEditor.setContent("Hello World");

        // Crear y ejecutar comandos
        CopyCommand copyCommand = new CopyCommand(textEditor, clipboard, "Hello");
        invoker.executeCommand(copyCommand);

        System.out.println("Clipboard content: " + clipboard.getClipboard());

        // Deshacer el comando
        invoker.undo();
        System.out.println("After undo - Clipboard content: " + clipboard.getClipboard());
    }
}
