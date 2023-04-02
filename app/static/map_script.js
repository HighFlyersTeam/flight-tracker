let map;
let mapMarkers;
let mapPaths;
let airportData;

async function getAirportData() {
    const response = await fetch("../static/airports.json")
        .then(response => {
            return response.json();
        });
    return response;
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
            }
        },
    });
    mapMarkers = [];
    mapPaths = [];

    airportData = await getAirportData();

    // Shows all airports by default
    const airportCodes = Object.keys(airportData);
    for (let i = 0; i < airportCodes.length; i++)
        createAirportMarker(airportCodes[i]);

    var bounds = new google.maps.LatLngBounds();
    for (let i = 0; i < mapMarkers.length; i++)
        bounds.extend(mapMarkers[i].getPosition());
    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds)
    map.setZoom(map.getZoom() - 1);
    if (map.getZoom() > 15) {
        map.setZoom(15);
    }

    // updateMapWithFlights([["JFK", "HKG", "LHR"], ["LHR", "JFK"]])
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

    mapMarkers.push(marker);
}

// Expects a 2D array of strings containing flight path data, with strings being airport codes
// Example: [["JFK", "HKG", "LHR"], ["LHR", "JFK"]]
export function updateMapWithFlights(flightData) {
    clearMap();

    let airports = new Set();
    const pathsAsCoordinates = [];
    for (let i = 0; i < flightData.length; i++) {
        const currentPath = [];
        for (let j = 0; j < flightData[i].length; j++) {
            airports.add(flightData[i][j]);
            const currentAirport = flightData[i][j];
            currentPath.push({lat: airportData[currentAirport]["lat"], lng: airportData[currentAirport]["lng"]})
        }
        pathsAsCoordinates.push(currentPath);
    }

    // Display all unique airports
    for (const currentAirportCode of airports.values())
        createAirportMarker(currentAirportCode);

    // Display all the paths
    for (let i = 0; i < pathsAsCoordinates.length; i++) {
        // TODO: decide if we want to keep this random color solution or have a systematic coloring system
        const randomColor = Math.floor(Math.random() * 16777215).toString(16);
        const flightPath = new google.maps.Polyline({
            path: pathsAsCoordinates[i],
            geodesic: true,
            strokeColor: "#" + randomColor,
            strokeOpacity: 1.0,
            strokeWeight: 2,
        });
        flightPath.setMap(map);
        mapPaths.push(flightPath);
    }
}

window.initMap = initMap;
