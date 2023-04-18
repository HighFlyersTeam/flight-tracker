"""module for filtering flight data by time"""
from datetime import datetime


def filter_flights_by_time(flight_data, start_time, end_time):
    """
    Filter flight data by time
    :param flight_data:
    :param start_time:
    :param end_time:
    :return:
    """
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

    # Create an empty list to hold filtered flight data
    filtered_data = []

    # Loop through each flight in the input list
    for flight in flight_data:
        # Convert flight departure time string to datetime object
        departure_time = datetime.strptime(flight["departure_time"], "%Y-%m-%d %H:%M")

        # If the flight departure time is within the specified time frame,
        # add it to the filtered data list
        if start_time <= departure_time <= end_time:
            filtered_data.append(flight)

    # Return the filtered data list
    return filtered_data
