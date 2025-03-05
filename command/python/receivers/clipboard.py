
class Clipboard:
    def __init__(self):
        self._clipboard_content = ""

    def set_clipboard(self, content):
        self._clipboard_content = content

    def get_clipboard(self):
        return self._clipboard_content