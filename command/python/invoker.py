
class Invoker:
    def __init__(self):
        self._commands = []
        self._undone_commands = []

    def execute_command(self, command):
        command.execute()
        self._commands.append(command)

    def undo(self):
        if self._commands:
            command = self._commands.pop()
            command.undo()
            self._undone_commands.append(command)

    def redo(self):
        if self._undone_commands:
            command = self._undone_commands.pop()
            command.execute()
            self._commands.append(command)