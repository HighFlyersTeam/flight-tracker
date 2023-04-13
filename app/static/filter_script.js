// Times are in UTC time
const DEFAULT_START = "2018-01-01T04:00:00";
const DEFAULT_END = "2018-12-31T17:00:00";

// Changing the start location type
let startLocationTypeSelect;
let startAirportDiv;
let startCountryDiv;
let startContinentDiv;

function changeStartLocationType() {
    const locationType = startLocationTypeSelect.value;

    startAirportDiv.style.display = "none";
    startCountryDiv.style.display = "none";
    startContinentDiv.style.display = "none";

    if (locationType === "airport") {
        startAirportDiv.style.display = "block";
    } else if (locationType === "country") {
        startCountryDiv.style.display = "block";
    } else if (locationType === "continent") {
        startContinentDiv.style.display = "block";
    }
}

function resetStartLocation() {
    startLocationTypeSelect.value = "airport";
    changeStartLocationType();
}

// Changing the end location type
let endLocationTypeSelect;
let endAirportDiv;
let endCountryDiv;
let endContinentDiv;

function changeEndLocationType() {
    const locationType = endLocationTypeSelect.value;

    endAirportDiv.style.display = "none";
    endCountryDiv.style.display = "none";
    endContinentDiv.style.display = "none";

    if (locationType === "airport") {
        endAirportDiv.style.display = "block";
    } else if (locationType === "country") {
        endCountryDiv.style.display = "block";
    } else if (locationType === "continent") {
        endContinentDiv.style.display = "block";
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
    startCountryDiv = document.getElementById("start-country-div");
    startAirportDiv = document.getElementById("start-airport-div");
    startContinentDiv = document.getElementById("start-continent-div");

    // Event Listeners
    startLocationTypeSelect.addEventListener("change", changeStartLocationType);
    filterForm.addEventListener("reset", resetStartLocation);

    // End Location
    endLocationTypeSelect = document.getElementById("end-location-type");
    endAirportDiv = document.getElementById("end-airport-div");
    endCountryDiv = document.getElementById("end-country-div");
    endContinentDiv = document.getElementById("end-continent-div");

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

    setFilterMenuData();
});

// Sets the filter menu data
function removeOptions(selectElement) {
    var i, L = selectElement.options.length - 1;
    for (i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
}

async function setFilterMenuData() {
    const airportData = await fetch("../static/airports.json")
        .then(response => {
            return response.json();
        });

    const airportCodes = Object.keys(airportData);

    // Set airports
    const airportStartMenu = document.getElementById("start-airport-select");
    const airportStartHotbar = document.getElementById("start-airport-hotbar");
    const airportEndMenu = document.getElementById("end-airport-select");
    const airportEndHotbar = document.getElementById("end-airport-hotbar");
    
    // Clear current options
    // removeOptions(airportStartMenu);
    // removeOptions(airportStartHotbar);
    // removeOptions(airportEndMenu);
    // removeOptions(airportEndHotbar);
    
    // Add new options
    for (let i = 0; i < airportCodes.length; i++) {
        const currentAirport = airportData[airportCodes[i]];
        const opt = document.createElement("option");
        opt.value = airportCodes[i];
        opt.textContent = airportCodes[i] + ": " + currentAirport["name"];

        airportStartMenu.appendChild(opt);
        airportStartHotbar.appendChild(opt.cloneNode(true));
        airportEndMenu.appendChild(opt.cloneNode(true));
        airportEndHotbar.appendChild(opt.cloneNode(true));
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

    const countryStartMenu = document.getElementById("start-country-select");
    const countryEndMenu = document.getElementById("end-country-select");

    // Clear current options
    // removeOptions(countryStartMenu);
    // removeOptions(countryEndMenu);

    // Add new options
    for (let i = 0; i < sorted_country_codes.length; i++) {
        const code = sorted_country_codes[i];
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = countries[code];

        countryStartMenu.appendChild(opt);
        countryEndMenu.appendChild(opt.cloneNode(true));
    }
}
