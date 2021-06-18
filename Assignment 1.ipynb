import sys
from datetime import datetime
import pytz
import tzlocal
import os
import csv
import pathlib


'''
Timestamp format changer.
UTC to IST.
'''
def utc_to_ist(timestamp):
    local_timezone = tzlocal.get_localzone()

    # parse given timestamp string to create datetime object.
    utc_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    # fetch back new timestamp.
    new_timestamp = local_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    return new_timestamp



#from utc_to_ist import utc_to_ist

current_directory = os.path.dirname(os.path.realpath('__file__'))
csv_file_path = os.path.join(current_directory, 'sample.csv')

# open and read csv file.
with open(csv_filepath, "r") as f:
    csv_reader = csv.DictReader(f)  # read the file as dictionary
    data = list(csv_reader)

given_timestamp = (data[len(data) - 1].get('Value'))  # extracting timestamp.
new_timestamp = utc_to_ist(given_timestamp)  # convert the timestamp from UTC format to IST format.

data = data[:-1]

# Given Key Mapping is stored as dictionary.
mapping = {
    "M_ID": "machineId",
    "P_PART": "partNumber",
    "M_STATE": "machineStatus",
    "NOZZLE_TEMP": "nozzleTemp",
    "ZONE_TEMP": "zoneTemp",
    "C_TIME": "cycleTime",
    "POWER": "powerConsumption",
    "TS": "timestamp"}


'''
- Replace values from "mapping" dictionary.
- Rename key name.
- Replace new formatted timestamp i.e, UTC to IST.

'''

def convert(d):
    for i in d:
        a = []
        i.pop("")
        i["param_name"] = mapping[i.pop("Name")] 
        i["param_value"] = i.pop("Value") 
        i["timestamp"] = new_timestamp
        print(i)

        
convert(data)


'''
Expected Output :

    {'param_name': 'machineId', 'param_value': '30001006', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'partNumber', 'param_value': 'Test Part', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'machineStatus', 'param_value': 'red', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'nozzleTemp', 'param_value': '25', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'zoneTemp', 'param_value': '200', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'cycleTime', 'param_value': '65.6', 'timestamp': '2021-04-20T16:30:00+0530'}
    {'param_name': 'powerConsumption', 'param_value': '3245.67', 'timestamp': '2021-04-20T16:30:00+0530'}
'''
