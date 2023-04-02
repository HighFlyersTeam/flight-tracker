// Filter find routes button functionality
import {updateMapWithFlights} from "../static/map_script.js";

export function displayFilteredFlights() {
    const data = getDataFromFilterMenu();

    // TODO: replace this with a call that sends the data to the backend
    // console.log(JSON.stringify(data, null, ' '));

    setCookie("form",JSON.stringify(data),5);

    // Simulate an HTTP redirect:
    // Simulate a mouse click:
    // window.location.href = "http://127.0.0.1:5000/form";

    updateMapWithFlights([["JFK", "HKG", "LHR"], ["LHR", "JFK"]])
}

function setCookie(c_name, value, expireminutes) {
    let exdate = new Date();
    exdate.setMinutes(exdate.getMinutes()+expireminutes);
    document.cookie=c_name+ "=" +escape(value)+
        ((expireminutes==null) ? "" : ";expires="+exdate.toUTCString());
}

function getDataFromFilterMenu() {
    const data = {};

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

    // Start Location
    const departure_location = {};
    const departure_location_type = document.getElementById("start_filter").value;
    let departure_location_values;
    if (departure_location_type == "airport") {
        departure_location_values = $('#airport_start_info').val();
    } else if (departure_location_type == "country") {
        departure_location_values = $('#country_start_info').val();
    } else if (departure_location_type == "continent") {
        departure_location_values = $('#continent_start_info').val();
    }
    departure_location["type"] = departure_location_type;
    departure_location["values"] = departure_location_values;
    departure_info["location"] = departure_location;

    // End Location
    const arrival_location = {};
    const arrival_location_type = document.getElementById("end_filter").value;
    let arrival_location_values;
    if (arrival_location_type == "airport") {
        arrival_location_values = $('#airport_end_info').val();
    } else if (arrival_location_type == "country") {
        arrival_location_values = $('#country_end_info').val();
    } else if (arrival_location_type == "continent") {
        arrival_location_values = $('#continent_end_info').val();
    }
    arrival_location["type"] = arrival_location_type;
    arrival_location["values"] = arrival_location_values;
    arrival_info["location"] = arrival_location;

    // Max Layovers
    data["max_layovers"] = parseInt(document.getElementById("max_layovers").value);

    // Airlines
    data["airlines"] = $('#airline_companies').val();

    // Type of Airline
    const airline_type = {};
    const cargo = document.getElementById("cargo_button").classList.contains("active");
    const passenger = document.getElementById("passenger_button").classList.contains("active");
    airline_type["cargo"] = cargo;
    airline_type["passenger"] = passenger;
    data["airline_type"] = airline_type;

    // Advanced Options
    const advanced_options = {};
    const added = document.getElementById("find_added_flights_button").classList.contains("active");
    const removed = document.getElementById("find_removed_flights_button").classList.contains("active");
    const start = {};
    const start_date = document.getElementById("start_date2").value;
    const start_time = document.getElementById("start_time2").value;
    start["date"] = start_date;
    start["time"] = start_time;
    const end = {};
    const end_date = document.getElementById("end_date2").value;
    const end_time = document.getElementById("end_time2").value;
    end["date"] = end_date;
    end["time"] = end_time;
    advanced_options["find_added"] = added;
    advanced_options["find_removed"] = removed;
    advanced_options["start_info"] = start;
    advanced_options["end_info"] = end;
    data["advanced_options"] = advanced_options;

    return data;
}