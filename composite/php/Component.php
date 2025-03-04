<?php

interface FileSystemComponent{
    public function getName();
    public function getSize();
    public function add(FileSystemComponent $component);
    public function remove(FileSystemComponent $component);
}