#! /usr/bin/env python3
# Author: Frederik Ramm
# Extended by Michael Reichert
# originally published in https://github.com/shortbread-tiles/shortbread-docs/issues/153#issuecomment-5476984543
#
# Program to determine a list of values for a given key
# or keys matching a given search string
# where each value/key is in the list of N most frequently used values/keys
# across a list of regions.
#
# Example:
#   - `python tag_usage_stats.py -t value -k shop -n 75`
#     will return all values of shop=* which are in the list of N most frequently used values of shop=* in all requested regions.
#     For example, if shop=outdoor is frequently used in Europe an North America but rarely used in Africa, it will be not be returned.
#     However shop=convenience will be returned because it is among the top 75 shop values in all regions.
#   - `python tag_usage_stats.py -t key -k name -n 75`
#     will return all keys containing the query string "name" if they appear among the 75 most frequently used keys containing
#     the substring "name" in all requested regions.
#   - `python tag_usage_stats.py -t value -k office -n 100 -r europe/germany,europe/france`
#     will return the values of office=* which are in the list of N most freuqently used values in Germany and France.

import argparse
import enum
import math
import requests
from collections import defaultdict
import sys
import urllib.parse

N = 100
key = 'shop'
regions = ['europe', 'north-america', 'asia', 'south-america', 'africa']
default_regions = ",".join(regions)
headers = {"User-Agent": "shortbread/tag_usage_stats"}

class QueryType(enum.Enum):
    values = 'value'
    keys = 'key'

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser(description="""Program to determine a list of values for a given key
where each value is in the list of N most frequently used values
across a list of regions.
""")
parser.add_argument("-k", "--key", type=str, default=key, help="Set OSM key (defaults to 'shop')")
parser.add_argument("-n", "--number", type=int, default=N, help="Change N (defaults to 100)")
parser.add_argument("-t", "--type", type=QueryType, choices=list(QueryType), default=QueryType.values, help="Whether to query the N most frequently used values of a given key or the N most frequently used keys matching a given search string.")
parser.add_argument("-r", "--regions", type=str, default=default_regions, help="Regions to compare. Specify as one string separated by comma. This must match the paths used at taginfo.geofabrik.de")
args = parser.parse_args()
regions = args.regions.split(",")
if len(regions) == 0:
    sys.stderr.write("ERROR: No regions provided.\n")

globalitem = {}

for i, region in enumerate(regions):
    url = "https://taginfo.geofabrik.de/{}/api/4/key/values".format(urllib.parse.quote(region))
    params = {"sortname": "count_all", "sortorder": "desc", "rp": str(args.number), "page": "1"}
    if args.type == QueryType.keys:
        url = "https://taginfo.geofabrik.de/{}/api/4/keys/all".format(urllib.parse.quote(region))
        params["query"] = args.key
    elif args.type == QueryType.values:
        params["key"] = args.key
    r = requests.get(url, headers=headers, params=params)
    if r.status_code != 200:
        sys.stderr.write("ERROR: {url} HTTP {status_code}\n".format(**r.__dict__))
        sys.exit(1)
    for item in r.json()['data']:
        entry_key = item[args.type.value]
        entry = globalitem.get(entry_key, [0 for j in range(len(regions))])
        attr = "count"
        if args.type == QueryType.keys:
            attr = "count_all"
        entry[i] = item[attr]
        globalitem[entry_key] = entry

top_entries = []
for item, counts in globalitem.items():
    if 0 not in counts:
        top_entries.append((item, sum(counts)))
top_entries.sort(key=lambda k: k[1], reverse=True)
max_keylength = max([len(k[0]) for k in top_entries])
max_valuelength = int(max([math.log(k[1], 10) for k in top_entries])) + 1
for t in top_entries:
    print("{} {}".format(t[0].ljust(max_keylength, " "), str(t[1]).rjust(max_valuelength, " ")))
