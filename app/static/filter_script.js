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

// Changing the start location type
let startLocationTypeSelect;
let startAirportSelect;
let startCountrySelect;
let startContinentSelect;

function changeStartLocationType() {
    const locationType = startLocationTypeSelect.value;

    startAirportSelect.style.display = "none";
    startCountrySelect.style.display = "none";
    startContinentSelect.style.display = "none";

    if (locationType === "airport") {
        startAirportSelect.style.display = "block";
    } else if (locationType === "country") {
        startCountrySelect.style.display = "block";
    } else if (locationType === "continent") {
        startContinentSelect.style.display = "block";
    }
}

function resetStartLocation() {
    startLocationTypeSelect.value = "airport";
    changeStartLocationType();
}

// Changing the end location type
let endLocationTypeSelect;
let endAirportSelect;
let endCountrySelect;
let endContinentSelect;

function changeEndLocationType() {
    const locationType = endLocationTypeSelect.value;

    endAirportSelect.style.display = "none";
    endCountrySelect.style.display = "none";
    endContinentSelect.style.display = "none";

    if (locationType === "airport") {
        endAirportSelect.style.display = "block";
    } else if (locationType === "country") {
        endCountrySelect.style.display = "block";
    } else if (locationType === "continent") {
        endContinentSelect.style.display = "block";
    }
}

function resetEndLocation() {
    endLocationTypeSelect.value = "airport";
    changeEndLocationType();
}

// Changing the advanced filter options
let advancedFiltersSelect;

function changeAdvancedFilters() {
    const advancedFilters = advancedFiltersSelect.value;

    if (advancedFilters === "find-added" || advancedFilters === "find-removed") {
        document.getElementById("advanced-filters").style.display = "block";
    } else {
        document.getElementById("advanced-filters").style.display = "none";
    }
}

function resetAdvancedFilters() {
    advancedFiltersSelect.value = "none";
    changeAdvancedFilters();
}

// Configures the dynamic filter window layout
document.addEventListener('DOMContentLoaded', () => {
    const filterForm = document.getElementById('filter-form');

    // Start Location
    startLocationTypeSelect = document.getElementById('start-location-type');
    startAirportSelect = document.getElementById("start-airport-select");
    startCountrySelect = document.getElementById("start-country-select");
    startContinentSelect = document.getElementById("start-continent-select");

    // Event Listeners
    startLocationTypeSelect.addEventListener('change', changeStartLocationType);
    filterForm.addEventListener('reset', resetStartLocation);

    // End Location
    endLocationTypeSelect = document.getElementById('end-location-type');
    endAirportSelect = document.getElementById("end-airport-select");
    endCountrySelect = document.getElementById("end-country-select");
    endContinentSelect = document.getElementById("end-continent-select");

    // Event Listenters
    endLocationTypeSelect.addEventListener('change', changeEndLocationType);
    filterForm.addEventListener('reset', resetEndLocation);

    // Advanced Filter Options
    advancedFiltersSelect = document.getElementById('advanced-filters-select');

    // Event Listeners
    advancedFiltersSelect.addEventListener('change', changeAdvancedFilters);
    filterForm.addEventListener('reset', resetAdvancedFilters);
});

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
        dayOfWeekButtons[i].classList.remove("active");

    // Reset multi-select menus (start location, end location, and airlines)
    $(".info option:selected").prop("selected", false);

    // Reset max layovers
    document.getElementById("max_layovers").value = 0;

    // Reset airline type buttons
    const airlineTypeButtons = document.getElementsByClassName("airline_type_button");
    for (let i = 0; i < airlineTypeButtons.length; i++)
        airlineTypeButtons[i].classList.remove("active");
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

// Changes selection for each location in the dropdown menu
$(document).on("change", "#start_filter, #end_filter", function() {
    const target = $(this).data('target');
    const show = $("option:selected", this).data('show');
    $(target).children().addClass('hide');
    $(show).removeClass('hide');
});

// Sets the filter menu data
async function setFilterMenuData() {
    const airportData = await fetch("../static/airports.json")
        .then(response => {
            return response.json();
        });

    const airportCodes = Object.keys(airportData);

    // Set airports
    const airportStartMenu = document.getElementById("airport_start_info");
    const airportEndMenu = document.getElementById("airport_end_info");
    for (let i = 0; i < airportCodes.length; i++) {
        const currentAirport = airportData[airportCodes[i]];
        const opt = document.createElement("option");
        opt.value = airportCodes[i];
        opt.textContent = airportCodes[i] + ": " + currentAirport["name"];
        airportStartMenu.appendChild(opt);
        airportEndMenu.appendChild(opt.cloneNode(true));
    }

    // Set countries
    const countries = {}
    for (let i = 0; i < airportCodes.length; i++) {
        const currentAirport = airportData[airportCodes[i]];
        if (currentAirport["country_code"] != null)
            countries[currentAirport["country_code"]] = currentAirport["country"];
    }

    const sorted_country_codes = [];
    for (const key in countries)
        sorted_country_codes[sorted_country_codes.length] = key;

    sorted_country_codes.sort(function(a, b) {
        return countries[a].localeCompare(countries[b]);
    });

    const countryStartMenu = document.getElementById("country_start_info");
    const countryEndMenu = document.getElementById("country_end_info");
    for (let i = 0; i < sorted_country_codes.length; i++) {
        const code = sorted_country_codes[i];
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = countries[code];
        countryStartMenu.appendChild(opt);
        countryEndMenu.appendChild(opt.cloneNode(true));
    }
}

// Triggers on start of the webpage creation
$(function(){
    void setFilterMenuData();

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