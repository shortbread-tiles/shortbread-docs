+++
title = "Using Planetiler"
description = "Generating vector tiles with Planetiler"
weight = 2
+++

Shortbread Tiles can be created with [Planetiler](https://github.com/onthegomap/planetiler).

## Planetiler overview

* Configs for OpenMapTiles and Shortbread schema
* YAML configuration or Java application
* Output formats: MBTiles, PMTiles
* No diff support
* Extremely fast!

### Quickstart (Docker)

```bash
mkdir data
docker run --rm --user=$UID -v $PWD/data:/data ghcr.io/onthegomap/planetiler shortbread.yml \
  --download --area=liechtenstein --output=/data/shortbread.pmtiles
```
