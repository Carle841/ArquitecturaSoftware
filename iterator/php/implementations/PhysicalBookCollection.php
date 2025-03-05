<?php

class PhysicalBookCollection implements BookCollection {
    private array $books = [];

    public function addBook(Book $book) {
        $this->books[] = $book;
    }

    public function createIterator(): Iterator {
        return new PhysicalBookIterator($this->books);
    }
}

