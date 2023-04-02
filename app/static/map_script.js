let map;
let mapMarkers;
let mapPaths;

async function getAirportData() {
    const response = await fetch("/app/data/airports.json")
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

    const airportData = await getAirportData();
    const airportCodes = Object.keys(airportData);
    for (let i = 0; i < airportCodes.length; i++) {
        const currentAirport = airportData[airportCodes[i]];
        const location = {lat: currentAirport["lat"], lng: currentAirport["lng"]};
        const infoWindow = new google.maps.InfoWindow({
            content: "<strong>" + currentAirport["name"] + "</strong>"
        });
        const marker = new google.maps.Marker({
            position: location,
            map,
            title: currentAirport["name"],
        });
        marker.addListener("click", function() {
            infoWindow.open(map, marker);
        });

        mapMarkers.push(marker);
    }

    const shanghai = {lat: 31.224361, lng: 121.469170};
    const shanghaiMarker = new google.maps.Marker({
        position: shanghai,
        map,
        title: "Shanghai",
    });
    mapMarkers.push(shanghaiMarker);

    const nyc = {lat: 40.7128, lng: -74.006}
    const nycMarker = new google.maps.Marker({
        position: nyc,
        map,
        title: "New York City",
    });
    mapMarkers.push(nycMarker);

    const berlin = {lat: 52.5200, lng: 13.4050}
    const berlinMarker = new google.maps.Marker({
        position: berlin,
        map,
        title: "Berlin"
    });
    mapMarkers.push(berlinMarker);

    var markers = [nycMarker, shanghaiMarker, berlinMarker];
    var bounds = new google.maps.LatLngBounds();
    for (let i = 0; i < markers.length; i++)
        bounds.extend(markers[i].getPosition());
    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds)
    map.setZoom(map.getZoom() - 1);

    if (map.getZoom() > 15) {
        map.setZoom(15);
    }

    const red = "#FF0000";
    const blue = "#0000FF";

    const flightPathCoordinates = [nyc, shanghai];
    const flightPath = new google.maps.Polyline({
        path: flightPathCoordinates,
        geodesic: true,
        strokeColor: red,
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });
    flightPath.setMap(map);
    mapPaths.push(flightPath);

    const flightPath2Coordinates = [nyc, berlin, shanghai];
    const flightPath2 = new google.maps.Polyline({
        path: flightPath2Coordinates,
        geodesic: true,
        strokeColor: blue,
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });
    flightPath2.setMap(map);
    mapPaths.push(flightPath2);

    // clearMap();
}

function clearMap() {
    for (let i = 0; i < mapMarkers.length; i++) {
        mapMarkers[i].setMap(null);
    }
    for (let i = 0; i < mapPaths.length; i++) {
        mapPaths[i].setMap(null);
    }
    mapMarkers = [];
    mapPaths = [];
}


window.initMap = initMap;
