"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Read and store the header row

        for line in reader:
            neo_data = {}  # Create a dictionary to store the data for each NEO
            for i, value in enumerate(line):
                neo_data[header[i]] = value  # Use the header as keys and the values from the CSV row

            # Create an instance of the NearEarthObject class using the data and add it to the list
            neo = NearEarthObject(**neo_data)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cads = []
    headers = ['des','orbit_id','jd','cd','dist','dist_min','dist_max','v_rel','v_inf','t_sigma_f','h']

    with open(cad_json_path, 'r') as f:
        data = json.load(f)
        # Create objects from the list of lists

    for item in data['data']:
        # Create a dictionary mapping headers to values
        item_dict = {header: value for header, value in zip(headers, item)}
        close_approach = CloseApproach(**item_dict)
        cads.append(close_approach)
        
    return cads