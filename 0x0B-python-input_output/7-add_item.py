#!/usr/bin/python3
import sys
""" This is a script that adds all arguments in the command line
    to a python list and save in a file"""

encoder = __import__("5-save_to_json_file").save_to_json_file
decoder = __import__("6-load_from_json_file").load_from_json_file

try:
    list_object = decoder("add_item.json")
except FileNotFoundError:
    list_object = []

list_object.extend(sys.argv[1:])
encoder(list_object, "add_item.json")
