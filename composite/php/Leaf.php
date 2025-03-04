<?php

class File implements FileSystemComponent{
    private $name;
    private $size;

    public function __construct($name, $size){
        $this->name = $name;
        $this->size = $size;
    }

    public function getName(){
        return $this->name;
    }

    public function getSize(){
        return $this->size;
    }

    public function add(FileSystemComponent $component){
        throw new Exception("Cannot add to a file");
    }

    public function remove(FileSystemComponent $component){
        throw new Exception("Cannot remove from a file");
    }
}