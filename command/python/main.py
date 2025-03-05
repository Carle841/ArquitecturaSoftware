
from receivers.text_editor import TextEditor
from receivers.clipboard import Clipboard
from commands.copy_command import CopyCommand
from invoker import Invoker

def main():
    text_editor = TextEditor()
    clipboard = Clipboard()
    invoker = Invoker()

    text_editor.set_content("Hello World")

    # Crear y ejecutar comandos
    copy_command = CopyCommand(text_editor, clipboard, "Hello")
    invoker.execute_command(copy_command)

    print("Clipboard content:", clipboard.get_clipboard())

    # Deshacer el comando
    invoker.undo()
    print("After undo - Clipboard content:", clipboard.get_clipboard())

if __name__ == "__main__":
    main()