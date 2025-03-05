
class TextEditor:
    def __init__(self):
        self._content = ""

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def copy(self, text):
        print(f"Copying: {text}")

    def cut(self, text):
        print(f"Cutting: {text}")
        self._content = self._content.replace(text, '')

    def paste(self, text):
        print(f"Pasting: {text}")
        self._content += text

