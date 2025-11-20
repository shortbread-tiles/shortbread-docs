+++
title = "Map Styles"
description = "This page gives an overview about available open source maps styles for Shortbread vector tiles"
weight = 3
+++

## Web mapping libraries

Most Javascript mapping libraries support vector tiles as data source.

Some well known options are:
* [MapLibre](https://maplibre.org/)
* [OpenLayers](https://openlayers.org/) ([ol-mapbox-style](https://github.com/openlayers/ol-mapbox-style))
* [Leaflet](https://leafletjs.com/) ([maplibre-gl-leaflet plugin](https://github.com/maplibre/maplibre-gl-leaflet))
* [deck.gl](https://deck.gl/) (MVTLayer), [kepler.gl](https://kepler.gl/)

### Styling

Vector tiles are usually rendered using [MapLibre styles](https://maplibre.org/maplibre-style-spec/).
You can either write your style in this JSON format or use a visual style editor like [Maputnik](https://maplibre.org/maputnik/).

## Available styles

The following open source rendering styles are available for Shortbread vector tiles.

### VersaTiles Styles

[VersaTiles Styles](https://github.com/versatiles-org/versatiles-style) are map styles written for the MapLibre rendering engine. [VersaTiles](https://versatiles.org/) is a completely FLOSS stack for generating, distributing and using map tiles based on OpenStreetMap data, free of any commercial interests.

<div id="map-container" style="position: relative; width: 100%; height: 600px; margin: 2rem 0; border: 2px solid #ccc; border-radius: 8px;">
  <div id="style-toggle" style="position: absolute; top: 10px; left: 10px; z-index: 1000; background: white; padding: 10px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
    <label for="style-select" style="display: block; margin-bottom: 5px; font-weight: bold;">Style:</label>
    <select id="style-select" style="padding: 5px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px;">
      <option value="colorful">Colorful</option>
      <option value="graybeard">Graybeard</option>
      <option value="eclipse">Eclipse</option>
      <option value="neutrino">Neutrino</option>
    </select>
  </div>
  <div id="map" style="width: 100%; height: 100%;"></div>
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maplibre-gl@5.12.0/dist/maplibre-gl.css">

<script type="module">
import maplibre from 'https://cdn.jsdelivr.net/npm/maplibre-gl@5.12.0/+esm';

const styleUrls = {
  colorful: 'https://tiles.versatiles.org/assets/styles/colorful/style.json',
  graybeard: 'https://tiles.versatiles.org/assets/styles/graybeard/style.json',
  eclipse: 'https://tiles.versatiles.org/assets/styles/eclipse/style.json',
  neutrino: 'https://tiles.versatiles.org/assets/styles/neutrino/style.json'
};

// Initialize map
const map = new maplibre.Map({
  container: 'map',
  style: styleUrls.colorful,
  center: [8.5, 47.4], // Switzerland
  zoom: 10
});

map.addControl(new maplibre.FullscreenControl(), 'top-right');

const styleSelect = document.getElementById('style-select');
styleSelect.addEventListener('change', (e) => {
  const selectedStyle = e.target.value;
  map.setStyle(styleUrls[selectedStyle]);
});
</script>

## Shortbread-Demo-MapLibre

A very basic [Maplibre style](https://github.com/shortbread-tiles/shortbread-demo-maplibre).

## Shortbread-Mapnik

[Shortbread-Mapnik](https://github.com/geofabrik/shortbread-mapnik) is a colored base map style rendering roads, landuse, water, places, buildings and important boundaries
without being too detailed. It is written for the Mapnik rendering engine using the vector tiles as source.

![Shortbread Mapnik at zoom level 4](shortbread-mapnik-z4.png)
![Shortbread Mapnik at zoom level 6](shortbread-mapnik-z6.png)
![Shortbread Mapnik at zoom level 8](shortbread-mapnik-z8.png)
![Shortbread Mapnik at zoom level 11](shortbread-mapnik-z11.png)
![Shortbread Mapnik at zoom level 14](shortbread-mapnik-z14.png)
![Shortbread Mapnik at zoom level 16](shortbread-mapnik-z16.png)
