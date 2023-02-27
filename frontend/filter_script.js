function toggleFilterWindow() {
    const filterWindow = document.getElementById("filter_content");
    if (window.getComputedStyle(filterWindow).display === "none") {
        filterWindow.style.display = "block";
    }
    else {
        filterWindow.style.display = "none";
    }
}