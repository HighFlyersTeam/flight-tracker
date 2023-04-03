from flask import Flask, redirect, render_template, url_for, request
from FlightInfo import FlightInfo
from Request import Request
FILENAME = "data.csv"

app = Flask(__name__)
flights = FlightInfo(FILENAME)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form')
def form():
    name = request.cookies.get('form')

    req = Request(name)

    flights.details = flights.fullData.copy()

    print(req.originType)
    print(req.originValues)
    print(req.destType)
    print(req.destValues)
    flights.filterByLocation(req.originType, req.originValues,
                             req.destType, req.destValues)

    # flights.filterByTime(req.originInfo['time'],
    #                      req.destInfo['time'])

    flights.filterByDayOfWeek(req.dayOfWeek)

    # flights.filterByAirline(req.airlines)
    #
    # if flights.advancedRequest.filterAdded:
    #     flights.filterByAdded(flights.advancedRequest)
    #
    # if flights.advancedRequest.filterRemoved:
    #     flights.filterByRemoved(flights.advancedRequest)
    print(flights.details)
    return f'{flights}'
