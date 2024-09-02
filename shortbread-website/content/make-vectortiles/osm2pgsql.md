+++
title = "Using osm2pgsql"
description = "Importing OSM data into PostGIS with osm2pgsql"
weight = 3
+++

[osm2pgsql](https://osm2pgsql.org/) can be used to import and update OSM data in a PostGIS database using the Shortbread schema.

## osm2pgsql overview

* Flex mode: configuration with Lua scripts
* Osm2pgsql [Themepark](https://osm2pgsql.org/themepark/) with Shortbread config
* `osm2pgsql-gen` for generalization in database
* `osm2pgsql-replication` for incremental updates
* Config generation for tile servers

### Quickstart (Docker)

```bash
git clone https://github.com/osm2pgsql-dev/osm2pgsql-themepark.git

# Start database
docker run -d --name postgis -p 127.0.0.1:5432:5432 \
  -e POSTGRES_DB=osm -e POSTGRES_USER=osm -e POSTGRES_PASSWORD=osm postgis/postgis

# Download OSM extract
mkdir data
curl -sSfO --output-dir data https://download.geofabrik.de/europe/liechtenstein-latest.osm.pbf

# Import OSM extract
docker run --rm --network=host -v $PWD/osm2pgsql-themepark:/osm2pgsql-themepark:ro -v $PWD/data:/data \
  -e LUA_PATH="/osm2pgsql-themepark/lua/?.lua;;" \
  -e PGHOST=127.0.0.1 -e PGUSER=osm -e PGPASSWORD=osm iboates/osm2pgsql:1.11.0 \
  osm2pgsql -d osm -S /osm2pgsql-themepark/config/shortbread_gen.lua -O flex --slim \
            /data/liechtenstein-latest.osm.pbf
```

### osm2pgsql generalization

```bash
# Download and import additional data (water polygons, etc.). Requires ogr2ogr!
PGHOST=127.0.0.1 PGUSER=osm PGPASSWORD=osm ./osm2pgsql-themepark/themes/external/download-and-import.sh \
  data osm oceans ocean

# Generalize
docker run --rm --network=host -v $PWD/osm2pgsql-themepark:/osm2pgsql-themepark:ro \
  -e LUA_PATH="/osm2pgsql-themepark/lua/?.lua;;" \
  -e PGHOST=127.0.0.1 -e PGUSER=osm -e PGPASSWORD=osm iboates/osm2pgsql:1.11.0 \
   osm2pgsql-gen -d osm -S /osm2pgsql-themepark/config/shortbread_gen.lua
```

### osm2pgsql updates

```bash
docker run --rm --network=host -v $PWD/osm2pgsql-themepark:/osm2pgsql-themepark:ro \
  -e LUA_PATH="/osm2pgsql-themepark/lua/?.lua;;" \
  -e PGHOST=127.0.0.1 -e PGUSER=osm -e PGPASSWORD=osm iboates/osm2pgsql:1.11.0 \
  osm2pgsql-replication update -d osm
```
