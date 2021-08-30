# Geofabrik Basic Vector Tiles

The Geofabrik "Basic" vector tile schema is intended to be a basic, lean, general-purpose vector tile schema for OpenStreetMap data.

It does not, and is not intended to, cover the full breath and depth of OpenStreetMap tagging.

This repository contains the description of the tile schema, i.e. which layers there
are on which zoom levels and which attributes to expect on features in that layer.

At present, this is still "work in progress" and very much a moving target.

## Installation

This repository does not have installable software. You will need to use a software
that can create vector tiles (e.g. tilemaker) and combine that with configuration files
designed to output vector tiles according to this schema (e.g. geofabrik-basicvt-tilemaker).

## Authors

The schema has been created for Geofabrik by Thomas Skowron, Christine Karch,
Amanda McCann, and Michael Reichert before it was put on Github. Further contributors
may be visible in the git history.

## License and Copyright

Geofabrik takes the position that this schema is not creative enough to be a copyrightable
work. For the sake of clarity, however, we are releasing it under the CC-0 license.
