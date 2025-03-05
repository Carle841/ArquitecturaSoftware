package command.java;

import java.util.ArrayList;
import java.util.List;

import command.java.interfaces.Command;

public class Invoker {
    private List<Command> commands = new ArrayList<>();
    private List<Command> undoneCommands = new ArrayList<>();

    public void executeCommand(Command command) {
        command.execute();
        commands.add(command);
    }

    public void undo() {
        if (!commands.isEmpty()) {
            Command command = commands.remove(commands.size() - 1);
            command.undo();
            undoneCommands.add(command);
        }
    }

    public void redo() {
        if (!undoneCommands.isEmpty()) {
            Command command = undoneCommands.remove(undoneCommands.size() - 1);
            command.execute();
            commands.add(command);
        }
    }
}
