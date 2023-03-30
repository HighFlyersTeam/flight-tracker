import pandas as pd
import datetime
import json


class Request:
    def __init__(self, json_request):
        self.details = json.loads(json_request)

        self.originInfo = self.details['departure_info']
        self.originType = self.originInfo['location']['type']
        self.originValues = None
        if self.originType == "airport":
            self.originValues = self.arrivalInfo['location']['values']
        elif self.originType == "country":
            self.originValues = self.arrivalInfo['location']['values']
        elif self.originType == "continent":
            self.originValues = self.arrivalInfo['location']['values']

        self.destInfo = self.details['arrival_info']
        self.destType = self.destInfo['location']['type']
        self.destValues = None
        if self.destType == "airport":
            self.destValues = self.destInfo['location']['values']
        elif self.destType == "country":
            self.destValues = self.destInfo['location']['values']
        elif self.destType == "continent":
            self.destValues = self.destInfo['location']['values']

        self.dayOfWeek = self.details['day_of_week']
        self.numLayovers = self.details['max_layovers']
        self.airlines = self.details['airlines']
        self.isCargo = self.details['airline_type']['cargo']
        self.isPassenger = self.details['airline_type']['passenger']

        self.advancedRequest = AdvancedRequest(
            self.details['advanced_options'])

    def populate(self, json_request):
        self.details = json.loads(json_request)

        self.originInfo = self.details['departure_info']
        self.originAirports = None
        self.originCountries = None
        self.originContinents = None
        if self.originInfo['location']['type'] == "airport":
            self.originAirports = self.arrivalInfo['location']['values']
        elif self.originInfo['location']['type'] == "country":
            self.originCountries = self.arrivalInfo['location']['values']
        elif self.originInfo['location']['type'] == "continent":
            self.originContinents = self.arrivalInfo['location']['values']

        self.destInfo = self.details['arrival_info']
        self.destAirports = None
        self.destCountries = None
        self.destContinents = None
        if self.destInfo['location']['type'] == "airport":
            self.destAirports = self.destInfo['location']['values']
        elif self.destInfo['location']['type'] == "country":
            self.destCountries = self.destInfo['location']['values']
        elif self.destInfo['location']['type'] == "continent":
            self.destContinents = self.destInfo['location']['values']

        self.dayOfWeek = self.details['day_of_week']
        self.layovers = self.details['max_layovers']
        self.airlines = self.details['airlines']
        self.isCargo = self.details['airline_type']['cargo']
        self.isPassenger = self.details['airline_type']['passenger']

        self.findAdded = self.details['advanced_options']['find_added']
        if self.findAdded:
            self.advancedStart = self.details['advanced_options']['start_info']
            self.advanctedEnd = self.details['advanced_options']['end_info']

        self.findRemoved = self.details['advanced_options']['find_removed']
        if self.findRemoved:
            self.advancedStart = self.details['advanced_options']['start_info']
            self.advanctedEnd = self.details['advanced_options']['end_info']


class AdvancedRequest:
    def __init__(self, request_details):
        self.filterAdded = request_details['find_added']
        if self.filterAdded:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']

        self.filterRemoved = request_details['find_removed']
        if self.filterRemoved:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']

    def populate(self, request_details):
        self.filterAdded = request_details['find_added']
        if self.filterAdded:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']

        self.filterRemoved = request_details['find_removed']
        if self.filterRemoved:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']


