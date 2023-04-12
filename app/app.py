"""The application"""
from flask import Flask, render_template, request
from flight_info import FlightInfo
from request import Request
FILENAME = "data.csv"

app = Flask(__name__)
flights = FlightInfo(FILENAME)


@app.route('/')
def home():
    """The home page"""
    return render_template('index.html')


@app.route('/form')
def form():
    """The form page"""
    name = request.cookies.get('form')

    req = Request(name)

    flights.details = flights.full_data.copy()

    flights.filter_by_location(req.origin_type,
                               req.origin_values,
                               req.dest_type,
                               req.dest_values)

    flights.filter_by_time(req.start_date,
                           req.start_time,
                           req.end_date,
                           req.end_time)

    flights.filter_by_day_of_week(req.day_of_week)

    flights.filter_by_airline(req.airlines)

    flights.filter_by_cargo(req.is_cargo, req.is_passenger)

    if req.adv_req.filter_added == 'true':
        flights.filter_by_added(req)

    if req.adv_req.filter_removed == 'true':
        flights.filter_by_removed(req)

    ret_val = []
    for _, row in flights.details.iterrows():
        ret_val.append([row['ORIGIN_AIRPORT'], row['DESTINATION_AIRPORT']])

    print("\nReturn Dataframe:\n", ret_val)
    return f'{ret_val}'
