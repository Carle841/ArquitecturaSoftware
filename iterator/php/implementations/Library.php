<?php
class Library {
    public static function displayBooks(Iterator $iterator) {
        for ($iterator->first(); !$iterator->isDone(); $iterator->next()) {
            $book = $iterator->currentItem();
            echo "Libro: {$book->getTitle()} - Autor: {$book->getAuthor()}\n";
        }
    }
}