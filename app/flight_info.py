"""FlightInfo class
    Attributes:
        details: dataframe containing all flight info"""
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
        self.full_data = self.details.copy()

    """
    Filter by origin and destination
    Parameters:
        origin_type: type of origin filter (airport, country, continent)
        origin_values: list of origin values to filter by
        dest_type: type of destination filter (airport, country, continent)
        dest_values: list of destination values to filter by
    """
    def filter_by_location(self, origin_type, origin_values,
                         dest_type, dest_values):
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

    """
    Filter by time
    Parameters:
        start_date: start date of filter
        start_time: start time of filter
        end_date: end date of filter
        end_time: end time of filter
    """
    def filter_by_time(self, start_date, start_time, end_date, end_time):
        parsed_start = start_date + '-' + start_time[:2] + '-' + start_time[2:]
        parsed_end = end_date + '-' + end_time[:2] + '-' + end_time[2:]

        depart_time = datetime.datetime.strptime(parsed_start,
                                                 '%Y-%m-%d-%H-%M')

        arrive_time = datetime.datetime.strptime(parsed_end,
                                                 '%Y-%m-%d-%H-%M')

        self.details = self.details[self.details["DEPARTURE_TIME"] > depart_time]

        self.details = self.details[self.details["ARRIVAL_TIME"] < arrive_time]

    """
    Filter by day of week
    Parameters:
        days: dictionary of days of week to filter by
    """
    def filter_by_day_of_week(self, days):
        selected_days = []
        for k in (days.keys()):
            if days[k] == "true":
                selected_days.append(k)

        # print("Selected Days:", selected_days)
        self.details = self.details[self.details["DAY_OF_WEEK"].isin(
            selected_days)]

    """
    Filter by airline
    Parameters:
        airlines: list of airlines to filter by
    """
    def filter_by_airline(self, airlines):
        self.details = self.details[self.details["AIRLINE"].isin(
            airlines)]

    """
    Filter by cargo or passenger
    Parameters:
        is_cargo: boolean for if cargo flights should be included
        is_passenger: boolean for if passenger flights should be included
    """
    def filter_by_cargo(self, is_cargo, is_passenger):
        if is_cargo == 'true' and is_passenger == 'false':
            self.details = self.details[self.details["CARGO"] == True]
        elif is_cargo == 'false' and is_passenger == 'true':
            self.details = self.details[self.details["CARGO"] == False]
        elif is_cargo == 'false' and is_passenger == 'false':
            self.details = self.details[self.details["CARGO"] == 2]

    """
    Filter by added
    Parameters:
        req: request object containing start and end dates
    """
    def filter_by_added(self, req):
        depart1 = datetime.datetime.strptime(req.start1, '%Y-%m-%d')
        depart2 = datetime.datetime.strptime(req.start2, '%Y-%m-%d')

        arrive1 = datetime.datetime.strptime(req.end1, '%Y-%m-%d')
        arrive2 = datetime.datetime.strptime(req.end2, '%Y-%m-%d')

        flights1 = self.full_data[self.full_data["DEPARTURE_TIME"] > depart1]
        flights1 = self.full_data[self.full_data["ARRIVAL_TIME"] < arrive1]

        flights2 = self.full_data[self.full_data["DEPARTURE_TIME"] > depart2]
        flights2 = self.full_data[self.full_data["ARRIVAL_TIME"] < arrive2]

        self.details = flights2

    """
    Filter by removed
    Parameters:
        req: request object containing start and end dates
    """
    def filter_by_removed(self, req):
        depart1 = datetime.datetime.strptime(req.start1, '%Y-%m-%d')
        # depart2 = datetime.datetime.strptime(req.start2, '%Y-%m-%d')

        arrive1 = datetime.datetime.strptime(req.end1, '%Y-%m-%d')
        # arrive2 = datetime.datetime.strptime(req.end2, '%Y-%m-%d')

        flights1 = self.full_data[(self.full_data["DEPARTURE_TIME"] > depart1)
                                  & (self.full_data["ARRIVAL_TIME"] < arrive1)]
        # flights1 = self.full_data[self.full_data["ARRIVAL_TIME"] < arrive1]

        # flights2 = self.full_data[(self.full_data["DEPARTURE_TIME"] > depart2)
        #                           & (self.full_data["ARRIVAL_TIME"] < arrive2)]
        # flights2 = self.full_data[self.full_data["ARRIVAL_TIME"] < arrive2]

        self.details = flights1
