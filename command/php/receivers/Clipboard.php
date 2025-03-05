<?php

class Clipboard {
    private string $clipboardContent = '';

    public function setClipboard(string $content): void {
        $this->clipboardContent = $content;
    }

    public function getClipboard(): string {
        return $this->clipboardContent;
    }
}