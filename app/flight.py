"""module for Flight class"""
import datetime


"""
Flight class
    Attributes:
        flight_time: flight time in minutes
        departure_time: departure time as a datetime object
        arrival_time: arrival time as a datetime object
        origin: origin airport ICAO code
        destination: destination airport ICAO code
"""
class Flight:
    def __init__(self, flight_info):
        self.flight_time = int(flight_info["ELAPSED_TIME"])

        self.departure_time = datetime.datetime(year=int(flight_info["YEAR"]),
                                            month=int(flight_info["MONTH"]),
                                            day=int(flight_info["DAY"]),
                                            hour=int(
                                                   flight_info["DEPARTURE_TIME"].zfill(4)[:2]),
                                            minute=int(flight_info["DEPARTURE_TIME"].zfill(4)[2:]))

        self.arrival_time = self.departure_time + \
            datetime.timedelta(minutes=self.flight_time)

        self.origin = flight_info["ORIGIN_AIRPORT"]
        self.destination = flight_info["DESTINATION_AIRPORT"]

    def __str__(self):
        ret_val = "\nOrigin: " + self.origin + "\n"
        ret_val += "Destination: " + self.destination + "\n"
        ret_val += "Departure Time: " + \
            self.departure_time.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Arrival Time: " + \
            self.arrival_time.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Flight Time: " + str(self.flight_time) + " minutes"

        return ret_val

    def __repr__(self):
        return self.__str__()
