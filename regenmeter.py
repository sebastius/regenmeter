#!/usr/bin/env python3

import requests
import csv

# Fetching the data from the URL
url = 'https://gpsgadget.buienradar.nl/data/raintext/?lat=51lon=3'
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Reading the text data
    data = response.text

    # Parsing the text data and splitting it into lines
    lines = data.splitlines()

    # Extracting rain and time data, calculating 'calculated_rain' values
    rain_data = [(int(line.split('|')[0]), line.split('|')[1]) for line in lines]
    calculated_rain = [round(10**((rain - 109) / 32), 2) for rain, _ in rain_data]

    # Writing data to a CSV file
    with open('/home/bas/regenmeter/rain_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Writing headers
        csv_writer.writerow(['rain', 'time', 'calculated_rain'])
        # Writing data rows
        for i in range(len(rain_data)):
            csv_writer.writerow([rain_data[i][0], rain_data[i][1], calculated_rain[i]])

    print("CSV file 'rain_data.csv' has been created successfully.")
else:
    print("Failed to fetch data from the URL.")
