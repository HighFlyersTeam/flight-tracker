import json


class Request:
    # TODO -- validate that I did everything right here
    def __init__(self, json_request):
        self.details = self.parse_cookie(json_request)

        self.originType = self.details['departure_location_type']
        self.originValues = self.details['departure_location_values']

        self.startDate = self.details['departure_date']
        self.startTime = self.details['departure_time']

        self.endDate = self.details['arrival_date']
        self.endTime = self.details['arrival_time']

        self.destType = self.details['arrival_location_type']
        self.destValues = self.details['arrival_location_values']

        self.dayOfWeek = self.details['day_of_week']
        self.numLayovers = self.details['max_layovers']
        self.airlines = self.details['airlines']
        self.isCargo = self.details['cargo']
        self.isPassenger = self.details['passenger']

        # TODO -- temp values for now this probably won't work
        # self.advancedRequest = AdvancedRequest(self.details['departure_time'], self.details['arrival_time'], None)

    # TODO -- this can all easily be changed to be in whatever format you want
    #      -- this is just a quick and dirty way to get it working
    def parse_cookie(self, cookie):
        to_return = dict()
        cookie = cookie.split('--')
        to_return['departure_date'] = cookie[0]
        to_return['departure_time'] = cookie[1]

        to_return['arrival_date'] = cookie[2]
        to_return['arrival_time'] = cookie[3]

        to_return['day_of_week'] = {
            '7': cookie[4],
            '6': cookie[5],
            '5': cookie[6],
            '4': cookie[7],
            '3': cookie[8],
            '2': cookie[9],
            '1': cookie[10]
        }

        to_return['departure_location_type'] = cookie[11]
        to_return['departure_location_values'] = cookie[12].split('%2C')

        to_return['arrival_location_type'] = cookie[13]
        to_return['arrival_location_values'] = cookie[14].split('%2C')

        to_return['max_layovers'] = cookie[15]

        to_return['airlines'] = cookie[16].split('%2C')

        to_return['cargo'] = cookie[17]
        to_return['passenger'] = cookie[18]

        to_return['advanced_start_date'] = cookie[19]
        to_return['advanced_start_time'] = cookie[20]

        to_return['advanced_end_date'] = cookie[21]
        to_return['advanced_end_time'] = cookie[22]

        to_return['find_added'] = cookie[23]
        to_return['find_removed'] = cookie[24]

        return to_return


class AdvancedRequest:
    def __init__(self, start1, end1, request_details):
        self.start1 = start1
        self.end1 = end1
        self.filterAdded = request_details['find_added']
        if self.filterAdded:
            self.start2 = self.filterAdded['start_info']
            self.end2 = self.filterAdded['end_info']

        self.filterRemoved = request_details['find_removed']
        if self.filterRemoved:
            self.start2 = self.filterAdded['start_info']
            self.end2 = self.filterAdded['end_info']

    def populate(self, request_details):
        self.filterAdded = request_details['find_added']
        if self.filterAdded:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']

        self.filterRemoved = request_details['find_removed']
        if self.filterRemoved:
            self.start = self.filterAdded['start_info']
            self.end = self.filterAdded['end_info']
