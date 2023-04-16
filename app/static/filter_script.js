// Times are in UTC time
const DEFAULT_START = "2000-01-01T04:00:00";
const DEFAULT_END = "2023-12-31T17:00:00";
const DEFAULT_SECONDARY_START = "2010-01-01T04:00:00";
const DEFAULT_SECONDARY_END = "2012-12-31T17:00:00";

// Matching start datetime between hotbar and menu
let startDatetimeHotbar;
let startDatetimeMenu;

function matchStartHotbartoMenu() {
    startDatetimeMenu.value = startDatetimeHotbar.value;
}

function matchStartMenutoHotbar() {
    startDatetimeHotbar.value = startDatetimeMenu.value;
}

// Matching end datetime between hotbar and menu
let endDatetimeHotbar;
let endDatetimeMenu;

function matchEndHotbartoMenu() {
    endDatetimeMenu.value = endDatetimeHotbar.value;
}

function matchEndMenutoHotbar() {
    endDatetimeHotbar.value = endDatetimeMenu.value;
}

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
let advancedFilterStartDatetime;
let advancedFilterEndDatetime;

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

    // Start Datetime
    startDatetimeHotbar = document.getElementById("start-datetime-hotbar");
    startDatetimeMenu = document.getElementById("start-datetime");

    // Default Values
    startDatetimeHotbar.value = DEFAULT_START;
    startDatetimeMenu.value = DEFAULT_START;

    // Event Listeners
    startDatetimeHotbar.addEventListener("change", matchStartHotbartoMenu);
    startDatetimeMenu.addEventListener("change", matchStartMenutoHotbar);

    // End Datetime
    endDatetimeHotbar = document.getElementById("end-datetime-hotbar");
    endDatetimeMenu = document.getElementById("end-datetime");

    // Default Values
    endDatetimeHotbar.value = DEFAULT_END;
    endDatetimeMenu.value = DEFAULT_END;

    // Event Listeners
    endDatetimeHotbar.addEventListener("change", matchEndHotbartoMenu);
    endDatetimeMenu.addEventListener("change", matchEndMenutoHotbar);

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
    advancedFilterStartDatetime = document.getElementById("secondary-start-datetime");
    advancedFilterEndDatetime = document.getElementById("secondary-end-datetime");

    // Default Values
    advancedFilterStartDatetime.value = DEFAULT_SECONDARY_START;
    advancedFilterEndDatetime.value = DEFAULT_SECONDARY_END;

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
    const airlineData = await fetch("../static/airlines.json")
        .then(response => {
            return response.json();
        });

    const airlineCodes = Object.keys(airlineData);
    airlineCodes.sort(function(a, b) {
        return airlineData[a].localeCompare(airlineData[b]);
    });

    // Set airlines
    const airlineMenu = document.getElementById("airlines");

    // Add airline options
    for (let i = 0; i < airlineCodes.length; i++) {
        const opt = document.createElement("option");
        opt.value = airlineCodes[i];
        opt.textContent = airlineData[airlineCodes[i]];

        airlineMenu.appendChild(opt);
    }

    const airportData = await fetch("../static/airports.json")
        .then(response => {
            return response.json();
        });

    const airportCodes = Object.keys(airportData);
    airportCodes.sort();

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

    const sortedCountryCodes = [];
    for (const key in countries)
        sortedCountryCodes[sortedCountryCodes.length] = key;

    sortedCountryCodes.sort(function(a, b) {
        return countries[a].localeCompare(countries[b]);
    });

    const countryStartMenu = document.getElementById("start-country-select");
    const countryEndMenu = document.getElementById("end-country-select");

    // Clear current options
    // removeOptions(countryStartMenu);
    // removeOptions(countryEndMenu);

    // Add new options
    for (let i = 0; i < sortedCountryCodes.length; i++) {
        const code = sortedCountryCodes[i];
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = countries[code];

        countryStartMenu.appendChild(opt);
        countryEndMenu.appendChild(opt.cloneNode(true));
    }
}
