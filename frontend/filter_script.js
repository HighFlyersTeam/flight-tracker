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

// Toggling button functionality for non-advanced options
$(document).on("click",".day_of_week_button, .airline_type_button", function() {
    if ($(this).hasClass("active")) {
        $(this).removeClass("active");
    }
    else {
        $(this).addClass("active");
    }
});

// Changes selection for each item in the dropdown menu
$(document).on("change", "#start_filter, #end_filter", function() {
    const target = $(this).data('target');
    const show = $("option:selected", this).data('show');
    $(target).children().addClass('hide');
    $(show).removeClass('hide');
});

// Toggles the time selection for the advanced controls
function advanced_controls_time_display() {
    const start_time = document.getElementById("secondary_start_time");
    const end_time = document.getElementById("secondary_end_time");
    if (start_time.style.display === "none") {
        start_time.style.removeProperty("display");
        end_time.style.removeProperty("display");
    }
    else {
        start_time.style.display = "none";
        end_time.style.display = "none";
    }
}

// Triggers on start of the webpage creation
$(function(){
    // Displays the selection for the first item in the dropdown menu
    $('#start_filter').trigger('change');
    $('#end_filter').trigger('change');

    // Hide the time selection for the advanced controls
    const start_time = document.getElementById("secondary_start_time");
    const end_time = document.getElementById("secondary_end_time");
    start_time.style.display = "none";
    end_time.style.display = "none";
});