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
    console.log(start_time.style.display);
    if (start_time.style.display === "none") {
        console.log("true");
        start_time.style.removeProperty("display");
        end_time.style.removeProperty("display");
    }
    else {
        console.log("false");
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