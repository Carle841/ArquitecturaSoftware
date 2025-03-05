<?php

class PhysicalBookIterator implements Iterator {
    private array $books;
    private int $position = 0;

    public function __construct(array $books) {
        $this->books = $books;
    }

    public function first() {
        $this->position = 0;
        return $this->currentItem();
    }

    public function next() {
        $this->position++;
    }

    public function isDone(): bool {
        return $this->position >= count($this->books);
    }

    public function currentItem(): ?Book {
        return $this->isDone() ? null : $this->books[$this->position];
    }
}

