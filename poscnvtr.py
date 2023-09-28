#!/usr/bin/env python3
"""APRS/UI-View POS file converter"""

import argparse
from datetime import datetime, timezone
from location import loc_from_pos

parser = argparse.ArgumentParser(description="APRS/UI-View POS converter")
parser.add_argument("input", help="APRS/UI-View POS file to read")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-x", "--xastir", action="store_true",help="output Xastir format")
group.add_argument("-j", "--json", action="store_true",help="output RadarScope JSON")
parser.add_argument("--current_time", action="store_true",
                    help="Use current UTC time for timestamp field")

args = parser.parse_args()

def output_json(locs):
    """Print given locations in JSON format"""
    print('[')
    for location in locs:
        print(f'    {location.json_str()},')
    print(']')

def current_timestamp() -> str:
    """Get the current UTC time in HHMMSSz format"""
    now = datetime.now(tz=timezone.utc)
    return f"{now.strftime('%H%M%S')}z"

def output_xastir(locs):
    """Print the given locations in Xastir log format"""
    timestamp = current_timestamp() if args.current_time else '000000z'

    for location in locs:
        print(f'{location.xastir_str(timestamp)}')

with open(args.input, 'r', encoding='utf-8') as f:
    Lines = f.readlines()
    locations = [loc for line in Lines if (loc := loc_from_pos(line)) is not None]

    if args.xastir:
        output_xastir(locations)
    elif args.json:
        output_json(locations)
