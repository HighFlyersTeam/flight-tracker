// Toggles the filter window
function toggleFilterWindow() {
    const filterWindow = document.getElementById("filter_content");
    const helpWindow = document.getElementById("help_content");
    if (window.getComputedStyle(filterWindow).display === "none") {
        filterWindow.style.display = "flex";
        helpWindow.style.display = "none";
    }
    else {
        filterWindow.style.display = "none";
    }
}

// Removes need for Shift+click in multiselect menus
$(document).on("mousedown", "option",function(e) {
    e.preventDefault();
    $(this).prop('selected', !$(this).prop('selected'));
    return false;
});

// Toggling button functionality for non-advanced options
$(document).on("click",".day_of_week_button, .airline_type_button", function() {
    if ($(this).hasClass("active")) {
        $(this).removeClass("active");
    }
    else {
        $(this).addClass("active");
    }
});

// Toggling button functionality for advanced options
$(document).on("click",".advanced_controls_button", function() {
    const start_time = document.getElementById("secondary_start_time");
    const end_time = document.getElementById("secondary_end_time");

    if ($(this).hasClass("active")) {
        $(this).removeClass("active");
        start_time.style.display = "none";
        end_time.style.display = "none";
    }
    else {
        $(".advanced_controls_button").removeClass("active");
        $(this).addClass("active");
        start_time.style.removeProperty("display");
        end_time.style.removeProperty("display");
    }
});

// Changes selection for each item in the dropdown menu
$(document).on("change", "#start_filter, #end_filter", function() {
    const target = $(this).data('target');
    const show = $("option:selected", this).data('show');
    $(target).children().addClass('hide');
    $(show).removeClass('hide');
});

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