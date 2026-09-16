#! /usr/bin/env python3
# Author: Frederik Ramm
# originally published in https://github.com/shortbread-tiles/shortbread-docs/issues/153#issuecomment-5476984543
#
# Program to determine a list of values for a given key
# where each value is in the list of N most frequently used values
# across a list of regions.

import requests
from collections import defaultdict

N = 100
tag = 'shop'
regions = ['europe', 'north-america', 'asia', 'south-america', 'africa']

globalitem = defaultdict(int)

for region in regions:
    r = requests.get("https://taginfo.geofabrik.de/{}/api/4/key/values?key={}&sortname=count&sortorder=desc&rp={}&page=1".format(region, tag, N))
    for item in r.json()['data']:
        globalitem[item['value']] += 1

for item in globalitem:
    if globalitem[item] == len(regions):
        print (item)
