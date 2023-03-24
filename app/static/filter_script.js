// Times are in UTC time
const DEFAULT_START = "2018-01-01T04:00:00";
const DEFAULT_END = "2018-12-31T17:00:00";

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

// Clear filter button functionality
$(document).on("click", "#clear_filter", function() {
    // Reset dates
    const start = new Date(DEFAULT_START).toISOString();
    const end = new Date(DEFAULT_END).toISOString();
    document.getElementById("start_date").value = start.substring(0, 10);
    document.getElementById("start_time").value = start.substring(11, 16);
    document.getElementById("end_date").value = end.substring(0, 10);
    document.getElementById("end_time").value = end.substring(11, 16);

    document.getElementById("start_date2").value = start.substring(0, 10);
    document.getElementById("start_time2").value = start.substring(11, 16);
    document.getElementById("end_date2").value = end.substring(0, 10);
    document.getElementById("end_time2").value = end.substring(11, 16);

    // Reset day of week buttons
    const dayOfWeekButtons = document.getElementsByClassName("day_of_week_button");
    for (let i = 0; i < dayOfWeekButtons.length; i++)
        dayOfWeekButtons[i].classList.add("active");

    // Reset multi-select menus (start location, end location, and airlines)
    $(".info option:selected").prop("selected", false);

    // Reset max layovers
    document.getElementById("max_layovers").value = 0;

    // Reset airline type buttons
    const airlineTypeButtons = document.getElementsByClassName("airline_type_button");
    for (let i = 0; i < airlineTypeButtons.length; i++)
        airlineTypeButtons[i].classList.remove("active");
});

// Filter find routes button functionality
$(document).on("click", "#find_routes_filter", function() {
    var data = {};

    // Earliest Start Time
    const departure_info = {};
    const departure_date = document.getElementById("start_date").value;
    const departure_time = document.getElementById("start_time").value;
    departure_info["date"] = departure_date;
    departure_info["time"] = departure_time;
    data["departure_info"] = departure_info;

    // Latest End Time
    const arrival_info = {};
    const arrival_date = document.getElementById("end_date").value;
    const arrival_time = document.getElementById("end_time").value;
    arrival_info["date"] = arrival_date;
    arrival_info["time"] = arrival_time;
    data["arrival_info"] = arrival_info

    // Day of Week
    const day_of_week_info = {};
    const sunday = document.getElementById("sunday_button").classList.contains("active");
    const monday = document.getElementById("monday_button").classList.contains("active");
    const tuesday = document.getElementById("tuesday_button").classList.contains("active");
    const wednesday = document.getElementById("wednesday_button").classList.contains("active");
    const thursday = document.getElementById("thursday_button").classList.contains("active");
    const friday = document.getElementById("friday_button").classList.contains("active");
    const saturday = document.getElementById("saturday_button").classList.contains("active");
    day_of_week_info["sunday"] = sunday;
    day_of_week_info["monday"] = monday;
    day_of_week_info["tuesday"] = tuesday;
    day_of_week_info["wednesday"] = wednesday;
    day_of_week_info["thursday"] = thursday;
    day_of_week_info["friday"] = friday;
    day_of_week_info["saturday"] = saturday;
    data["day_of_week"] = day_of_week_info;

    console.log(JSON.stringify(data, null, ' '));
});

// Filter cancel button functionality
$(document).on("click", "#cancel_filter", function() {
    const filterWindow = document.getElementById("filter_content");
    filterWindow.style.display = "none";
});

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
    const startTime = document.getElementById("secondary_start_time");
    const endTime = document.getElementById("secondary_end_time");

    if ($(this).hasClass("active")) {
        $(this).removeClass("active");
        startTime.style.display = "none";
        endTime.style.display = "none";
    }
    else {
        $(".advanced_controls_button").removeClass("active");
        $(this).addClass("active");
        startTime.style.removeProperty("display");
        endTime.style.removeProperty("display");
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
    // Reset the filter menu
    $('#clear_filter').trigger('click');

    // Displays the selection for the first item in the dropdown menu
    $('#start_filter').trigger('change');
    $('#end_filter').trigger('change');

    // Hide the time selection for the advanced controls
    const startTime = document.getElementById("secondary_start_time");
    const endTime = document.getElementById("secondary_end_time");
    startTime.style.display = "none";
    endTime.style.display = "none";
});