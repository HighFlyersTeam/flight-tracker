function toggleFilterWindow() {
    const window = document.getElementById("filter_content");
    if (window.style.display === "none") {
        window.style.display = "block";
    }
    else {
        window.style.display = "none";
    }
}