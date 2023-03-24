function toggleHelpWindow() {
    const helpWindow = document.getElementById("help_content");
    const filterWindow = document.getElementById("filter_content");
    if (window.getComputedStyle(helpWindow).display === "none") {
        helpWindow.style.display = "flex";
        filterWindow.style.display = "none";
    }
    else {
        helpWindow.style.display = "none";
    }
}
