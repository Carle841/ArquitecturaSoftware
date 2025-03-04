<?php
require_once 'documentCreator.php';
require_once 'resume.php';

//Creador concreto para curriculum
class resumeCreator extends documentCreator {
    public function createDocument(): document {
        return new resume();
    }
}  