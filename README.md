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
