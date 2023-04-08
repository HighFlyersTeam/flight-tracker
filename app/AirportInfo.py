import csv
import json

country_data = json.load(open("./data/countries.json", encoding="utf8"))


def get_country_code(country):
    # Due to differences in the data sets
    if country == "North Korea":
        country = "Korea (Democratic People's Republic of"
    elif country == "South Korea":
        country = "Korea, Republic of"
    elif country == "Laos":
        country = "Lao People's Democratic Republic"
    elif country == "British Virgin Islands":
        country = "Virgin Islands (British)"
    elif country == "Macau":
        country = "Macao"
    elif country == "Congo (Brazzaville)":
        country = "Congo"
    elif country == "Congo (Kinshasa)":
        country = "Congo, Democratic Republic of the"
    elif country == "Czech Republic":
        country = "Czechia"
    elif country == "Reunion":
        country = "Réunion"
    elif country == "Cape Verde":
        country = "Cabo Verde"

    for item in country_data:
        if country.strip().upper() in item["name"].strip().upper():
            return item["alpha-2"]
    return None


data = dict()
indent = 4
with open("./data/airports.dat.txt", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        current_airport = dict()
        current_airport["name"] = row[1]
        current_airport["city"] = row[2]

        # Airport dataset is a bit old
        if row[3] == "Burma":
            current_airport["country"] = "Myanmar"
        elif row[3] == "Netherlands Antilles":
            current_airport["country"] = "Netherlands"
        else:
            current_airport["country"] = row[3]

        current_airport["country_code"] = get_country_code(current_airport["country"])
        current_airport["lat"] = float(row[6])
        current_airport["lng"] = float(row[7])

        icao_code = row[5]
        data[icao_code] = current_airport

json_object = json.dumps(data, indent=indent)

with open("./static/airports.json", "w") as file:
    file.write(json_object)
