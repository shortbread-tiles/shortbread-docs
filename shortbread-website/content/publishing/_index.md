+++
title = "Publishing Shortbread Maps"
description = "Publishing maps with Shortbread vector tiles"
weight = 6
+++

## Required resources for Shortbread maps

* **Tileset**: See [tile storage](/make-vectortiles/#tile-storage) for vector tile storage options. If an external tileset is used, CORS headers are required.
* **Tile server**: Except for pregenerated MVT/PBF files or PMTiles archives, a vector tile server is required.
* **Map Style**: [JSON document](https://maplibre.org/maplibre-style-spec/) with embedded or external TileJSON source specifications. A map style can also be created using Javascript code.
* **Fonts**: Fonts must be available in a Maplibre specific PBF format, see [font-maker](https://github.com/maplibre/font-maker) for more information. When using OpenLayers, system fonts are used instead of glyph PPFs.
* **Sprites**: Images for point symbols or fill patterns must be availabe as [Sprites](https://maplibre.org/maplibre-style-spec/sprite/).
* **HTML/Javascript viewer**: A HTML page with embedded or external Javascript code.


## Example workflow

Minimal tutorial using PMTiles created with Planetiler and MapLibre with a Versatile style.

Prepare directories:
```bash
mkdir -p data public/styles public/assets/sprites
```

Generate Shortbread tiles using Planetiler:
```bash
docker run --rm --user=$UID -v $PWD/data:/data ghcr.io/onthegomap/planetiler shortbread.yml \
  --download --area=liechtenstein --output=/data/shortbread.pmtiles
mv data/shortbread.pmtiles public/
```
Download Versatiles styles and sprites:
```bash
cd public
wget -O - https://github.com/versatiles-org/versatiles-style/releases/latest/download/styles.tar.gz | tar xz -C styles
wget -O - https://github.com/versatiles-org/versatiles-style/releases/latest/download/sprites.tar.gz | tar xz -C assets/sprites
```
Replace tile source with your PMTiles URL:
```bash
jq '.sources."versatiles-shortbread".url="pmtiles:///shortbread.pmtiles" | del(.sources."versatiles-shortbread".tiles)' \
   styles/colorful.json > styles/colorful-pmtiles.json
```
Make sprite URL relative:
```bash
sed --in-place -e 's!https://tiles.versatiles.org/assets/sprites!/assets/sprites!g' styles/*.json
```

Viewer `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>MapLibre Viewer</title>
    <script src='https://unpkg.com/maplibre-gl@4/dist/maplibre-gl.js'></script>
    <link href='https://unpkg.com/maplibre-gl@4/dist/maplibre-gl.css' rel='stylesheet' />
    <script src="https://unpkg.com/pmtiles@3/dist/pmtiles.js"></script>
    <style>
        body { margin: 0; }
        #map { height: 100vh; width: 100vw;}
    </style>
  </head>
  <body>
    <div id="map"/>
    <script>
      let protocol = new pmtiles.Protocol();
      maplibregl.addProtocol("pmtiles", protocol.tile);
      var map = new maplibregl.Map({
        container: 'map',
        style: 'styles/colorful-pmtiles.json',
        center: [9.55, 47.14],
        zoom: 10
      });
    </script>
  </body>
</html>
```

Upload public directory to a site supporting HTTP Range Requests:

```
scp -r . example.com:
```
