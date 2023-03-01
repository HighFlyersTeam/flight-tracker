import pandas as pd
import datetime







class FlightInfo:
    def __init__(self, filename, airportsfilename):
        self.columns = ["YEAR", "MONTH", "DAY", "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER", 
                        "ORIGIN_AIRPORT", "DESTINATION_AIRPORT","DEPARTURE_TIME",
                        "DIVERTED","CANCELLED","ARRIVAL_TIME", "ELAPSED_TIME"]

        self.data_types = { "YEAR": int, 
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

        self.details = pd.read_csv( filename, usecols = self.columns, dtype = self.data_types)

        #copy of full data for resetting filters    
        self.fullData = self.details.copy()

        #import airports
        self.airports = pd.read_csv(airportsfilename, sep = ",")
        self.airports.columns = self.airports.columns.to_series().apply(lambda x: x.strip())
        self.airports = self.airports[['NAME', 'COUNTRY', 'IATA']]
        self.fullAirports = self.airports.copy()

        self.defaultDateF = [[1,1,2015], [1,7,2015]]
        #keep track of all current filters
        #starting date will need to be changed for different datasets
        self.currentDateF = self.defaultDateF.copy()
        self.currentLocationF = None
        self.currentTimeF = None
        self.currentStops = 0
        self.currentPassengerCargoF = None
        self.currentSpecificAirlineF = None
        self.currentAddedFlightsF = None
        self.currentRemovedFlightsF = None

        #filter to default time frame
        self.changeDateFrame(self.currentDateF[1], self.currentDateF[2])



    def removeCancelledFlights(self):
        self.details = self.details[self.details['DIVERTED'] == 0]
        self.details = self.details[self.details['CANCELLED'] == 0]

    #change time frame of flights to flights between date1 and date2
    #date1 and date2 are lists list containing [month, day, year]
    #note: THIS CLEARS ALL OTHER FILTERS, THEY WILL NEED TO BE REAPPLIED
    def changeDateFrame(self, date1, date2):
        #add error handling later for invalid dates


        #copy original flight dataset, apply date range filter
        self.details = self.fullData.copy()
        
        if(date1[2] == date2[2]):
            if(date1[0] == date2[0]):
                if(date1[1] == date2[1]):
                    #same day case
                    self.details = self.details[self.details["YEAR"] == date1[2] & self.details["MONTH"] == date1[0] & self.details["DAY"] == date1[1]]
                else:
                    #different day, same month and year
                    self.details = self.details[((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date1[0]) 
                        & (self.details["DAY"] >= date1[1]) & (self.details["DAY"] <= date2[1])
                        )]
            else:
                #different day and month, same year
                self.details = self.details[(((self.details["YEAR"] == date1[0]) & (self.details["MONTH"] > date1[0]) & (self.details['MONTH'] < date2[0]))
                    | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date1[0]) & (self.details["DAY"] >= date1[1]))
                    | ((self.details["YEAR"] == date1[2]) & (self.details["MONTH"] == date2[0]) & (self.details["DAY"] <= date2[1]))
                    )]
        else:
            #different day/month/year
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



    #resets date frame to first week of year
    def resetDateFrame(self):
        self.changeDateFrame([1,1,2015], [1,7,2015])


    #filters data based on origin and destination location
    #typeOrigin and typeDest will be "airport", "country", or "continent"
    #locationListOrigin and locationListDest are lists of the airports, countries, or continents
    def locationFilter(self, typeOrigin = "airport", locationListOrigin = [], typeDest = "airport", locationListDest = []):
        #add error handling later for invalid locations





        #filter origin location first
        if(len(locationListOrigin) > 0):
            if(typeOrigin == "airport"):
                self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(locationListOrigin)]
            elif(typeOrigin == "country"):
                #DOES NOT WORK YET, WILL FIX WHEN BETTER DATA ACQUIRED
                '''
                self.airports = self.fullAirports.copy()
                #get list of all airports in a given country
                self.airports = self.airports[self.airports["COUNTRY"].isin(locationListOrigin)]
                print(self.airports)
                self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(self.airports["COUNTRY"])]
                '''

            else:
                "s"




        #filter destination location
        if(len(locationListDest) > 0):
            if(typeDest == "airport"):

                self.details = self.details[self.details["DESTINATION_AIRPORT"].isin(locationListOrigin)]
            elif(typeDest == "country"):
                "s"
            else:
                "s"

        currentLocationF = [typeOrigin, locationListOrigin, typeDest, locationListDest]



    #the hardest thing
    #def locationWithStops(self, typeOrigin, locationListOrigin, typeDest, locationListDest, maxStops):



    #filters between 2 times from 0000 to 2359
    #time1 and time2 are 4 digit ints between 0000 and 2359
    def timeOfDayFilter(self, time1, time2):
        #add error handling later


        self.details = self.details[((self.details["DEPARTURE_TIME"] >= str(time1)) & 
            (self.details["DEPARTURE_TIME"] <= str(time2)))]

        self.currentTimeF = [time1, time2]


    #filters specific days of the week
    #days is a list of 7 values of either 1 or 0, with 1 representing a day being selected
    def dayOfWeekFilter(self, days):
        #get actual numerical values for days
        selectedDays = []
        for i in range(len(days)):
            if(days[i] == 1):
                selectedDays.append(i+1)

        self.details = self.details[self.details["DAY_OF_WEEK"].isin(selectedDays)]




    #def passengerCargoFilter(self, pOrC):
    #need to put some more thought into this



    #filters for specific airlines
    #airline list is a list of IATA codes
    def specificAirlineFilter(self, airlineList):
        self.details = self.details[self.details["AIRLINE"].isin(airlineList)]


    #resets all filters
    def resetFilters(self):
        self.changeDateFrame(currentDateF[1], currentDateF[2])




    def filterAddedFlights(self, beginTime1, beginTime2, endTime1, endTime2):
        self.changeDateFrame(beginTime1, beginTime2)
        beginFrame = self.details.copy()

        self.resetDateFrame()

        self.changeDateFrame(endTime1, endTime2)

        endframe = self.details.copy()

    #def filterRemovedFlights(self, beginTime1, beginTime2, endTime1, endTime2):






    #prints first numRows rows
    def printRows(self, numRows):
        if(numRows == 0):
            print(self.details)
        else:
            print(self.details.head(numRows))








