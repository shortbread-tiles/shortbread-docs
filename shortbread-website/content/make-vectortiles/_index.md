+++
title = "Creating Shortbread Vector Tiles"
description = "This page describes how to generate the vector tiles in the Shortbread schema"
+++

Shortbread Tiles can be created with [Tilemaker](https://tilemaker.org/).


Creating Shortbread vetor tiles is very simple. Install Tilemaker & the shortbread-tilemaker settings, get the OSM & external data, and run tilemaker!

## Software required
### Tilemaker

* Follow the [Tilemaker installation instructions](https://github.com/systemed/tilemaker/blob/master/docs/INSTALL.md).

### Extra software

You need [`ogr2ogr`](https://gdal.org/programs/ogr2ogr.html).

| OS            | command                     |
|---------------|-----------------------------|
| Debian/Ubuntu | `sudo apt install gdal-bin` |
| _(Other OS)_  | _(command)_                 |

## Shortbread-Tilemaker settings

Clone the Git repository of the vector tile schema from Github:

```sh
git clone https://github.com/shortbread-tiles/shortbread-tilemaker
```

## Data

### OpenStreetMap data

Tilemaker needs raw OpenStreetMap data as input. You can download it from:

* regional extracts from [Geofabrik Download Service](https://download.geofabrik.de)
* latest weekly planet PBF file from [planet.openstreetmap.org](https://planet.openstreetmap.org/) or any of its [mirrors](https://wiki.openstreetmap.org/wiki/Planet.osm#Planet.osm_mirrors)
* regional extracts from [download.openstreetmap.fr](https://download.openstreetmap.fr/extracts/)

Please try with a small extract first before you try to load the complete planet file.

### Additional data

In the shortbread-tilemaker directory:

	./get-shapefiles.sh

It will download a few required additional files into the `data` directory.

## Generate Tiles

In the shortbread-tilemaker directory, run this command:

	tilemaker --config config.json --process process.lua --bbox -180,-90,180,90 \
		--input OSM_FILE.osm.pbf --output shortbread-tiles.mbtiles


The generated data is the `shortbread-tiles.mbtiles` file.

### Output format

Tilemaker supports a few [output formats](https://github.com/systemed/tilemaker/blob/master/docs/RUNNING.md#standard-usage). Here [mbtiles](https://wiki.openstreetmap.org/wiki/MBTiles) is used.


### BBox PBF files

If the `.osm.pbf` file contains a bounding box entry in its header (this is not
true for the planet), you can omit the `--bbox -180,-90,180,90` part of the
tilemaker command. The generation process will be much faster for smaller
areas, and the output data will contain less “ocean tiles”, [[and be a little
bit smaller]]??

The error message `Can't read shapefiles unless a bounding box is provided.`
means you need to specify the `--bbox` option.

### Memory

--store FIXME


## Statistics

In February 2022, a server with a AMD EPYC 7452 32-Core Processor (2.35–3.35 GHz), 512 GB RAM,
cache on NVMe and output to a loop-mounted hard disk drive (RAID 1) took 16:15 hours and needed up
to 358 GB RAM to generate the whole planet.

## Troubleshooting
