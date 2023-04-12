from flask import Flask, redirect, render_template, url_for, request, make_response
from flight_info import FlightInfo
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

    flights.filterByLocation(req.originType, req.originValues,
                             req.destType, req.destValues)

    flights.filterByTime(req.startDate, req.startTime,
                         req.endDate, req.endTime)

    flights.filterByDayOfWeek(req.dayOfWeek)

    flights.filterByAirline(req.airlines)

    flights.filterByCargo(req.isCargo, req.isPassenger)

    # if flights.advancedRequest.filterAdded:
    #     flights.filterByAdded(flights.advancedRequest)

    # if flights.advancedRequest.filterRemoved:
    #     flights.filterByRemoved(flights.advancedRequest)

    ret_val = []
    for index, row in flights.details.iterrows():
        ret_val.append([row['ORIGIN_AIRPORT'], row['DESTINATION_AIRPORT']])

    print("\nReturn Dataframe:\n", ret_val)
    return f'{ret_val}'
