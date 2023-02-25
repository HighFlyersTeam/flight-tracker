let map;

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
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

    var markers = [nycMarker, shanghaiMarker];
    var bounds = new google.maps.LatLngBounds();
    for (let i = 0; i < markers.length; i++)
        bounds.extend(markers[i].getPosition());
    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds)
    map.setZoom(map.getZoom() - 1);

    if(map.getZoom() > 15){
        map.setZoom(15);
    }
}

window.initMap = initMap;
