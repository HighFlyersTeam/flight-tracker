import pandas as pd
import datetime

class FlightInfo:
    def __init__(self, filename):
        self.columns = ["YEAR", "MONTH", "DAY", "AIRLINE", "FLIGHT_NUMBER", 
                        "ORIGIN_AIRPORT", "DESTINATION_AIRPORT","DEPARTURE_TIME",
                        "DIVERTED","CANCELLED","ARRIVAL_TIME", "ELAPSED_TIME"]

        self.data_types = { "YEAR": int, 
                            "MONTH": int, 
                            "DAY": int, 
                            "AIRLINE": "string", 
                            "FLIGHT_NUMBER": int, 
                            "ORIGIN_AIRPORT": "string", 
                            "DESTINATION_AIRPORT": "string",
                            "DEPARTURE_TIME": "string",
                            "ARRIVAL_TIME": "string",
                            "DIVERTED": int,
                            "CANCELLED": int,
                            "ELAPSED_TIME": "string"}

        self.details = pd.read_csv( filename, usecols = self.columns, dtype = self.data_types)
    
    def removeCancelledFlights(self):
        self.details = self.details[self.details['DIVERTED'] == 0]
        self.details = self.details[self.details['CANCELLED'] == 0]


class Flight:
    def __init__(self, flightInfo):
        self.flightTime = int(flightInfo["ELAPSED_TIME"])

        self.departureTime = datetime.datetime( year = int(flightInfo["YEAR"]),
                                                month = int(flightInfo["MONTH"]),
                                                day = int(flightInfo["DAY"]),
                                                hour = int(flightInfo["DEPARTURE_TIME"].zfill(4)[:2]),
                                                minute = int(flightInfo["DEPARTURE_TIME"].zfill(4)[2:]))

        self.arrivalTime = self.departureTime + datetime.timedelta(minutes= self.flightTime)

        self.origin = flightInfo["ORIGIN_AIRPORT"]
        self.destination = flightInfo["DESTINATION_AIRPORT"]

    def __str__(self):
        ret_val =  "\nOrigin: " + self.origin + "\n"
        ret_val += "Destination: " + self.destination + "\n" 
        ret_val += "Departure Time: "+ self.departureTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Arrival Time: " + self.arrivalTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Flight Time: " + str(self.flightTime) + " minutes"

        return ret_val


