import datetime


class Flight:
    def __init__(self, flightInfo):
        self.flightTime = int(flightInfo["ELAPSED_TIME"])

        self.departureTime = datetime.datetime(year=int(flightInfo["YEAR"]),
                                               month=int(flightInfo["MONTH"]),
                                               day=int(flightInfo["DAY"]),
                                               hour=int(
                                                   flightInfo["DEPARTURE_TIME"].zfill(4)[:2]),
                                               minute=int(flightInfo["DEPARTURE_TIME"].zfill(4)[2:]))

        self.arrivalTime = self.departureTime + \
            datetime.timedelta(minutes=self.flightTime)

        self.origin = flightInfo["ORIGIN_AIRPORT"]
        self.destination = flightInfo["DESTINATION_AIRPORT"]

    def __str__(self):
        ret_val = "\nOrigin: " + self.origin + "\n"
        ret_val += "Destination: " + self.destination + "\n"
        ret_val += "Departure Time: " + \
            self.departureTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Arrival Time: " + \
            self.arrivalTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Flight Time: " + str(self.flightTime) + " minutes"

        return ret_val
