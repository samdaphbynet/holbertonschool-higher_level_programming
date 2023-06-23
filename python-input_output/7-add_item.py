#!/usr/bin/python3
import sys
save_to_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # load existing data from file if it exists
    data = load_from_json_file(filename)
except FileNotFoundError:
    # create an empty list if the file doesn't exist
    data = []
# add command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_file(data, filename)
