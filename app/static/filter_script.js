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
document.addEventListener("DOMContentLoaded", () => {
    const filterForm = document.getElementById("filter-form");

    // Start Location
    startLocationTypeSelect = document.getElementById("start-location-type");
    startAirportSelect = document.getElementById("start-airport-select");
    startCountrySelect = document.getElementById("start-country-select");
    startContinentSelect = document.getElementById("start-continent-select");

    // Event Listeners
    startLocationTypeSelect.addEventListener("change", changeStartLocationType);
    filterForm.addEventListener("reset", resetStartLocation);

    // End Location
    endLocationTypeSelect = document.getElementById("end-location-type");
    endAirportSelect = document.getElementById("end-airport-select");
    endCountrySelect = document.getElementById("end-country-select");
    endContinentSelect = document.getElementById("end-continent-select");

    // Event Listenters
    endLocationTypeSelect.addEventListener("change", changeEndLocationType);
    filterForm.addEventListener("reset", resetEndLocation);

    // Advanced Filter Options
    advancedFiltersSelect = document.getElementById("advanced-filters-select");

    // Event Listeners
    advancedFiltersSelect.addEventListener("change", changeAdvancedFilters);
    filterForm.addEventListener("reset", resetAdvancedFilters);

    // Remove need for Shift/Ctrl + Click in multiselect menus
    $(document).on("mousedown", "option", function (e) {
        e.preventDefault();
        $(this).prop("selected", !$(this).prop("selected"));
        return false;
    });
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
