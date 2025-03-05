<?php

class Invoker {
    private array $commands = [];
    private array $undoneCommands = [];

    public function executeCommand(Command $command): void {
        $command->execute();
        $this->commands[] = $command;
    }

    public function undo(): void {
        if (!empty($this->commands)) {
            $command = array_pop($this->commands);
            $command->undo();
            $this->undoneCommands[] = $command;
        }
    }

    public function redo(): void {
        if (!empty($this->undoneCommands)) {
            $command = array_pop($this->undoneCommands);
            $command->execute();
            $this->commands[] = $command;
        }
    }
}