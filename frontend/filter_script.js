// Toggles the filter window
function toggleFilterWindow() {
    const filterWindow = document.getElementById("filter_content");
    if (window.getComputedStyle(filterWindow).display === "none") {
        filterWindow.style.display = "flex";
    }
    else {
        filterWindow.style.display = "none";
    }
}

// Changes selection for each item in the dropdown menu
$(document).on("change", "#start_filter", function() {
    var target = $(this).data('target');
    var show = $("option:selected", this).data('show');
    $(target).children().addClass('hide');
    $(show).removeClass('hide');
});

// Displays the selection for the first item in the dropdown menu
$(function(){
    $('#start_filter').trigger('change');
});