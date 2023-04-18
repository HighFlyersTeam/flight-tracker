"""This module reads the data from the csv file and stores it into a pandas dataframe."""
import pandas as pd


class FlightData:
    """
    FlightData class
        Attributes: None
    """

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-locals
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-arguments

    def __init__(
        self,
        year,
        month,
        day,
        day_of_week,
        airline,
        flight_number,
        tail_number,
        origin_airport,
        destination_airport,
        scheduled_dep,
        dep_time,
        dep_delay,
        taxi_out,
        wheels_off,
        scheduled_time,
        elapsed_time,
        air_time,
        distance,
        wheels_on,
        taxi_in,
        scheduled_arr,
        arr_time,
        arr_delay,
        diverted,
        cancelled,
        cancellation_code,
        air_system_delay,
        security_delay,
        airline_delay,
        late_aircraft_delay,
        weather_delay,
    ):
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.airline = airline
        self.flight_number = flight_number
        self.tail_number = tail_number
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.scheduled_dep = scheduled_dep
        self.dep_time = dep_time
        self.dep_delay = dep_delay
        self.taxi_out = taxi_out
        self.wheels_off = wheels_off
        self.scheduled_time = scheduled_time
        self.elapsed_time = elapsed_time
        self.air_time = air_time
        self.distance = distance
        self.wheels_on = wheels_on
        self.taxi_in = taxi_in
        self.scheduled_arr = scheduled_arr
        self.arr_time = arr_time
        self.arr_delay = arr_delay
        self.diverted = diverted
        self.cancelled = cancelled
        self.cancellation_code = cancellation_code
        self.air_system_delay = air_system_delay
        self.security_delay = security_delay
        self.airline_delay = airline_delay
        self.late_aircraft_delay = late_aircraft_delay
        self.weather_delay = weather_delay


def create_flight_objects(flight_data):
    """
    Function: createFlightObjects
    Parameters: flight_data - csv file containing flight data
    Returns: None
    """
    # read from csv file and store into pandas dataframe
    data = pd.read_csv(flight_data)
    data.get()


if __name__ == "__main__":
    create_flight_objects("2015 flights.csv")
