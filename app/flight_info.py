"""flight info module for flight info class"""
import datetime
import pandas as pd


class FlightInfo:
    """
    FlightInfo class
    Attributes:
        details: pandas dataframe with flight details
    """
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
        self.full_data = self.details.copy()

    def filter_by_location(self,
                           origin_type,
                           origin_values,
                           dest_type,
                           dest_values):
        """
        Filter by origin and destination
        Parameters:
            origin_type: type of origin filter (airport, country, continent)
            origin_values: list of origin values to filter by
            dest_type: type of destination filter (airport, country, continent)
            dest_values: list of destination values to filter by
        """

        for i in origin_values:
            if(i == 'NA'):
                origin_values.remove(i)
                origin_values.append("UA")
        for i in dest_values:
            if(i == 'NA'):
                dest_values.remove(i)
                dest_values.append("UA")

        if origin_type == 'airport':
            self.details = self.details[self.details["ORIGIN_AIRPORT"].isin(
                origin_values)]
        elif origin_type == 'country':
            self.details = self.details[self.details["ORIGIN_COUNTRY"].isin(
                origin_values)]
        elif origin_type == 'continent':
            self.details = self.details[self.details["ORIGIN_CONTINENT"].isin(
                origin_values)]

        if dest_type == 'airport':
            self.details = self.details[self.details["DESTINATION_AIRPORT"].isin(
                dest_values)]
        elif dest_type == 'country':
            self.details = self.details[self.details["DESTINATION_COUNTRY"].isin(
                dest_values)]
        elif dest_type == 'continent':
            self.details = self.details[self.details["DESTINATION_CONTINENT"].isin(
                dest_values)]




    def filter_by_time(self,
                       start_date,
                       start_time,
                       end_date,
                       end_time):
        """
        Filter by time
        Parameters:
            start_date: start date of filter
            start_time: start time of filter
            end_date: end date of filter
            end_time: end time of filter
        """
        parsed_start = start_date + '-' + start_time[:2] + '-' + start_time[2:]
        parsed_end = end_date + '-' + end_time[:2] + '-' + end_time[2:]

        depart_time = datetime.datetime.strptime(parsed_start,
                                                 '%Y-%m-%d-%H-%M')

        arrive_time = datetime.datetime.strptime(parsed_end,
                                                 '%Y-%m-%d-%H-%M')

        self.details = self.details[self.details["DEPARTURE_TIME"] > depart_time]

        self.details = self.details[self.details["ARRIVAL_TIME"] < arrive_time]

    def filter_by_day_of_week(self, days):
        """
        Filter by day of week
        Parameters:
            days: dictionary of days of week to filter by
        """
        selected_days = []
        for k in (days.keys()):
            if days[k] == "true":
                selected_days.append(k)

        self.details = self.details[self.details["DAY_OF_WEEK"].isin(
            selected_days)]

    def filter_by_airline(self, airlines):
        """
        Filter by airline
        Parameters:
            airlines: list of airlines to filter by
        """
        self.details = self.details[self.details["AIRLINE"].isin(
            airlines)]

    def filter_by_cargo(self, is_cargo, is_passenger):
        """
        Filter by cargo or passenger
        Parameters:
            is_cargo: boolean for if cargo flights should be included
            is_passenger: boolean for if passenger flights should be included
        """
        if is_cargo == 'true' and is_passenger == 'false':
            self.details = self.details[self.details["CARGO"] == 1]
        elif is_cargo == 'false' and is_passenger == 'true':
            self.details = self.details[self.details["CARGO"] == 0]

    def filter_by_added(self, req):
        """
        Filter by added
        Parameters:
            req: request object containing start and end dates
        """
        parsed_start1 = req.start_date + '-' + \
            req.start_time[:2] + '-' + req.start_time[2:]
        parsed_end1 = req.end_date + '-' + \
            req.end_time[:2] + '-' + req.end_time[2:]

        parsed_start2 = req.adv_req.start_date + '-' + \
            req.adv_req.start_time[:2] + '-' + req.adv_req.start_time[2:]
        parsed_end2 = req.adv_req.end_date + '-' + \
            req.adv_req.end_time[:2] + '-' + req.adv_req.end_time[2:]

        depart1 = datetime.datetime.strptime(parsed_start1, '%Y-%m-%d-%H-%M')
        arrive1 = datetime.datetime.strptime(parsed_end1, '%Y-%m-%d-%H-%M')

        depart2 = datetime.datetime.strptime(parsed_start2, '%Y-%m-%d-%H-%M')
        arrive2 = datetime.datetime.strptime(parsed_end2, '%Y-%m-%d-%H-%M')

        flights1 = self.details[(self.details["DEPARTURE_TIME"] > depart1)
                                & (self.details["ARRIVAL_TIME"] < arrive1)]

        flights2 = self.full_data[(self.full_data["DEPARTURE_TIME"] > depart2)
                                  & (self.full_data["ARRIVAL_TIME"] < arrive2)]
        flights2 = flights2[flights2["AIRLINE"].isin(req.airlines)]

        # time_delta = pd.to_timedelta(depart2-depart1)
        added_flights = flights2.copy()
        for index, f in flights2.iterrows():
            # check_time = (f["DEPARTURE_TIME"] - time_delta)
            temp = flights1[(flights1["DAY_OF_WEEK"] == f["DAY_OF_WEEK"])
                            & (flights1["HOUR"] == f["HOUR"])
                            & (flights1["MINUTE"] == f["MINUTE"])
                            & (flights1["AIRLINE"] == f["AIRLINE"])
                            & (flights1["ORIGIN_AIRPORT"] == f["ORIGIN_AIRPORT"])
                            & (flights1["DESTINATION_AIRPORT"] == f["DESTINATION_AIRPORT"])]
            if temp.shape[0] > 0:
                added_flights.drop(index, inplace=True)

        self.details = added_flights

    def filter_by_removed(self, req):
        """
        Filter by removed
        Parameters:
            req: request object containing start and end dates
        """
        parsed_start1 = req.start_date + '-' + \
            req.start_time[:2] + '-' + req.start_time[2:]
        parsed_end1 = req.end_date + '-' + \
            req.end_time[:2] + '-' + req.end_time[2:]

        parsed_start2 = req.adv_req.start_date + '-' + \
            req.adv_req.start_time[:2] + '-' + req.adv_req.start_time[2:]
        parsed_end2 = req.adv_req.end_date + '-' + \
            req.adv_req.end_time[:2] + '-' + req.adv_req.end_time[2:]

        depart1 = datetime.datetime.strptime(parsed_start1, '%Y-%m-%d-%H-%M')
        arrive1 = datetime.datetime.strptime(parsed_end1, '%Y-%m-%d-%H-%M')

        depart2 = datetime.datetime.strptime(parsed_start2, '%Y-%m-%d-%H-%M')
        arrive2 = datetime.datetime.strptime(parsed_end2, '%Y-%m-%d-%H-%M')

        flights1 = self.details[(self.details["DEPARTURE_TIME"] > depart1)
                                & (self.details["ARRIVAL_TIME"] < arrive1)]

        flights2 = self.full_data[(self.full_data["DEPARTURE_TIME"] > depart2)
                                  & (self.full_data["ARRIVAL_TIME"] < arrive2)]
        flights2 = flights2[flights2["AIRLINE"].isin(req.airlines)]

        # time_delta = pd.to_timedelta(depart2-depart1)
        removed_flights = flights1.copy()
        for index, f in flights1.iterrows():
            # check_time = (f["DEPARTURE_TIME"] + time_delta)
            temp = flights2[(flights2["DAY_OF_WEEK"] == f["DAY_OF_WEEK"])
                            & (flights2["HOUR"] == f["HOUR"])
                            & (flights2["MINUTE"] == f["MINUTE"])
                            & (flights2["AIRLINE"] == f["AIRLINE"])
                            & (flights2["ORIGIN_AIRPORT"] == f["ORIGIN_AIRPORT"])
                            & (flights2["DESTINATION_AIRPORT"] == f["DESTINATION_AIRPORT"])]
            if temp.shape[0] > 0:
                removed_flights.drop(index, inplace=True)

        self.details = removed_flights

    def stop_helper(self,stops,airports):
        
        return

    def filter_by_stops(self, stops):
        """
        Filter by stops
            parameters:
                stops: number of stops
        """
        if(stops == 0):
            return
        
        
