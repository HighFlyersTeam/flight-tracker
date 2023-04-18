"""This file contains the Request class, which is used to parse the request from the frontend"""


class Request:
    """
    This class is used to parse the request from the frontend
    """

    def __init__(self, json_request):
        self.details = self.parse_cookie(json_request)

        self.origin_type = self.details["departure_location_type"]
        self.origin_values = self.details["departure_location_values"]

        self.start_date = self.details["departure_date"]
        self.start_time = self.details["departure_time"]

        self.end_date = self.details["arrival_date"]
        self.end_time = self.details["arrival_time"]

        self.dest_type = self.details["arrival_location_type"]
        self.dest_values = self.details["arrival_location_values"]

        self.day_of_week = self.details["day_of_week"]
        self.num_layovers = self.details["max_layovers"]
        self.airlines = self.details["airlines"]
        self.is_cargo = self.details["cargo"]
        self.is_passenger = self.details["passenger"]

        self.adv_req = AdvancedRequest(
            self.details["advanced_start_date"],
            self.details["advanced_start_time"],
            self.details["advanced_end_date"],
            self.details["advanced_end_time"],
            self.details["find_added"],
            self.details["find_removed"],
        )

    def parse_cookie(self, cookie):
        """
        Parse the cookie from the frontend
        Parameters:
            cookie: the cookie from the frontend
        """
        to_return = {}
        cookie = cookie.split("--")
        to_return["departure_date"] = cookie[0]
        to_return["departure_time"] = cookie[1]

        to_return["arrival_date"] = cookie[2]
        to_return["arrival_time"] = cookie[3]

        to_return["day_of_week"] = {
            "7": cookie[4],
            "6": cookie[5],
            "5": cookie[6],
            "4": cookie[7],
            "3": cookie[8],
            "2": cookie[9],
            "1": cookie[10],
        }

        to_return["departure_location_type"] = cookie[11]
        to_return["departure_location_values"] = cookie[12].split("%2C")

        to_return["arrival_location_type"] = cookie[13]
        to_return["arrival_location_values"] = cookie[14].split("%2C")

        to_return["max_layovers"] = cookie[15]

        to_return["airlines"] = cookie[16].split("%2C")

        to_return["cargo"] = cookie[17]
        to_return["passenger"] = cookie[18]

        to_return["advanced_start_date"] = cookie[19]
        to_return["advanced_start_time"] = cookie[20]

        to_return["advanced_end_date"] = cookie[21]
        to_return["advanced_end_time"] = cookie[22]

        to_return["find_added"] = cookie[23]
        to_return["find_removed"] = cookie[24]

        print("\n\nFrontend Request:\n", to_return)
        return to_return


class AdvancedRequest:
    """
    This class is used to parse the advanced request from the frontend
    """

    def __init__(self, start_date, start_time, end_date, end_time, added, removed):
        self.filter_added = added
        self.filter_removed = removed

        if self.filter_added == "true":
            self.start_date = start_date
            self.start_time = start_time
            self.end_date = end_date
            self.end_time = end_time
        elif self.filter_removed == "true":
            self.start_date = start_date
            self.start_time = start_time
            self.end_date = end_date
            self.end_time = end_time

    def populate(self, request_details):
        """
        Populate the advanced request
        Parameters:
            request_details: the details of the request
        """
        self.filter_added = request_details["find_added"]
        if self.filter_added:
            self.start = self.filter_added["start_info"]
            self.end = self.filter_added["end_info"]

        self.filter_removed = request_details["find_removed"]
        if self.filter_removed:
            self.start = self.filter_added["start_info"]
            self.end = self.filter_added["end_info"]
