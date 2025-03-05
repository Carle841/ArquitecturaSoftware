<?php


class CopyCommand implements Command {
    private TextEditor $textEditor;
    private Clipboard $clipboard;
    private string $textToCopy;

    public function __construct(TextEditor $textEditor, Clipboard $clipboard, string $textToCopy) {
        $this->textEditor = $textEditor;
        $this->clipboard = $clipboard;
        $this->textToCopy = $textToCopy;
    }

    public function execute(): void {
        $this->textEditor->copy($this->textToCopy);
        $this->clipboard->setClipboard($this->textToCopy);
    }

    public function undo(): void {
        $this->clipboard->setClipboard('');
    }
}

// Implementaciones similares para CutCommand y PasteCommand