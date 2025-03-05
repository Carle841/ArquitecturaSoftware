package command.java.receivers;


public class TextEditor {
    private String content = "";

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void copy(String text) {
        System.out.println("Copying: " + text);
    }

    public void cut(String text) {
        System.out.println("Cutting: " + text);
        content = content.replace(text, "");
    }

    public void paste(String text) {
        System.out.println("Pasting: " + text);
        content += text;
    }
}

