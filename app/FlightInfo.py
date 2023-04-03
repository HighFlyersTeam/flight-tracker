import pandas as pd
import datetime


class FlightInfo:
    def __init__(self, filename):
        columns = ["YEAR", "MONTH", "DAY", "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER",
                   "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "DEPARTURE_TIME",
                   "DIVERTED", "CANCELLED", "ARRIVAL_TIME", "ELAPSED_TIME",
                   "ORIGIN_COUNTRY", "DESTINATION_COUNTRY", "ORIGIN_CONTINENT",
                   "DESTINATION_CONTINENT",	"CARGO"]

        data_types = {"YEAR": int,
                      "MONTH": int,
                      "DAY": int,
                      "DAY_OF_WEEK": "string",
                      "AIRLINE": "string",
                      "FLIGHT_NUMBER": int,
                      "ORIGIN_AIRPORT": "string",
                      "DESTINATION_AIRPORT": "string",
                      "DEPARTURE_TIME": "string",
                      "ARRIVAL_TIME": "string",
                      "DIVERTED": int,
                      "CANCELLED": int,
                      "ELAPSED_TIME": int,
                      "ORIGIN_COUNTRY": "string",
                      "DESTINATION_COUNTRY": "string",
                      "ORIGIN_CONTINENT": "string",
                      "DESTINATION_CONTINENT": "string",
                      "CARGO": bool}

        self.details = pd.read_csv(filename, usecols=columns, dtype=data_types)

        self.details["DEPARTURE_TIME"] = self.details["DEPARTURE_TIME"].str.zfill(
            4)

        self.details["HOUR"] = self.details["DEPARTURE_TIME"].str[:2]
        self.details["MINUTE"] = self.details["DEPARTURE_TIME"].str[2:]

        self.details["DEPARTURE_TIME"] = pd.to_datetime(
            self.details[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']])

        self.details["ELAPSED_TIME"] = pd.to_timedelta(
            self.details["ELAPSED_TIME"], unit='minute')

        self.details["ARRIVAL_TIME"] = self.details["DEPARTURE_TIME"] + \
            self.details["ELAPSED_TIME"]

        # copy of full data for resetting filters
        self.fullData = self.details.copy()

    def filterByLocation(self, originType, originValues,
                         destType, destValues):
        if originType == 'airport':
            self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(
                originValues)]
        elif originType == 'country':
            self.details = self.details[self.details["ORIGIN_COUNTRY"].isin(
                originValues)]
        elif originType == 'continent':
            self.details = self.details[self.details["ORIGIN_CONTINENT"].isin(
                originValues)]

        if destType == 'airport':
            self.details = self.details[self.details["DESTINATION_AIRPORT"].isin(
                destValues)]
        elif destType == 'country':
            self.details = self.details[self.details["DESTINATION_COUNTRY"].isin(
                destValues)]
        elif destType == 'continent':
            self.details = self.details[self.details["DESTINATION_CONTINENT"].isin(
                destValues)]

    def filterByTime(self, startDate, startTime, endDate, endTime):
        parsed_start = startDate + '-' + startTime[:2] + '-' + startTime[2:]
        parsed_end = endDate + '-' + endTime[:2] + '-' + endTime[2:]

        depart_time = datetime.datetime.strptime(parsed_start,
                                                 '%Y-%m-%d-%H-%M')

        arrive_time = datetime.datetime.strptime(parsed_end,
                                                 '%Y-%m-%d-%H-%M')

        self.details = self.details[self.details["DEPARTURE_TIME"] > depart_time]

        self.details = self.details[self.details["ARRIVAL_TIME"] < arrive_time]

    def filterByDayOfWeek(self, days):
        selectedDays = []
        for k in (days.keys()):
            if (days[k] == "true"):
                selectedDays.append(k)

        # print("Selected Days:", selectedDays)
        self.details = self.details[self.details["DAY_OF_WEEK"].isin(
            selectedDays)]

    def filterByAirline(self, airlines):
        self.details = self.details[self.details["AIRLINE"].isin(
            airlines)]

    def filterByAdded(self, req):
        depart1 = datetime.datetime.strptime(req.start1, '%Y-%m-%d')
        depart2 = datetime.datetime.strptime(req.start2, '%Y-%m-%d')

        arrive1 = datetime.datetime.strptime(req.end1, '%Y-%m-%d')
        arrive2 = datetime.datetime.strptime(req.end2, '%Y-%m-%d')

        flights1 = self.fullData[self.fullData["DEPARTURE_TIME"] > depart1]
        flights1 = self.fullData[self.fullData["ARRIVAL_TIME"] < arrive1]

        flights2 = self.fullData[self.fullData["DEPARTURE_TIME"] > depart2]
        flights2 = self.fullData[self.fullData["ARRIVAL_TIME"] < arrive2]

        self.details = flights2

    def filterByRemoved(self, req):
        depart1 = datetime.datetime.strptime(req.start1, '%Y-%m-%d')
        depart2 = datetime.datetime.strptime(req.start2, '%Y-%m-%d')

        arrive1 = datetime.datetime.strptime(req.end1, '%Y-%m-%d')
        arrive2 = datetime.datetime.strptime(req.end2, '%Y-%m-%d')

        flights1 = self.fullData[self.fullData["DEPARTURE_TIME"] > depart1]
        flights1 = self.fullData[self.fullData["ARRIVAL_TIME"] < arrive1]

        flights2 = self.fullData[self.fullData["DEPARTURE_TIME"] > depart2]
        flights2 = self.fullData[self.fullData["ARRIVAL_TIME"] < arrive2]

        self.details = flights1
