let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
    });

    const shanghai = { lat: 31.224361, lng: 121.469170 };
    const shanghaiMarker = new google.maps.Marker({
        position: shanghai,
        map,
        title: "Shanghai",
    });

    const nyc = { lat: 40.7128, lng: -74.006 }
    const nycMarker = new google.maps.Marker({
       position: nyc,
       map,
       title: "New York City",
    });

    const berlin = { lat: 52.5200, lng: 13.4050 }
    const berlinMarker = new google.maps.Marker({
        position: berlin,
        map,
        title: "Berlin"
    })

    var markers = [nycMarker, shanghaiMarker, berlinMarker];
    var bounds = new google.maps.LatLngBounds();
    for (let i = 0; i < markers.length; i++)
        bounds.extend(markers[i].getPosition());
    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds)
    map.setZoom(map.getZoom() - 1);

    if(map.getZoom() > 15){
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

    const flightPath2Coordinates = [nyc, berlin, shanghai];
    const flightPath2 = new google.maps.Polyline({
        path: flightPath2Coordinates,
        geodesic: true,
        strokeColor: blue,
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });
    flightPath2.setMap(map);
}

window.initMap = initMap;
