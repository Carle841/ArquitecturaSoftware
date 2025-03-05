<?php
require_once 'Iterator.php';
interface BookCollection {
    public function createIterator(): Iterator;
}