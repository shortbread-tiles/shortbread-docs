# <img src="./shortbread-website/static/shortbread_logo.png" width=50> Shortbread Vector Tiles – Specification

The Shortbread vector tile schema is intended to be a basic, lean, general-purpose vector tile schema for OpenStreetMap data.

It does not, and is not intended to, cover the full breadth and depth of OpenStreetMap tagging.

This repository contains the description of the tile schema, i.e. which layers there
are on which zoom levels and which attributes to expect on features in that layer.

**At present, this is still "work in progress" and very much a moving target.**

## Installation

This repository does not have installable software. You will need to use a software
that can create vector tiles (e.g. Tilemaker) and combine that with configuration files
designed to output vector tiles according to this schema (e.g. [shortbread-tilemaker](https://github.com/shortbread-tiles/shortbread-tilemaker)).

## Scripts

### `tag_usage_stats.py`

Although [Taginfo](https://taginfo.openstreetmap.org) provides global statistics about usage of tags,
it provides a narrow view on actual usage only. Some tags are used a lot in one region but rarely used elsewhere.
Overview maps provided by Taginfo show some differences.

For decisions which tags should be included a vector tile schema like Shortbread, a comparison between
multiple regions is more helpful. Therefore this repository contains a [utility script](tag_usage_stats.py) to aid decisions which tags to support.
It retrieves the N most frequently used values per key or N most frequently used keys matching a given search string
from [Geofabrik's Taginfo instances](https://taginfo.geofabrik.de) for a couple for regions and returns those who appear in all regions among the top N ranks.
Run `python tag_usage_stats.py --help` for instructions how to use. See the comment at the beginning of
the file for usage examples.

## Authors

The schema has been created for Geofabrik by Thomas Skowron, Christine Karch,
Amanda McCann, and Michael Reichert before it was put on Github. Further contributors
may be visible in the Git history.

## See also

* [shortbread-tilemaker](https://github.com/shortbread-tiles/shortbread-tilemaker): Generate this data schema with [tilemaker](https://tilemaker.org/).

## License and Copyright

We take the position that this schema is not creative enough to be a copyrightable
work. For the sake of clarity, however, we are releasing it under the [CC-0 license](./LICENSE.md).
For the avoidance of doubt, using this schema to create your vector tiles will not add any attribution
requirements, but if you generate vector tiles from OpenStreetMap data, you will of course have
to attribute OpenStreetMap.
