import csv
import chardet
from datetime import datetime

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

def read_flight_data(file_path):
    encoding = detect_encoding(file_path)

    with open(file_path, 'r', encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file)
        header = reader.fieldnames

        data = []
        for row in reader:
            time_str = row['TIME']
            time = datetime.strptime(time_str, '%H:%M:%S:%f').time()

            roll = float(row.get('ROLL(DEG)', 0.0))
            pitch = float(row.get('PITCH(DEG)', 0.0))
            true_heading = float(row.get('TRUE HEADING(DEG)', 0.0))
            longitude = float(row.get('LONGITUDE', 0.0))
            latitude = float(row.get('LATITUDE', 0.0))
            altitude = float(row.get('ALTITUDE(METERS)', 0.0))

            data.append({
                'TIME': time,
                'ROLL': roll,
                'PITCH': pitch,
                'TRUE HEADING': true_heading,
                'LONGITUDE': longitude,
                'LATITUDE': latitude,
                'ALTITUDE': altitude
            })

    return header, data


file_path = '/Users/rajdeepjaiswal/Documents/2023-07-04-09-36-14-5325-NAVIGATION.csv'
header, data = read_flight_data(file_path)

print("Header:")
print(header)

print("\nData:")
for row in data:
    print(row)

