+++
title = "Creating Shortbread Vector Tiles"
description = "This page describes how to generate the vector tiles in the Shortbread schema"
weight = 4
+++

## Tile creation workflows

### PBF → Vector tiles

{{< figure src="pbf-mvt.png" width="70%" >}}

Software:
* tilemaker ([Tutorial](tilemaker/))
* Planetiler ([Tutorial](planetiler/))

### PBF → DB → Vector tiles

{{< figure src="pbf-db-mvt.png" width="70%" >}}

Software PBF → PostGIS:
* osm2pgsql ([Tutorial](osm2pgsql/))

Software PostGIS → Vector tiles:
* BBOX ([Tutorial](bbox/))
* Tilekiln ([Tutorial](tilekiln/))

## Tile storage

There are multiple options to store vector tiles:

* Files / S3
* [MBTiles](https://github.com/mapbox/mbtiles-spec) (requires tile service for serving)
* [PMTiles](https://docs.protomaps.com/pmtiles/)
* DB cache (requires tile service for serving)
* No storage - live generated tiles
