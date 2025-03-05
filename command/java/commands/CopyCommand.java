package command.java.commands;

import command.java.interfaces.Command;
import command.java.receivers.Clipboard;
import command.java.receivers.TextEditor;

// CopyCommand.java
public class CopyCommand implements Command {
    private TextEditor textEditor;
    private Clipboard clipboard;
    private String textToCopy;
    private String previousClipboardContent;

    public CopyCommand(TextEditor textEditor, Clipboard clipboard, String textToCopy) {
        this.textEditor = textEditor;
        this.clipboard = clipboard;
        this.textToCopy = textToCopy;
    }

    @Override
    public void execute() {
        previousClipboardContent = clipboard.getClipboard();
        textEditor.copy(textToCopy);
        clipboard.setClipboard(textToCopy);
    }

    @Override
    public void undo() {
        clipboard.setClipboard(previousClipboardContent);
    }
}

// Implementaciones similares para CutCommand y PasteCommand