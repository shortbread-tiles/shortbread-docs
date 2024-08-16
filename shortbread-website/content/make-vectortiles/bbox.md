+++
title = "Using BBOX"
description = "Generating vector tiles with BBOX"
weight = 4
+++

Shortbread Tiles can be created with [BBOX](https://www.bbox.earth/).

## BBOX overview

* Generate and serve vector tiles
* Formats: PostGIS, MBTiles, PMTiles, S3
* Non-Mercator tile grids
* Successor of t-rex tile server

### Serve shortbread tiles from PostGIS

When importing OSM data into PostGIS with [osm2pgsql](/make-vectortiles/osm2pgsql/):
* Set `local BBOX = true` in `osm2pgsql-themepark/config/shortbread_gen.lua`
* Change `write_config('bbox-config.toml')` to `write_config('/data/bbox-config.toml')`
  when running with Docker
* Run `osm2pgsql`

Run BBOX tile server:
```bash
BBOX_DATASOURCE_DB=postgres://osm:osm@127.0.0.1/osm bbox-tile-server -c data/bbox-config.toml serve
```

Tiles are served on <http://localhost:8080/xyz/osm.style.json>

Serve with style:
```bash
mkdir styles
curl -L https://github.com/versatiles-org/versatiles-style/releases/latest/download/styles.tar.gz \
  | tar xz -C styles colorful.json
sed 's!https://tiles.versatiles.org/tiles/osm/{z}/{x}/{y}!http://localhost:8080/xyz/osm/{z}/{x}/{y}.pbf!g' styles/colorful.json > styles/colorful-local.json

BBOX_DATASOURCE_DB=postgres://osm:osm@127.0.0.1/osm BBOX_ASSETS__STATIC='[{dir="../styles",path="/styles"}]' bbox-tile-server -c data/bbox-config.toml serve
```

### Serve PMTiles or MBTiles with style

```bash
mkdir styles
curl -L https://github.com/versatiles-org/versatiles-style/releases/latest/download/styles.tar.gz \
  | tar xz -C styles colorful.json
sed 's!https://tiles.versatiles.org/tiles/osm/{z}/{x}/{y}!http://localhost:8080/xyz/shortbread/{z}/{x}/{y}.pbf!g' \
 styles/colorful.json > styles/colorful-local.json

# Serve MBTiles
BBOX_ASSETS__STATIC='[{dir="styles",path="/styles"}]' bbox-tile-server serve data/shortbread.mbtiles

# Serve PMTiles
BBOX_ASSETS__STATIC='[{dir="styles",path="/styles"}]' bbox-tile-server serve data/shortbread.pmtiles

# Open in Maputnik
xdg-open "https://maplibre.org/maputnik/?style=http://localhost:8080/styles/colorful-local.json#15/47.1377/9.5188"
```