class Flight:
    def __init__(self, flightInfo):
        self.flightTime = int(flightInfo["ELAPSED_TIME"])

        self.departureTime = datetime.datetime( year = int(flightInfo["YEAR"]),
                                                month = int(flightInfo["MONTH"]),
                                                day = int(flightInfo["DAY"]),
                                                hour = int(flightInfo["DEPARTURE_TIME"].zfill(4)[:2]),
                                                minute = int(flightInfo["DEPARTURE_TIME"].zfill(4)[2:]))

        self.arrivalTime = self.departureTime + datetime.timedelta(minutes = self.flightTime)

        self.origin = flightInfo["ORIGIN_AIRPORT"]
        self.destination = flightInfo["DESTINATION_AIRPORT"]

    def __str__(self):
        ret_val =  "\nOrigin: " + self.origin + "\n"
        ret_val += "Destination: " + self.destination + "\n" 
        ret_val += "Departure Time: "+ self.departureTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Arrival Time: " + self.arrivalTime.strftime("%m/%d/%Y %H:%M") + "\n"
        ret_val += "Flight Time: " + str(self.flightTime) + " minutes"

        return ret_val









#some tests
def testDateFilter(f):
    f.printRows(0)
    f.changeDateFrame([9,1,2015],[10,7,2015])
    f.printRows(0)
    f.resetDateFrame()
    f.printRows(0)

def testLocationFilter(f):
    f.printRows(0)
    f.locationFilter("airport", ["LAX"])
    f.printRows(0)
    f.resetDateFrame()
    '''
    f.locationFilter("country", ["United States"])
    f.printRows(0)
    '''

def testTimeFilter(f):
    f.printRows(0)
    f.timeOfDayFilter(1200,2359)
    f.printRows(0)

def testWeekdayFilter(f):
    f.printRows(0)
    f.dayOfWeekFilter([1,0,0,0,0,0,1])
    f.printRows(0)

def testSpecificAirlines(f):
    f.printRows(0)
    f.specificAirlineFilter(["AA", "DL"])
    f.printRows(0)




f = FlightInfo("data/2015 flights.csv", "data/airports.txt")
#testDateFilter(f)
#testLocationFilter(f)
#testTimeFilter(f)
#testWeekdayFilter(f)
#testSpecificAirlines(f)