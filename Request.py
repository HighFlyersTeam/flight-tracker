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

        self.advancedRequest = AdvancedRequest(self.originInfo['time'], self.destInfo['time'],
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
