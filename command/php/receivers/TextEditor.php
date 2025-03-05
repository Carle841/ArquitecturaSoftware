<?php
// receivers/TextEditor.php
class TextEditor {
    private string $content = '';

    public function getContent(): string {
        return $this->content;
    }

    public function setContent(string $content): void {
        $this->content = $content;
    }

    public function copy(string $text): void {
        echo "Copiando: $text\n";
    }

    public function cut(string $text): void {
        echo "Cortando: $text\n";
        $this->content = str_replace($text, '', $this->content);
    }

    public function paste(string $text): void {
        echo "Pegando: $text\n";
        $this->content .= $text;
    }
}
