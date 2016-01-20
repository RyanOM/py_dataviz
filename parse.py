# Code based on the DataViz tutorial that can be found here: http://newcoder.io/dataviz/part-1/

import csv

MY_DATA_FILE = './data/sample_sfpd_incident_all.csv'


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV File
    opened_file.close()

    return parsed_data


def main():
    my_json_data = parse(MY_DATA_FILE, ',')
    print(my_json_data)


if __name__ == "__main__":
    main()
