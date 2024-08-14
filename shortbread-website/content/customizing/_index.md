+++
title = "Customizing Shortbread"
description = "How to create and display custoimzed shortbread vector tiles"
weight = 6
+++

## Use cases

* **Custom styles**: Hiding features in a map or highlighting specific features can be done with a custom style.
Since styles are applied in the browser, you can use existing Shortbread tiles.

* **Additional POIs**: If some POIs are missing or specific attributes for styling are not included, then you
have to create custom Shortbread tiles or an additional tileset. 

* **Route relations**: If you want to highlight route relations (e.g. bus lines) in your map, then you
have to create custom Shortbread tiles or an additional tileset. 

* **More tags for special objects**: If you want do create specialized maps requiring additional tags, then you
have to create custom Shortbread tiles or an additional tileset. 

* **Additional tags for streets or buildings**: If you want do create specialized maps requiring additional tags for streets or buildings, then you
have to create custom Shortbread tiles. 

* **Other / more languages**: Currently Shortbread tiles include `name`, `name_en` and `name_de`. It is a goal for Shortbread 2.0 to
add support for other languages. In the meantime you have to create custom Shortbread tiles, if you need more languages.

## Custom Styling

### Web mapping libraries

Most Javascript mapping libraries support vector tiles as data source.

Some well known options are:
* [MapLibre](https://maplibre.org/)
* [OpenLayers](https://openlayers.org/) ([ol-mapbox-style](https://github.com/openlayers/ol-mapbox-style))
* [Leaflet](https://leafletjs.com/) ([maplibre-gl-leaflet plugin](https://github.com/maplibre/maplibre-gl-leaflet))
* [deck.gl](https://deck.gl/) (MVTLayer), [kepler.gl](https://kepler.gl/)

### Styling

Vector tiles are usually rendered using [MapLibre styles](https://maplibre.org/maplibre-style-spec/).
You can either write your style in this JSON format or use a visual style editor like [Maputnik](https://maplibre.org/maputnik/).

## Extending Shortbread

### Creating custom Shotbread tiles

See [Creating Shortbread Vector Tiles](/make-vectortiles/) for workflows and tutorials to create custom Shortbread tiles.

The main options for custom configurations are:
* tilemaker config (JSON, Lua)
* Planetiler config (YAML, Java)
* osm2pgsl config (Lua)

### Basic rules

* Keep tile size small
* Don't break base map styles
* Discuss core extensions in [shortbread-docs repo](https://github.com/shortbread-tiles/shortbread-docs)

### Tileset combinations

There are pros and cons for creating custom base map tiles or creating additional tilesets:

* Extended base map tiles
  * No additional tiles
  * Can break base map styles
  * Selfhosting required
* Additional tilesets
  * Additional tile source in style
  * No easy relation to base map tiles
  * Potential duplication of data

### Server-side combination

Mapbox vector tiles allow concatenating tiles on server-side.

There are some drawbacks though:
* Requires a service
* Not supported by all tile servers
* Caching more difficult

## Publish custom tiles

There are many ways to publish you own maps based on Shortbread tiles. Here's a minimal tutorial using [PMTiles](https://docs.protomaps.com/pmtiles/) for storing tiles. Tiles are efficently stored in a single file and no additional server software is required for serving tiles. The only requirement is an HTTP server supporting HTTP range requests.

### Preparing tiles and style

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

### Deploy and serve

Upload directory to a site supporting HTTP Range Requests:
```
scp -r . example.com:
```
