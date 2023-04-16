let map;
let mapMarkers;
let mapPaths;

let airportData;
let airportInfoWindows;
let airlineData;
let airlineInfoWindows;

let airlineColors;

async function getAirportData() {
    return await fetch("../static/airports.json")
        .then(response => {
            return response.json();
        });
}

async function getAirlineColorData() {
    return await fetch("../static/airline_colors.json")
        .then(response => {
            return response.json();
        });
}

async function getAirlineData() {
    return await fetch("../static/airlines.json")
        .then(response => {
            return response.json();
        });
}

async function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        restriction: {
            latLngBounds: {
                north: 85,
                south: -85,
                west: -180,
                east: 180
            },
            strictBounds: true
        },
    });
    mapMarkers = [];
    mapPaths = [];

    airportInfoWindows = [];
    airlineInfoWindows = [];

    airportData = await getAirportData();
    airlineData = await getAirlineData();

    // Shows all airports by default
    const airportCodes = Object.keys(airportData);
    for (let i = 0; i < airportCodes.length; i++)
        createAirportMarker(airportCodes[i]);

    map.setCenter({lat: 0, lng: 0});
    map.setZoom(0);

    airlineColors = await getAirlineColorData();
}

function clearMap() {
    for (let i = 0; i < mapMarkers.length; i++)
        mapMarkers[i].setMap(null);
    for (let i = 0; i < mapPaths.length; i++)
        mapPaths[i].setMap(null);
    mapMarkers = [];
    mapPaths = [];
}

function createAirportMarker(airportCode) {
    const currentAirport = airportData[airportCode];
    const location = {lat: currentAirport["lat"], lng: currentAirport["lng"]};
    const infoWindow = new google.maps.InfoWindow({
        content: "<strong>" + currentAirport["name"] + "</strong>"
    });
    const marker = new google.maps.Marker({
        position: location,
        map,
        title: currentAirport["name"],
    });
    marker.addListener("click", function () {
        infoWindow.open(map, marker);
    });

    airportInfoWindows.push(infoWindow);
    mapMarkers.push(marker);
}

// Expects a 2D array of strings containing origin airport, destination airport, airline, and true/false depending on
// whether or not it is a cargo plane
export function updateMapWithFlights(flightData) {
    clearMap();

    // Close any info windows that are currently open
    for (let i = 0; i < airportInfoWindows.length; i++)
        airportInfoWindows[i].close();
    for (let i = 0; i < airlineInfoWindows.length; i++)
        airlineInfoWindows[i].close();

    let airports = new Set();
    for (let i = 0; i < flightData.length; i++) {
        const originAirport = flightData[i][0];
        const destinationAirport = flightData[i][1];
        airports.add(originAirport);
        airports.add(destinationAirport);
    }

    // Display all unique airports
    for (const currentAirportCode of airports.values())
        createAirportMarker(currentAirportCode);

    // Display all the paths
    airlineInfoWindows = [];
    for (let i = 0; i < flightData.length; i++) {
        const currentPath = [];
        const originAirport = flightData[i][0];
        const destinationAirport = flightData[i][1];
        currentPath.push({lat: airportData[originAirport]["lat"], lng: airportData[originAirport]["lng"]});
        currentPath.push({lat: airportData[destinationAirport]["lat"], lng: airportData[destinationAirport]["lng"]})

        const airline = flightData[i][2];
        const flightPath = new google.maps.Polyline({
            path: currentPath,
            geodesic: true,
            strokeColor: airlineColors[airline],
            strokeOpacity: 1.0,
            strokeWeight: 5,
        });
        flightPath.setMap(map);

        // Set info window for each flight path
        let information = originAirport + "&rarr;" + destinationAirport + "<br />"
            + "Airline: " + airlineData[airline] + "<br />";
        if (flightData[i][3] === "true")
            information += "Cargo airplane";
        else if (flightData[i][3] === "false")
            information += "Passenger airplane";

        const infoWindow = new google.maps.InfoWindow({
            content: information
        });
        google.maps.event.addListener(flightPath, 'click', (function (poly, i) {
            return function (event) {
                infoWindow.setPosition(event.latLng);
                infoWindow.open(map);
            };
        })(flightPath, i));

        airlineInfoWindows.push(infoWindow);
        mapPaths.push(flightPath);
    }
}

window.initMap = initMap;
