<?php

interface Iterator {
    public function first();
    public function next();
    public function isDone(): bool;
    public function currentItem(): ?Book;
}

