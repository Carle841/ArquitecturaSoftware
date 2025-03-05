package command.java.receivers;

public class Clipboard {
    private String clipboardContent = "";

    public void setClipboard(String content) {
        this.clipboardContent = content;
    }

    public String getClipboard() {
        return clipboardContent;
    }
}
