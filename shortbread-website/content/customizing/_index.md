+++
title = "Customizing Shortbread"
description = "How to create and display custoimzed shortbread vector tiles"
weight = 6
+++

## Use cases

* Custom style
* Additional POIs
* Route relations
* More tags for special objects
* Additional tags for streets or buildings
* Other / more languages

### Basic rules

* Keep tiles small
* Don't break base map styles
* Discuss core extensions in [shortbread-docs repo](https://github.com/shortbread-tiles/shortbread-docs)

## Custom Styling

Mapbox / MapLibre GL JSON: <https://maplibre.org/maplibre-style-spec/>

Style editor:

Maputnik Editor ([maplibre.org/maputnik](https://maplibre.org/maputnik/))

## Extending Shortbread

* tilemaker config (JSON, Lua)
* Planetiler config (YAML, Java)
* osm2pgsl config (Lua)

### Tileset combinations

* Extended base map tiles
  * No additional tiles
  * Can break base map styles
  * Selfhosting required
* Additional tilesets
  * Additional tile source in style
  * No easy relation to base map tiles
  * Potential duplication of data

### Server-side combination

* Vector tiles can be concatenated by server
* Requires a service
* Not supported by all tile servers
* Caching more difficult

## Publish custom tiles

### PMTiles, style and sprites

```bash
# Generate Shortbread tiles
docker run --rm --user=$UID -v $PWD/data:/data ghcr.io/onthegomap/planetiler shortbread.yml \
  --download --area=liechtenstein --output=/data/shortbread.pmtiles
# Download Versatiles Styles + Assets
mkdir -p styles assets/sprites
wget -O - https://github.com/versatiles-org/versatiles-style/releases/latest/download/styles.tar.gz | tar xz -C styles
wget -O - https://github.com/versatiles-org/versatiles-style/releases/latest/download/sprites.tar.gz | tar xz -C assets/sprites
# Replace tile source with PMTiles URL
jq '.sources."versatiles-shortbread".url="pmtiles:///shortbread.pmtiles" | del(.sources."versatiles-shortbread".tiles)' \
   styles/colorful.json > styles/colorful-pmtiles.json
# Make sprite URL relative
sed --in-place -e 's!https://tiles.versatiles.org/assets/sprites!/assets/sprites!g' styles/*.json
```

### Viewer HTML

index.html:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>MapLibre Viewer</title>
    <script src='https://unpkg.com/maplibre-gl@4.5.0/dist/maplibre-gl.js'></script>
    <link href='https://unpkg.com/maplibre-gl@4.5.0/dist/maplibre-gl.css' rel='stylesheet' />
    <script src="https://unpkg.com/pmtiles@3.0.6/dist/pmtiles.js"></script>
    <style>
        body { margin: 0; }
        #map { height:100%; width:100%;}
    </style>
  </head>
  <body>
    <div id="map"/>
    <script>
      let protocol = new pmtiles.Protocol();
      maplibregl.addProtocol("pmtiles", protocol.tile);
      var map = new maplibregl.Map({
        container: 'map',
        style: 'styles/colorful-mbtiles.json'
      });
    </script>
  </body>
</html>
```

### Deploy and serve

```
# Upload to site supporting HTTP Range Requests

scp -r . example.com:


# Or deploy to a hosting provider like Github pages
```
