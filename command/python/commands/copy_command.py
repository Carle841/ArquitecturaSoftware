
from interfaces.command import Command

class CopyCommand(Command):
    def __init__(self, text_editor, clipboard, text_to_copy):
        self._text_editor = text_editor
        self._clipboard = clipboard
        self._text_to_copy = text_to_copy
        self._previous_clipboard_content = ""

    def execute(self):
        self._previous_clipboard_content = self._clipboard.get_clipboard()
        self._text_editor.copy(self._text_to_copy)
        self._clipboard.set_clipboard(self._text_to_copy)

    def undo(self):
        self._clipboard.set_clipboard(self._previous_clipboard_content)

# Implementaciones similares para cut_command.py y paste_command.py