class FlightInfo:
    def __init__(self, filename):
        columns = ["YEAR", "MONTH", "DAY", "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER",
                   "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "DEPARTURE_TIME",
                   "DIVERTED", "CANCELLED", "ARRIVAL_TIME", "ELAPSED_TIME"]

        data_types = {"YEAR": int,
                      "MONTH": int,
                      "DAY": int,
                      "DAY_OF_WEEK": int,
                      "AIRLINE": "string",
                      "FLIGHT_NUMBER": int,
                      "ORIGIN_AIRPORT": "string",
                      "DESTINATION_AIRPORT": "string",
                      "DEPARTURE_TIME": "string",
                      "ARRIVAL_TIME": "string",
                      "DIVERTED": int,
                      "CANCELLED": int,
                      "ELAPSED_TIME": "string"}

        self.details = pd.read_csv(filename, usecols=columns, dtype=data_types)

        # copy of full data for resetting filters
        self.fullData = self.details.copy()

        # #import airports
        # self.airports = pd.read_csv(airportsfilename, sep=",")
        # self.airports.columns = self.airports.columns.to_series().apply(lambda x: x.strip())
        # self.airports = self.airports[['NAME', 'COUNTRY', 'IATA']]
        # self.fullAirports = self.airports.copy()

        # self.defaultDateF = [[1, 1, 2015], [1, 7, 2015]]
        # # keep track of all current filters
        # # starting date will need to be changed for different datasets
        # self.currentDateF = self.defaultDateF.copy()
        # self.currentLocationF = None
        # self.currentTimeF = None
        # self.currentStops = 0
        # self.currentPassengerCargoF = None
        # self.currentSpecificAirlineF = None
        # self.currentAddedFlightsF = None
        # self.currentRemovedFlightsF = None

        # # filter to default time frame
        # self.changeDateFrame(self.currentDateF[1], self.currentDateF[2])

    def __init__(self, filename, airportsfilename):
        columns = ["YEAR", "MONTH", "DAY", "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER",
                   "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "DEPARTURE_TIME",
                   "DIVERTED", "CANCELLED", "ARRIVAL_TIME", "ELAPSED_TIME"]

        data_types = {"YEAR": int,
                      "MONTH": int,
                      "DAY": int,
                      "DAY_OF_WEEK": int,
                      "AIRLINE": "string",
                      "FLIGHT_NUMBER": int,
                      "ORIGIN_AIRPORT": "string",
                      "DESTINATION_AIRPORT": "string",
                      "DEPARTURE_TIME": "string",
                      "ARRIVAL_TIME": "string",
                      "DIVERTED": int,
                      "CANCELLED": int,
                      "ELAPSED_TIME": "string"}

        self.details = pd.read_csv(filename, usecols=columns, dtype=data_types)

        # copy of full data for resetting filters
        self.fullData = self.details.copy()

        #import airports
        self.airports = pd.read_csv(airportsfilename, sep=",")
        self.airports.columns = self.airports.columns.to_series().apply(lambda x: x.strip())
        self.airports = self.airports[['NAME', 'COUNTRY', 'IATA']]
        self.fullAirports = self.airports.copy()

        self.defaultDateF = [[1, 1, 2015], [1, 7, 2015]]
        # keep track of all current filters
        # starting date will need to be changed for different datasets
        self.currentDateF = self.defaultDateF.copy()
        self.currentLocationF = None
        self.currentTimeF = None
        self.currentStops = 0
        self.currentPassengerCargoF = None
        self.currentSpecificAirlineF = None
        self.currentAddedFlightsF = None
        self.currentRemovedFlightsF = None

        # filter to default time frame
        self.changeDateFrame(self.currentDateF[1], self.currentDateF[2])

    def removeCancelledFlights(self):
        self.details = self.details[self.details['DIVERTED'] == 0]
        self.details = self.details[self.details['CANCELLED'] == 0]

    # change time frame of flights to flights between date1 and date2
    # date1 and date2 are lists list containing [month, day, year]
    # note: THIS CLEARS ALL OTHER FILTERS, THEY WILL NEED TO BE REAPPLIED
    def changeDateFrame(self, date1, date2):
        # add error handling later for invalid dates

        # copy original flight dataset, apply date range filter
        if (date1[2] == date2[2]):
            if (date1[0] == date2[0]):
                if (date1[1] == date2[1]):
                    # same day case
                    self.details = self.details[self.details["YEAR"] == date1[2] &
                                                self.details["MONTH"] == date1[0] & self.details["DAY"] == date1[1]]
                else:
                    # different day, same month and year
                    self.details = self.details[((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date1[0])
                                                 & (self.details["DAY"] >= date1[1]) & (self.details["DAY"] <= date2[1])
                                                 )]
            else:
                # different day and month, same year
                self.details = self.details[(((self.details["YEAR"] == date1[0]) & (self.details["MONTH"] > date1[0]) & (self.details['MONTH'] < date2[0]))
                                             | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date1[0]) & (self.details["DAY"] >= date1[1]))
                                             | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date2[0]) & (self.details["DAY"] <= date2[1]))
                                             )]
        else:
            # different day/month/year
            self.details = self.details[(((self.details["YEAR"] > date1[2]) & (self.details["YEAR"] < date2[2]))
                                         | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] > date1[0]))
                                         | ((self.details["YEAR"] == date2[2]) & (self.details["MONTH"] < date2[0]))
                                         | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date1[0]) & (self.details["DAY"] >= date1[1]))
                                         | ((self.details["YEAR"] == date2[2]) & (self.details["MONTH"] == date2[0]) & (self.details["DAY"] <= date2[1]))
                                         )]

        self.currentDateF = [date1, date2]
        self.currentLocationF = None
        self.currentTimeF = None
        self.currentStops = 0
        self.currentPassengerCargoF = None
        self.currentSpecificAirlineF = None
        self.currentAddedFlightsF = None
        self.currentRemovedFlightsF = None

    # resets date frame to first week of year
    def resetDateFrame(self):
        self.changeDateFrame([1, 1, 2015], [1, 7, 2015])

    # filters data based on origin and destination location
    # typeOrigin and typeDest will be "airport", "country", or "continent"
    # locationListOrigin and locationListDest are lists of the airports, countries, or continents

    def filterByLocation(self, typeOrigin="airport", locationListOrigin=[], typeDest="airport", locationListDest=[]):
        # add error handling later for invalid locations

        # filter origin location first
        if (len(locationListOrigin) > 0):
            if (typeOrigin == "airport"):
                self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(
                    locationListOrigin)]
            elif (typeOrigin == "country"):
                # DOES NOT WORK YET, WILL FIX WHEN BETTER DATA ACQUIRED
                '''
                self.airports = self.fullAirports.copy()
                #get list of all airports in a given country
                self.airports = self.airports[self.airports["COUNTRY"].isin(locationListOrigin)]
                print(self.airports)
                self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(self.airports["COUNTRY"])]
                '''

            else:
                "s"

        # filter destination location
        if (len(locationListDest) > 0):
            if (typeDest == "airport"):

                self.details = self.details[self.details["DESTINATION_AIRPORT"].isin(
                    locationListOrigin)]
            elif (typeDest == "country"):
                "s"
            else:
                "s"

        currentLocationF = [typeOrigin,
                            locationListOrigin, typeDest, locationListDest]

    # the hardest thing
    # def locationWithStops(self, typeOrigin, locationListOrigin, typeDest, locationListDest, maxStops):

    # filters between 2 times from 0000 to 2359
    # time1 and time2 are 4 digit ints between 0000 and 2359

    def filterByTime(self, time1, time2):
        # add error handling later
        start = time1[:2] + time1[3:]
        end = time2[:2] + time2[3:]

        self.details = self.details[((self.details["DEPARTURE_TIME"] >= str(start)) &
                                     (self.details["DEPARTURE_TIME"] <= str(end)))]

        self.currentTimeF = [time1, time2]

    # filters specific days of the week
    # days is a list of 7 values of either 1 or 0, with 1 representing a day being selected

    def filterByDayOfWeek(self, days):
        # get actual numerical values for days
        selectedDays = []
        for k in (days.keys()):
            if (days[k]):
                selectedDays.append(k)

        self.details = self.details[self.details["DAY_OF_WEEK"].isin(
            selectedDays)]

    # def passengerCargoFilter(self, pOrC):
    # need to put some more thought into this

    # filters for specific airlines
    # airline list is a list of IATA codes

    def filterByAirline(self, airlineList):
        self.details = self.details[self.details["AIRLINE"].isin(airlineList)]

    # resets all filters

    def resetFilters(self):
        self.details = self.fullData.copy()

    def filterByAdded(self, beginTime1, beginTime2, endTime1, endTime2):
        self.changeDateFrame(beginTime1, beginTime2)
        beginFrame = self.details.copy()

        self.resetDateFrame()

        self.changeDateFrame(endTime1, endTime2)

    def filterRemovedFlights(self, beginTime1, beginTime2, endTime1, endTime2):
        self.changeDateFrame(beginTime1, beginTime2)
        beginFrame = self.details.copy()

        self.resetDateFrame()

        self.changeDateFrame(endTime1, endTime2)

        endframe = self.details.copy()
    # prints first numRows rows

    def printRows(self, numRows):
        if (numRows == 0):
            print(self.details)
        else:
            print(self.details.head(numRows))


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
