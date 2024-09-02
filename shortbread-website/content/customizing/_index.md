+++
title = "Customizing Shortbread"
description = "How to create and display customized shortbread vector tiles"
weight = 6
+++

## Use cases

* **Custom styles**: Hiding features in a map or highlighting specific features can be done with a custom style.
Since styles are applied in the browser, you can use existing Shortbread tiles. See [Rendering Styles](/styles/).

* **Additional POIs**: If some POIs are missing or specific attributes for styling are not included, then you
have to create custom Shortbread tiles or an additional tileset. 

* **Route relations**: If you want to highlight route relations (e.g. bus lines) in your map, then you
have to create custom Shortbread tiles or an additional tileset. 

* **More tags for special objects**: If you want to create specialized maps requiring additional tags, then you
have to create custom Shortbread tiles or an additional tileset. 

* **Additional tags for streets or buildings**: If you want to create specialized maps requiring additional tags for streets or buildings, then you
have to create custom Shortbread tiles. 

* **Other / more languages**: Currently Shortbread tiles include `name`, `name_en` and `name_de`. It is a goal for Shortbread to
add support for other languages. In the meantime you have to create custom Shortbread tiles, if you need more languages.


## Customizing Shortbread

### Creating custom Shortbread tiles

See [Creating Shortbread Vector Tiles](/make-vectortiles/) for workflows and tutorials to create custom Shortbread tiles.

The main options for custom configurations are:
* tilemaker config (JSON, Lua)
* Planetiler config (YAML, Java)
* osm2pgsl config (Lua)

### Basic rules

* Keep tile size small
* Don't break base map styles
* Discuss core extensions in [shortbread-docs repo](https://github.com/shortbread-tiles/shortbread-docs)

## Using Shortbread with additional tilesets

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
