import json


class Request:
    # TODO -- validate that I did everything right here
    def __init__(self, json_request):
        self.details = self.parse_cookie(json_request)

        self.originType = self.details['departure_location_type']
        self.originValues = self.details['departure_location_values']

        self.destType = self.details['arrival_location_type']
        self.destValues = self.details['arrival_location_values']

        self.dayOfWeek = self.details['day_of_week']
        self.numLayovers = self.details['max_layovers']
        self.airlines = self.details['airlines']
        self.isCargo = self.details['cargo']
        self.isPassenger = self.details['passenger']

        # TODO -- temp values for now this probably won't work
        # self.advancedRequest = AdvancedRequest(self.details['departure_time'], self.details['arrival_time'], None)

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
            'sunday': cookie[4],
            'monday': cookie[5],
            'tuesday': cookie[6],
            'wednesday': cookie[7],
            'thursday': cookie[8],
            'friday': cookie[9],
            'saturday': cookie[10]
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
