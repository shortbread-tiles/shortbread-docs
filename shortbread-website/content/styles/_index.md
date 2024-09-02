+++
title = "Map Styles"
description = "This page gives an overview about available open source maps styles for Shortbread vector tiles"
weight = 3
toc = false
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

### VersaTiles Colorful

[VersaTiles Colorful](https://github.com/versatiles-org/versatiles-style) is a colorful, full featured map written for the MapLibre rendering engine.
[Demo](https://versatiles.org/) using [VersaTiles](https://versatiles.org/guide.html), a completely FLOSS stack for generating, distributing and using map tiles based on OpenStreetMap data, free of any commercial interests.

<div class="example-images">

![VersaTiles Colorful at zoom level 3](versatiles-colorful-z3.webp)
![VersaTiles Colorful at zoom level 5](versatiles-colorful-z5.webp)
![VersaTiles Colorful at zoom level 7](versatiles-colorful-z7.webp)
![VersaTiles Colorful at zoom level 9](versatiles-colorful-z9.webp)
![VersaTiles Colorful at zoom level 11](versatiles-colorful-z11.webp)
![VersaTiles Colorful at zoom level 13](versatiles-colorful-z13.webp)
![VersaTiles Colorful at zoom level 15](versatiles-colorful-z15.webp)

</div>

### VersaTiles Neutrino

[VersaTiles Neutrino](https://github.com/versatiles-org/versatiles-style) is a light basemap style written for the MapLibre rendering engine.

<div class="example-images">

![VersaTiles Neutrino at zoom level 3](versatiles-neutrino-z3.webp)
![VersaTiles Neutrino at zoom level 5](versatiles-neutrino-z5.webp)
![VersaTiles Neutrino at zoom level 7](versatiles-neutrino-z7.webp)
![VersaTiles Neutrino at zoom level 9](versatiles-neutrino-z9.webp)
![VersaTiles Neutrino at zoom level 11](versatiles-neutrino-z11.webp)
![VersaTiles Neutrino at zoom level 13](versatiles-neutrino-z13.webp)
![VersaTiles Neutrino at zoom level 15](versatiles-neutrino-z15.webp)

</div>

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
