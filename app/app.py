from flask import Flask, redirect, render_template, url_for, request
from Flights import *
FILENAME = "simple_data.csv"

app = Flask(__name__)
flights = FlightInfo(FILENAME, "./data/airports.txt")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form')
def form():
    name = request.cookies.get('form')

    req = Request(name)
    flights.details = flights.fullData.copy()

    flights.filterByLocation(req.originType, req.originValues,
                             req.destType, req.destValues)

    flights.filterByTime(req.originInfo['time'],
                         req.destInfo['time'])

    flights.filterByDayOfWeek(req.dayOfWeek)

    flights.filterByAirline(req.airlines)

    if flights.advancedRequest.filterAdded:
        flights.filterByAdded(flights.advancedRequest.start,
                              flights.advancedRequest.end)

    if flights.advancedRequest.filterRemoved:
        flights.filterByRemoved(flights.advancedRequest.start,
                                flights.advancedRequest.end)

    return f'Hello {name}!'
