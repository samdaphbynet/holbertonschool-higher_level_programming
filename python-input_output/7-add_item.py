#!/usr/bin/python3
"""
script that adds all arguments to a Python list
"""
import sys
import os
save_to_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

data = load_from_json_file(filename) if os.path.exists(filename) else []
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_file(data, filename)
