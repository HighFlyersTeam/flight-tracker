function toggleFilterWindow() {
    const filterWindow = document.getElementById("filter_content");
    if (window.getComputedStyle(filterWindow).display === "none") {
        filterWindow.style.display = "flex";
    }
    else {
        filterWindow.style.display = "none";
    }
}

function toggleHelpWindow() {
    const helpWindow = document.getElementById("help_content");
    if (window.getComputedStyle(helpWindow).display === "none") {
        helpWindow.style.display = "flex";
    }
    else {
        helpWindow.style.display = "none";
    }
}