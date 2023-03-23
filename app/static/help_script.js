function toggleHelpWindow() {
    const helpWindow = document.getElementById("help_content");
    if (window.getComputedStyle(helpWindow).display === "none") {
        helpWindow.style.display = "flex";
    }
    else {
        helpWindow.style.display = "none";
    }
}