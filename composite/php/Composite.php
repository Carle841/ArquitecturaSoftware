<?php

class Directory implements FileSystemComponent{
    private $name;
    private $components = array();

    public function __construct($name){
        $this->name = $name;
    }

    public function getName(){
        return $this->name;
    }

    public function getSize(){
        $totalSize = 0;
        foreach($this->components as $component){
            $totalSize += $component->getSize();
        }
        return $totalSize;
    }

    public function add(FileSystemComponent $component){
        $this->components[] = $component;
    }

    public function remove(FileSystemComponent $component){
        $index = array_search($component, $this->components);
        if($index !== false){
            unset($this->components[$index]);
        }
    }
}