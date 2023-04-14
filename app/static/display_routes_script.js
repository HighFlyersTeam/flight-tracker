// Filter find routes button functionality
import {updateMapWithFlights} from "../static/map_script.js";

export function displayFilteredFlights() {
    const data = getDataFromFilterMenu();

    setCookie("form", data, 5);

    $.ajax({
        url: 'http://127.0.0.1:5000/form', success: function(data) {
            updateMapWithFlights(eval(data));
        }
    });
}

function setCookie(c_name, value, expireminutes) {
    let exdate = new Date();
    exdate.setMinutes(exdate.getMinutes() + expireminutes);
    document.cookie = c_name + "=" + escape(value)+
        ((expireminutes == null) ? "" : ";expires=" + exdate.toUTCString());
}

function getDataFromFilterMenu() {
    let data = [];

    // Earliest Start Time
    const departure_datetime = document.getElementById("start-datetime").value;
    let start_data = departure_datetime.split("T");
    let start_time = start_data[1].replace(":", "");
    data.push(start_data[0]);
    data.push(String(start_time));

    // Latest End Time
    const arrival_datetime = document.getElementById("end-datetime").value;

    let end_data = arrival_datetime.split("T");
    let end_time = end_data[1].replace(":", "");
    data.push(end_data[0]);
    data.push(String(end_time));

    // Days of the Week
    const sunday = document.getElementById("sunday").checked;
    const monday = document.getElementById("monday").checked;
    const tuesday = document.getElementById("tuesday").checked;
    const wednesday = document.getElementById("wednesday").checked;
    const thursday = document.getElementById("thursday").checked;
    const friday = document.getElementById("friday").checked;
    const saturday = document.getElementById("saturday").checked;

    if (sunday === monday && monday === tuesday && tuesday === wednesday && wednesday === thursday
        && thursday === friday && friday === saturday) {
        for (let i = 0; i < 7; i++) {
            data.push(true);
        }
    } else {
        data.push(sunday);
        data.push(monday);
        data.push(tuesday);
        data.push(wednesday);
        data.push(thursday);
        data.push(friday);
        data.push(saturday);
    }

    // Start Location
    const departure_location_type = document.getElementById("start-location-type").value;
    let departure_location_values;
    let startID;
    if (departure_location_type === "airport") {
        startID = "#start-airport-select";
    } else if (departure_location_type === "country") {
        startID = "#start-country-select";
    } else if (departure_location_type === "continent") {
        startID = "#start-continent-select";
    }

    departure_location_values = $(startID).val();

    if (departure_location_values.length === 0) {
        departure_location_values = [];
        $(startID + " option").each(function() {
            departure_location_values.push($(this).val());
        });
    }

    data.push(departure_location_type);
    data.push(departure_location_values);

    // End Location
    const arrival_location_type = document.getElementById("end-location-type").value;
    let arrival_location_values;
    let endID;
    if (arrival_location_type === "airport") {
        endID = "#end-airport-select";
    } else if (arrival_location_type === "country") {
        endID = "#end-country-select";
    } else if (arrival_location_type === "continent") {
        endID = "#end-continent-select";
    }

    arrival_location_values = $(endID).val();

    if (arrival_location_values.length === 0) {
        arrival_location_values = [];
        $(endID + " option").each(function() {
            arrival_location_values.push($(this).val());
        });
    }

    data.push(arrival_location_type);
    data.push(arrival_location_values);
    
    // Max Layovers
    data.push(String(parseInt(document.getElementById("layovers").value)));

    // Airlines
    let airlines = $("#airlines").val();
    if (airlines.length == 0) {
        airlines = [];
        $("#airlines" + " option").each(function() {
            airlines.push($(this).val());
        })
    }
    data.push(airlines);

    // Type of Airline
    const all_airlines = document.getElementById("airline-type-all").checked;
    const passenger = document.getElementById("airline-type-passenger").checked;
    const cargo = document.getElementById("airline-type-cargo").checked;
    if (all_airlines) {
        data.push(true);
        data.push(true);
    } else if (passenger) {
        data.push(false);
        data.push(true);
    } else if (cargo) {
        data.push(true);
        data.push(false);
    } else {
        data.push(true);
        data.push(true);
    }

    // Advanced Options
    const option = document.getElementById("advanced-filters-select").value;
    const added = option === "find-added";
    const removed = option === "find-removed";

    const adv_start_datetime = document.getElementById("secondary-start-datetime").value;
    let adv_start_data = adv_start_datetime.split("T");
    let adv_start_time = adv_start_data[1].replace(":", "");
    data.push(adv_start_data[0]);
    data.push(adv_start_time);

    const adv_end_datetime = document.getElementById("secondary-end-datetime").value;
    let adv_end_data = adv_end_datetime.split("T");
    let adv_end_time = adv_end_data[1].replace(":", "");
    data.push(adv_end_data[0]);
    data.push(adv_end_time);

    data.push(added);
    data.push(removed);

    return data.join("--");
}