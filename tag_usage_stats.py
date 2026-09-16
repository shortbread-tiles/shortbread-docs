#! /usr/bin/env python3
# Author: Frederik Ramm
# Extended by Michael Reichert
# originally published in https://github.com/shortbread-tiles/shortbread-docs/issues/153#issuecomment-5476984543
#
# Program to determine a list of values for a given key
# where each value is in the list of N most frequently used values
# across a list of regions.

import argparse
import requests
from collections import defaultdict
import sys

N = 100
key = 'shop'
regions = ['europe', 'north-america', 'asia', 'south-america', 'africa']
default_regions = ",".join(regions)

parser = argparse.ArgumentParser(description="""Program to determine a list of values for a given key
where each value is in the list of N most frequently used values
across a list of regions.
""")
parser.add_argument("-n", "--number", type=int, default=N, help="Change N (defaults to 100)")
parser.add_argument("-k", "--key", type=str, default=key, help="Set OSM key (defaults to 'shop')")
parser.add_argument("-r", "--regions", type=str, default=default_regions, help="Regions to compare. Specify as one string separated by comma. This must match the paths used at taginfo.geofabrik.de")
args = parser.parse_args()
regions = args.regions.split(",")
if len(regions) == 0:
    sys.stderr.write("ERROR: No regions provided.\n")

globalitem = defaultdict(int)

for region in regions:
    r = requests.get("https://taginfo.geofabrik.de/{}/api/4/key/values?key={}&sortname=count&sortorder=desc&rp={}&page=1".format(region, args.key, args.number))
    for item in r.json()['data']:
        globalitem[item['value']] += 1

for item in globalitem:
    if globalitem[item] == len(regions):
        print (item)
