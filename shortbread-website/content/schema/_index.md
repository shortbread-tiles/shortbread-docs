+++
draft= false
title = "Vector Tile Schema"
description = "This page describes the layers of the Shortbread vector schema and their contents"
+++

{{% toc /%}}

## About

The Shortbread vector tile schema is intended to be a basic, lean, general-purpose vector tile schema for OpenStreetMap data.
It does not, and is not intended to, cover the full breadth and depth of OpenStreetMap tagging.

This document describes the layers that are defined in the vector tile schema, and the features and attributes available on each layer.


## Feature sorting

Some layers have their features sorted by importance or rendering order. This allows you to use rendering engines which do not support feature sorting themselves.


## Water

### Layer "ocean"

This layer contains oceans.

Additional attributes are provided only to make GDAL read features from this layer. They have no other meaning.

### Layer "water\_polygons"

This layer contains inland water bodies and glaciers.

#### Properties

| Field Name | Type    | Description                                |
| ---------- | :------ | :----------------------------------------- |
| `kind`     | string  | type of water body                         |
| `way_area` | numeric | area in square meter (Mercator Projection) |

#### Features

|           | `kind`    | OSM tag                                               | Geometry | Zoom |
| --------- | :-------- | :---------------------------------------------------- | :------- | :--- |
| glacier   | glacier   | `natural=glacier`                                     | polygon  | 4+   |
| water     | water     | `natural=water` + `water!=river`                      | polygon  | 4+   |
| river     | river     | `waterway=riverbank`, `natural=water` + `water=river` | polygon  | 4+   |
| reservoir | reservoir | `landuse=reservoir`                                   | polygon  | 4+   |
| basin     | basin     | `landuse=basin`                                       | polygon  | 4+   |
| dock      | dock      | `waterway=dock`                                       | polygon  | 10+  |
| canal     | canal     | `waterway=canal`                                      | polygon  | 10+  |

### Layer "water\_polygons\_labels"

Holds point (centroid) geometries and names for all named water polygons available in the *water\_polygons* layer.

The `way_area` attributes allows you to prefer labels of larger areas.  Features are sorted by `way_area` in
descending order.

#### Properties

| Field name | Type    | Description                                                            |
| ---------- | :------ | :--------------------------------------------------------------------- |
| `kind`     | string  | type of water body (see *water\_polygons* layer for a list of values)  |
| `way_area` | numeric | area in square meter (Mercator Projection)                             |
| `name`     | string  | value of OSM `name=*` tag                                              |
| `name_en`  | string  | value of OSM `name:en=*` tag                                           |
| `name_de`  | string  | value of OSM `name:de=*` tag                                           |

### Layer "water\_lines"

Holds waterway line geometries. Features are sorted by their `layer=*` tags in OpenStreetMap in ascending order (default 0).

#### Properties

| Field Name | Type    | Default | Description                                                                |
| ---------- | :------ | :------ | :------------------------------------------------------------------------- |
| `kind`     | string  |         | type of waterway                                                           |
| `tunnel`   | boolean | false   | true for `tunnel=yes/building_passage` or `covered=yes`, `false` otherwise |
| `bridge`   | boolean | false   | true for `bridge=yes`, `false` otherwise                                   |

#### Features

|        | `kind` | OSM tag         | Geometry | Zoom |
| ------ | :----- | :-------------- | :------- | :--- |
| canal  | canal  | waterway=canal  | line     | Canals are available if their line is longer than 0.25 pixel but not below 9. |
| river  | river  | waterway=river  | line     | Rivers are available if their line is longer than 0.25 pixel but not below 9. |
| stream | stream | waterway=stream | line     | 14+  |
| ditch  | ditch  | waterway=ditch  | line     | 14+  |

### Layer "water\_lines\_labels"

Hold line geometries and names for named water lines.

#### Minimum Zoom Levels

| Feature | Zoom                                                                           |
| ------- | :----------------------------------------------------------------------------- |
| canal   | Canals are available if their line is longer than 0.25 pixel but not below 12. |
| river   | Rivers are available if their line is longer than 0.25 pixel but not below 12. |
| stream  | 14+                                                                            |
| ditch   | 14+                                                                            |

#### Properties

| Field Name | Type   | Description                                                          |
| ---------- | :----- | :------------------------------------------------------------------- |
| `kind`     | string | type of water body (see *water\_lines* layer for a list of values)   |
| `name`     | string | value of OSM `name=*` tag                                            |
| `name_en`  | string | value of OSM `name:en=*` tag                                         |
| `name_de`  | string | value of OSM `name:de=*` tag                                         |

### Layer "dam\_lines"

Holds line geometries of dams (not dykes).

#### Properties

| Field Name | Type    |
| ---------- | :------ |
| `kind`     | string  |

#### Features

|      | `kind` | OSM tag      | Geometry | Zoom |
| ---- | :----- | :----------- | :------- | :--- |
| dam  | dam    | waterway=dam | line     | 12+  |

### Layer "dam\_polygons"

Holds polygon geometries of dams (not dykes).

#### Properties

| Field Name | Type    |
| ---------- | :------ |
| `kind`     | string  |

#### Features

|      | `kind` | OSM tag      | Geometry | Zoom |
| ---- | :----- | :----------- | :------- | :--- |
| dam  | dam    | waterway=dam | polygon  | 12+  |


### Layer "pier\_lines"

This layer contains piers, breakwaters and groynes mapped as lines. See the *pier\_polygons* layer for those mapped as polygons.

#### Properties

| Field Name  | Type    | Description                              |
| ----------- | :------ | :--------------------------------------- |
| kind        | string  | see Features section for possible values |


#### Features
| `kind`                  | OSM Tags                           | Geometry | Zoom |
| ----------------------- | :--------------------------------- | :------- | :--- |
| pier                    | `man_made=pier`                    | line     | 12+  |
| breakwater              | `man_made=breakwater`              | line     | 12+  |
| groyne                  | `man_made=groyne`                  | line     | 12+  |


### Layer "pier\_polygons"

This layer contains piers, breakwaters and groynes mapped as polygons. See the *pier\_lines* layer for those mapped as lines.

#### Properties

| Field Name  | Type    | Description                              |
| ----------- | :------ | :--------------------------------------- |
| kind        | string  | see Features section for possible values |


#### Features
| `kind`                  | OSM Tags                           | Geometry | Zoom |
| ----------------------- | :--------------------------------- | :------- | :--- |
| pier                    | `man_made=pier`                    | line     | 12+  |
| breakwater              | `man_made=breakwater`              | line     | 12+  |
| groyne                  | `man_made=groyne`                  | line     | 12+  |


## Countries, States, Cities

### Layer "boundaries"

Holds boundary lines of countries and states.


#### Properties

| Field name    | Type    | Description                                                                                                              |
| ------------- | :------ | :----------------------------------------------------------------------------------------------------------------------- |
| `admin_level` | numeric | highest administrative boundary this line belongs to                                                                     |
| `maritime`    | boolean | Boundary line is located on sea, base on OSM `maritime=*` tag, or is the coastline (way tagged with `natural=coastline`) |


#### Features

|           | Value of `admin_level` | Geometry | Zoom |
| --------- | :--------------------- | :------- | :--- |
| countries | 2                      | line     | 0+   |
| states    | 4                      | line     | 7+   |

### Layer "boundary\_labels"

Holds label points for boundary polygons of countries and states. Features are sorted by `way_area` in
descending order.


#### Properties

| Field name    | Type    | Description                                                                |
| ------------- | :------ | :------------------------------------------------------------------------- |
| `admin_level` | numeric | value of OSM `admin_level=*` tag, see Features section for possible values |
| `way_area`    | numeric | area in ha                                                                 |
| `name`        | string  | value of OSM `name=*` tag                                                  |
| `name_en`     | string  | value of OSM `name:en=*` tag                                               |
| `name_de`     | string  | value of OSM `name:de=*` tag                                               |

#### Features

|           | Value of `admin_level`  | Geometry | Minimum Area | Zoom |
| --------- | :---------------------- | :------- | :----------- | :--- |
| countries | 2                       | line     | 2*10^6 km²   | 2+   |
| countries | 2                       | line     | 7*10^5 km²   | 3+   |
| countries | 2                       | line     | 1*10^5 km²   | 4+   |
| countries | 2                       | line     | none         | 5+   |
| states    | 4                       | line     | 7*10^5 km²   | 3+   |
| states    | 4                       | line     | 1*10^5 km²   | 4+   |
| states    | 4                       | line     | none         | 5+   |

### Layer "place\_labels"

Holds label points for populated places. Features are sorted by `population` in descending order.

#### Properties

| Field Name   | Type    | Description                                                            |
| ------------ | :------ | :--------------------------------------------------------------------- |
| `kind`       | string  | value of OSM `place=*` tag, see Features section for possible values   |
| `name`       | string  | value of OSM `name=*` tag                                              |
| `name_en`    | string  | value of OSM `name:en=*` tag                                           |
| `name_de`    | string  | value of OSM `name:de=*` tag                                           |
| `population` | numeric | value of OSM `population=*` tag, else defaults (see below)             |

#### Features

|                   | Value of `kind`      | OSM Tags                                         | Geometry | Zoom | Default Population |
| ----------------- | :------------------- | :----------------------------------------------- | :------- | :--- | :----------------- |
| national capital  | `capital`            | `place=city/town/village/hamlet` + `capital=yes` | point    | 4+   | depends on place=* |
| state capital     | `state_capital`      | `place=city/town/village/hamlet` + `capital=4`   | point    | 4+   | depends on place=* |
| city              | `city`               | `place=city` (except capitals)                   | point    | 6+   | 100,000            |
| town              | `town`               | `place=town` (except capitals)                   | point    | 7+   | 5,000              |
| village           | `village`            | `place=village` (except capitals)                | point    | 10+  | 100                |
| hamlet            | `hamlet`             | `place=hamlet` (except capitals)                 | point    | 10+  | 50                 |
| suburb            | `suburb`             | `place=suburb`                                   | point    | 10+  | 1,000              |
| quarter           | `quarter`            | `place=quarter`                                  | point    | 10+  | 500                |
| neighbourhood     | `neighbourhood`      | `place=neighbourhood`                            | point    | 10+  | 100                |
| isolated dewlling | `isolated_dwelling`  | `place=isolated_dwelling`                        | point    | 10+  | 5                  |
| farm              | `farm`               | `place=farm`                                     | point    | 10+  | 5                  |
| island            | `island`             | `place=island`                                   | point    | 10+  | 0                  |
| unpopolate place  | `locality`           | `place=locality`                                 | point    | 10+  | 0                  |

## Land Use, Land Cover, Buildings

### Layer "land"

This layer contains basic land cover that is usually drawn first.

#### Properties

| Field Name  | Type    | Description                              |
| ----------- | :------ | :--------------------------------------- |
| kind        | string  | see Features section for possible values |


#### Features
| `kind`                  | OSM Tags                           | Geometry | Zoom |
| ----------------------- | :--------------------------------- | :------- | :--- |
| forest                  | `landuse=forest` or `natural=wood` | polygon  | 7+   |
| grass                   | `landuse=grass`                    | polygon  | 11+  |
| meadow                  | `landuse=meadow`                   | polygon  | 11+  |
| orchard                 | `landuse=orchard`                  | polygon  | 11+  |
| vineyard                | `landuse=vineyard`                 | polygon  | 11+  |
| allotments              | `landuse=allotments`               | polygon  | 11+  |
| cemetery                | `landuse=cemetery`                 | polygon  | 13+  |
| grave_yard              | `amenity=grave_yard`               | polygon  | 13+  |
| village_green           | `landuse=village_green`            | polygon  | 11+  |
| recreation_ground       | `landuse=recreation_ground`        | polygon  | 11+  |
| greenhouse_horticulture | `landuse=greenhouse_horticulture`  | polygon  | 11+  |
| plant_nursery           | `landuse=plant_nursery`            | polygon  | 11+  |
| sand                    | `natural=sand`                     | polygon  | 10+  |
| scrub                   | `natural=beach`                    | polygon  | 10+  |
| heath                   | `natural=heath`                    | polygon  | 11+  |
| scrub                   | `natural=scrub`                    | polygon  | 11+  |
| grassland               | `natural=grassland`                | polygon  | 11+  |
| bare\_rock              | `natural=bare_rock`                | polygon  | 11+  |
| scree                   | `natural=scree`                    | polygon  | 11+  |
| shingle                 | `natural=shingle`                  | polygon  | 11+  |
| swamp                   | `wetland=swamp`                    | polygon  | 11+  |
| bog                     | `wetland=bog`                      | polygon  | 11+  |
| string\_bog             | `wetland=string_bog`               | polygon  | 11+  |
| wet\_meadow             | `wetland=wet_meadow`               | polygon  | 11+  |
| marsh                   | `wetland=marsh`                    | polygon  | 11+  |
| golf\_course            | `leisure=golf_course`              | polygon  | 11+  |
| park                    | `leisure=park`                     | polygon  | 11+  |
| garden                  | `leisure=garden`                   | polygon  | 11+  |
| playground              | `leisure=playground`               | polygon  | 11+  |
| miniature\_golf         | `leisure=miniature_golf`           | polygon  | 11+  |
| residential             | `landuse=residential`              | polygon  | 10+  |
| industrial              | `landuse=industrial`               | polygon  | 10+  |
| commercial              | `landuse=commercial`               | polygon  | 10+  |
| garages                 | `landuse=garages`                  | polygon  | 10+  |
| retail                  | `landuse=retail`                   | polygon  | 10+  |
| railway                 | `landuse=railway`                  | polygon  | 10+  |
| landfill                | `landuse=landfill`                 | polygon  | 10+  |
| quarry                  | `landuse=quarry`                   | polygon  | 11+  |
| brownfield              | `landuse=brownfield`               | polygon  | 10+  |
| greenfield              | `landuse=greenfield`               | polygon  | 10+  |
| farmyard                | `landuse=farmyard`                 | polygon  | 10+  |
| farmland                | `landuse=farmland`                 | polygon  | 10+  |

### Layer "sites"

This layer is for types of land use that will usually be above the basic
land layer, but below buildings.

|                      | Value of `kind`   | OSM Tag                   | Label | Geometry | Zoom |
| -------------------- | :---------------- | :------------------------ | :---- | :------- | :--- |
| military danger area | `danger_area`     | `military=danger_area`    | name  | polygon  | 14+  |
| sports center        | `sports_center`   | `leisure=sports_center`   | name  | polygon  | 14+  |
| university campus    | `university`      | `amenity=university`      | name  | polygon  | 14+  |
| college campus       | `college`         | `amenity=college`         | name  | polygon  | 14+  |
| school campus        | `school`          | `amenity=school`          | name  | polygon  | 14+  |
| hospital campus      | `hospital`        | `amenity=hospital`        | name  | polygon  | 14+  |
| prison area          | `prison`          | `amenity=prison`          | name  | polygon  | 14+  |
| car park             | `parking`         | `amenity=parking`         | name  | polygon  | 14+  |
| bicycle parking      | `bicycle_parking` | `amenity=bicycle_parking` | name  | polygon  | 14+  |
| construction site    | `construction`    | `landuse=construction`    | name  | polygon  | 14+  |

### Layer "buildings"

Has polygons for everything with a building tag (not building=no) from
zoom 14 on.

### Layer "addresses"

Has points for everything with an address from zoom 14+. Polygons are represented by their centroid.

If a feature is available in the *pois* layer, it will not be duplicated in the *addresses* layer.

#### Properties

| Field Name    | Type    | OSM Key              |
| ------------- | :------ | :------------------- |
| `housename`   | string  | `addr:housename=*`   |
| `housenumber` | string  | `addr:housenumber=*` |

## Streets and Transport

### Layer "streets"

Holds line geometries of the whole road network. Features are ordered by the so-called z-order value which is computed
from road class, OSM `layer=*`, `bridge=*` and `tunnel=*` tags. More important roads are are sorted before less important roads, tunnels before bridges.

#### Properties

| Field Name     | Type     | Zoom | Default             | Description                                                                             |
| -------------- | :------- | :--- | :------------------ | :-------------------------------------------------------------------------------------- |
| kind           | string   | 5+   | always set          | Feature class, contains value of `highway=*`, `aeroway=*` or `railway=*`                |
| link           | boolean  | 11+  | false               | true for link roads (`highway=(motorway|trunk|primary|secondary|tertiary)_link`)        |
| rail           | boolean  | 5+   | false               | true for railways, false otherwise                                                      |
| tunnel         | boolean  | 11+  | false               | true for `tunnel=yes/building_passage` or `covered=yes`, `false` otherwise              |
| bridge         | boolean  | 11+  | false               | true for `bridge=yes`, `false` otherwise                                                |
| oneway         | boolean  | 14+  | false               | true for `oneway=yes/1/true/-1`; always false for rail features                         |
| oneway_reverse | boolean  | 14+  | false               | true for reverse (not reversible) oneways (`oneway=-1`); always false for rail features |
| tracktype      | string   | 11+  | field not available | value of `tracktype=*`                                                                  |
| surface        | string   | 11+  | empty string        | value of `surface=*`                                                                    |
| service        | string   | 11+  | field not available | value of `service=*`                                                                    |
| bicycle        | string   | 14+  | empty string        | value of `bicycle=*`                                                                    |
| horse          | string   | 14+  | empty string        | value of `horse=*`                                                                      |

#### Features

The following features are available in this layer:

| Feature Class                       | value of `kind`  | Zoom  | Comment                                                                              |
| ----------------------------------- | :--------------- | :---- | :----------------------------------------------------------------------------------- |
| motorway                            | `motorway`       | 5+    |                                                                                      |
| trunk roads                         | `trunk`          | 6+    |                                                                                      |
| primary roads                       | `primary`        | 8+    |                                                                                      |
| secondary roads                     | `secondary`      | 9+    |                                                                                      |
| tertiary roads                      | `tertiary`       | 10+   |                                                                                      |
| side roads                          | `unclassified`   | 12+   |                                                                                      |
| residential roads                   | `residential`    | 12+   |                                                                                      |
| roads exclusively for buses         | `busway`         | 12+   |                                                                                      |
| bus guideways                       | `bus_guideway`   | 12+   |                                                                                      |
| residential roads w/traffic calming | `living_street`  | 13+   |                                                                                      |
| service roads                       | `service`        | 13+   |                                                                                      |
| pedestrian roads                    | `pedestrian`     | 13+   |                                                                                      |
| tracks                              | `track`          | 13+   |                                                                                      |
| footpaths                           | `footway`        | 13+   |                                                                                      |
| steps                               | `steps`          | 13+   |                                                                                      |
| unspecified paths                   | `path`           | 13+   | use the `bicycle` and `horse` attributes for details about permitted use of the path |
| bicycle paths                       | `cycleway`       | 13+   |                                                                                      |
| runway                              | `runway`         | 11+   |                                                                                      |
| taxiway                             | `taxiway`        | 13+   |                                                                                      |
| railway                             | `rail`           | 8/10+ | ways with `service=*` on zoom level 8+, other ways on zoom level 10+                 |
| narrow gauge railway                | `narrow_gauge`   | 8+    | ways with `service=*` on zoom level 8+, other ways on zoom level 10+                 |
| tram                                | `tram`           | 10+   |                                                                                      |
| light railway                       | `light_rail`     | 10+   |                                                                                      |
| funicular                           | `funicular`      | 10+   |                                                                                      |
| subway                              | `subway`         | 10+   |                                                                                      |
| monorail                            | `monorail`       | 10+   |                                                                                      |

### Layer "street\_polygons"

Holds polygons geometries of certain streets mapped as polygons. Features are ordered by the so-called z-order value which is computed
from road class, OSM `layer=*`, `bridge=*` and `tunnel=*` tags. More important roads are are sorted before less important roads, tunnels before bridges.

#### Properties

| Field Name | Type     | Default             | Description                                                                      |
| ---------- | :------- | :------------------ | :------------------------------------------------------------------------------- |
| kind       | string   | always set          | Feature class, contains value of `highway=*` or `area:aeroway=*`                 |
| rail       | boolean  | false               | true for railways, false otherwise                                               |
| tunnel     | boolean  | false               | true for `tunnel=yes/building_passage` or `covered=yes`, `false` otherwise       |
| bridge     | boolean  | false               | true for `bridge=yes`, `false` otherwise                                         |
| surface    | string   | empty string        | value of `surface=*`                                                             |

#### Features

The following features are available in this layer:

| Feature Class  | value of `kind`  | Zoom  |
| -------------- | :--------------- | :---- |
| pedestrian     | `pedestrian`     | 14+   |
| service roads  | `service`        | 14+   |
| runway         | `runway`         | 11+   |
| taxiway        | `taxiway`        | 13+   |


### Layer "street\_labels"

This layer holds street geometries for labelling. It contains their names and reference numbers.

#### Features

| Feature Class                       | value of `kind`  | Zoom  |
| ----------------------------------- | :--------------- | :---- |
| motorway                            | `motorway`       | 10+   |
| motorway links                      | `motorway_link`  | 13+   |
| trunk roads                         | `trunk`          | 12+   |
| trunk roads                         | `trunk_link`     | 13+   |
| primary roads                       | `primary`        | 12+   |
| primary links                       | `primary_link`   | 13+   |
| secondary roads                     | `secondary`      | 13+   |
| secondary links                     | `secondary_link` | 13+   |
| tertiary roads                      | `tertiary`       | 13+   |
| teratiary links                     | `tertiary_link`  | 14+   |
| side roads                          | `unclassified`   | 14+   |
| residential roads                   | `residential`    | 14+   |
| residential roads w/traffic calming | `living_street`  | 14+   |
| roads exclusively for buses         | `busway`         | 14+   |
| bus guideways                       | `bus_guideway`   | 14+   |
| service roads                       | `service`        | 14+   |
| pedestrian roads                    | `pedestrian`     | 14+   |
| tracks                              | `track`          | 14+   |
| footpaths                           | `footway`        | 14+   |
| steps                               | `steps`          | 14+   |
| unspecified paths                   | `path`           | 14+   |
| bicycle paths                       | `cycleway`       | 14+   |
| runway                              | `runway`         | 11+   |
| taxiway                             | `taxiway`        | 13+   |
| railway                             | `rail`           | 10+   |
| narrow gauge railway                | `narrow_gauge`   | 10+   |
| tram                                | `tram`           | 10+   |
| light railway                       | `light_rail`     | 10+   |
| funicular                           | `funicular`      | 10+   |
| subway                              | `subway`         | 10+   |
| monorail                            | `monorail`       | 10+   |

#### Properties

| Field Name   | Type     | OSM Key                                                                                  |
| ------------ | :------- | :--------------------------------------------------------------------------------------- |
| `kind`       | string   | value of OSM `highway=*`, `aeroway=*` or `taxiway=*` tag                                 |
| `ref`        | string   | value of OSM `ref=*` tag, semicolons replaced by newline characters (ASCII character 10) |
| `ref_rows`   | numeric  | number of lines of the `ref` value                                                       |
| `ref_cols`   | numeric  | maximum line length of the `ref` value                                                   |
| `name`       | string   | value of OSM `name=*` tag                                                                |
| `name_en`    | string   | value of OSM `name:en=*` tag                                                             |
| `name_de`    | string   | value of OSM `name:de=*` tag                                                             |

### Layer "streets_polygons_labels"

Holds labelling points of the polygons of the "streets_polygons" layer.

#### Properties

| Field Name   | Type     | OSM Key                                     |
| ------------ | :------- | :------------------------------------------ |
| `kind`       | string   | value of OSM `highway=*` or `aeroway=*` tag |
| `name`       | string   | value of OSM `name=*` tag                   |
| `name_en`    | string   | value of OSM `name:en=*` tag                |
| `name_de`    | string   | value of OSM `name:de=*` tag                |

#### Features

The following features are available in this layer:

| Feature Class  | value of `kind`  | Zoom  |
| -------------- | :--------------- | :---- |
| pedestrian     | `pedestrian`     | 14+   |
| service roads  | `service`        | 14+   |
| runway         | `runway`         | 14+   |
| taxiway        | `taxiway`        | 14+   |


### Layer "streets\_labels\_points"

This layer holds motorway exit labels.

#### Properties

| Field Name   | Type    | OSM Key                      |
| ------------ | :------ | :--------------------------- |
| `kind`       | string  | value of OSM `highway=*` tag |
| `ref`        | string  | value of OSM `ref=*` tag     |
| `name`       | string  | value of OSM `name=*` tag    |
| `name_en`    | string  | value of OSM `name:en=*` tag |
| `name_de`    | string  | value of OSM `name:de=*` tag |

#### Features

The following features are available in this layer:

| Feature Class        | value of `kind`     | Zoom |
| -------------------- | :------------------ | :--- |
| motorway exit points | `motorway_junction` | 12+  |


### Layer "bridges"

This layer contains bridges mapped as polygons. There is no distinction which type of road, railway, runway or
waterway uses this bridge.

Please mind that only some bridges are mapped as polygons but almost all roads located on a bridge have their
location on a bridge as an attribute (see *streets* layer for details).

#### Properties

| Field Name  | Type    | Description                              |
| ----------- | :------ | :--------------------------------------- |
| kind        | string  | see Features section for possible values |


#### Features

| `kind` | OSM Tags          | Geometry | Zoom |
| ------ | :---------------- | :------- | :--- |
| bridge | `man_made=bridge` | polygon  | 12+  |


### Layer "aerialways"

Holds aerialways as lines.

#### Properties

| Field Name | Type     | OSM Key        |
| ---------- | :------- | :------------- |
| `kind`     | string   | `aerialway=*`  |


#### Features

| Feature Class   | value of `kind` | OSM Tag                 | Zoom |
| --------------- | :-------------- | :---------------------- | :--- |
| cable car       | `cable_car`     | `aerialways=cable_car`  | 12+  |
| gondola         | `gondola`       | `aerialways=gondola`    | 12+  |
| goods cable car | `goods`         | `aerialways=goods`      | 12+  |
| chair lift      | `chair_lift`    | `aerialways=chair_lift` | 12+  |
| drag lift       | `drag_lift`     | `aerialways=drag_lift`  | 12+  |
| t-bar lift      | `t-bar`         | `aerialways=t-bar`      | 12+  |
| j-bar lift      | `j-bar`         | `aerialways=j-bar`      | 12+  |
| platter lift    | `platter`       | `aerialways=platter`    | 12+  |
| rope-tow lift   | `rope-tow`      | `aerialways=rope_tow`   | 12+  |


### Layer "ferries"

Holds line geometries of ferries.

#### Properties

| Field Name   | Type    | OSM Key                      |
| ------------ | :------ | :--------------------------- |
| `kind`       | string  |                              |
| `name`       | string  | value of OSM `name=*` tag    |
| `name_en`    | string  | value of OSM `name:en=*` tag |
| `name_de`    | string  | value of OSM `name:de=*` tag |

#### Features

The following features are available in this layer:

| Feature Class         | value of `kind` | OSM Tag                              | Zoom |
| --------------------- | :-------------- | :----------------------------------- | :--- |
| motor vehicle ferries | `ferry`         | `route=ferry` + `motor_vehicle!=no`  | 10+  |
| all ferries           | `ferry`         | `route=ferry`                        | 12+  |


## Points of interest

### Layer "public\_transport"

Holds public transport stops as points. Areas in OSM are represented by their centroid.

#### Properties

| Field Name  | Type   | Description                  |
| ----------- | :----- | :--------------------------- |
| `kind`      | string | feature class                |
| `name`      | string | value of OSM `name=*` tag    |
| `name_en`   | string | value of OSM `name:en=*` tag |
| `name_de`   | string | value of OSM `name:de=*` tag |

#### Features

| Feature Class      | value of `kind`      | OSM Tag                    | Zoom |
| ------------------ | :------------------- | :------------------------- | :--- |
| airport, aerodrome | `aerodrome`          | `aeroway=aerodrome`        | 11+  |
| helipad            | `helipad`            | `aeroway=helipad`          | 13+  |
| station            | `station`            | `railway=station`          | 13+  |
| halt               | `halt`               | `railway=halt`             | 13+  |
| tram_stop          | `tram_stop`          | `railway=tram_stop`        | 14+  |
| bus_station        | `bus_station`        | `amenity=bus_station`      | 13+  |
| bus_stop           | `bus_stop`           | `highway=bus_stop`         | 14+  |
| ferry terminal     | `ferry_terminal`     | `aerialway=ferry_terminal` | 12+  |
| aerialway station  | `aerialway_station`  | `aerialway=station`        | 13+  |


### Layer "pois"

Holds points of interest as point geometries. Areas in OSM are represented by their centroid.

All features are available on zoom level 14 only.

#### Properties

| Field Name    | Type   | Default | Description                                                                 |
| ------------- | :----- | :------ | :-------------------------------------------------------------------------- |
| `amenity`     | string | null    | value of OSM `amenity=*` tag if listed in the "Features" subsection below   |
| `leisure`     | string | null    | value of OSM `leisure=*` tag if listed in the "Features" subsection below   |
| `tourism`     | string | null    | value of OSM `tourism=*` tag if listed in the "Features" subsection below   |
| `shop`        | string | null    | value of OSM `shop=*` tag if listed in the "Features" subsection below      |
| `man_made`    | string | null    | value of OSM `man_made=*` tag if listed in the "Features" subsection below  |
| `historic`    | string | null    | value of OSM `historic=*` tag if listed in the "Features" subsection below  |
| `emergency`   | string | null    | value of OSM `emergency=*` tag if listed in the "Features" subsection below |
| `highway`     | string | null    | value of OSM `highway=*` tag if listed in the "Features" subsection below   |
| `office`      | string | null    | value of OSM `office=*` tag if listed in the "Features" subsection below    |
| `name`        | string | null    | value of OSM `name=*` tag                                                   |
| `name_en`     | string | null    | value of OSM `name:en=*` tag                                                |
| `name_de`     | string | null    | value of OSM `name:de=*` tag                                                |
| `housename`   | string | null    | `addr:housename=*`                                                          |
| `housenumber` | string | null    | `addr:housenumber=*`                                                        |

The following attributes are set for selected features only. Their value comes from the equally named OSM keys.

| Field Name               | Type    | Default | Selection criteria (OSM tags)               |
| ------------------------ | :------ | :------ | :------------------------------------------ |
| `cuisine`                | string  | null    | `amenity=restaurant/fast_food/pub/bar/cafe` |
| `sport`                  | string  | null    | `leisure=pitch/sports_centre`               |
| `vending`                | string  | null    | `amenity=vending_machine`                   |
| `information`            | string  | null    | `tourism=information`                       |
| `tower:type`             | string  | null    | `man_made=tower`                            |
| `religion`               | string  | null    | `amenity=place_of_worship`                  |
| `denomination`           | string  | null    | `amenity=place_of_worship`                  |

The following attributes are set for selected features only. They are true if the specified OSM key has the value `yes`.

| Field Name               | Type    | Default | Selection criteria (OSM tags)  |
| ------------------------ | :------ | :------ | :----------------------------- |
| `recycling:glass_bottles`| boolean | false   | `amenity=recycling`            |
| `recycling:paper`        | boolean | false   | `amenity=recycling`            |
| `recycling:clothes`      | boolean | false   | `amenity=recycling`            |
| `recycling:scrap_metal`  | boolean | false   | `amenity=recycling`            |
| `atm`                    | boolean | false   | `amenity=bank`                 |

#### Features

The following key-value combinations are included in this layer:

| Key               | Value                    |
| ----------------- | :----------------------- |
| `amenity`         | `police`                 |
| `amenity`         | `fire_station`           |
| `amenity`         | `post_box`               |
| `amenity`         | `post_office`            |
| `amenity`         | `telephone`              |
| `amenity`         | `library`                |
| `amenity`         | `townhall`               |
| `amenity`         | `courthouse`             |
| `amenity`         | `prison`                 |
| `amenity`         | `embassy`                |
| `amenity`         | `community_centre`       |
| `amenity`         | `nursing_home`           |
| `amenity`         | `arts_centre`            |
| `amenity`         | `grave_yard`             |
| `amenity`         | `marketplace`            |
| `amenity`         | `recycling`              |
| `amenity`         | `university`             |
| `amenity`         | `school`                 |
| `amenity`         | `college`                |
| `amenity`         | `public_building`        |
| `amenity`         | `pharmacy`               |
| `amenity`         | `hospital`               |
| `amenity`         | `clinic`                 |
| `amenity`         | `doctors`                |
| `amenity`         | `denitst`                |
| `amenity`         | `veterinary`             |
| `amenity`         | `theatre`                |
| `amenity`         | `nightclub`              |
| `amenity`         | `cinema`                 |
| `amenity`         | `restaurant`             |
| `amenity`         | `fast_food`              |
| `amenity`         | `cafe`                   |
| `amenity`         | `pub`                    |
| `amenity`         | `bar`                    |
| `amenity`         | `foot_court`             |
| `amenity`         | `biergarten`             |
| `amenity`         | `shelter`                |
| `amenity`         | `car_rental`             |
| `amenity`         | `car_wash`               |
| `amenity`         | `car_sharing`            |
| `amenity`         | `bicycle_rental`         |
| `amenity`         | `vending_machine`        |
| `amenity`         | `bank`                   |
| `amenity`         | `atm`                    |
| `amenity`         | `toilets`                |
| `amenity`         | `bench`                  |
| `amenity`         | `drinking_water`         |
| `amenity`         | `fountain`               |
| `amenity`         | `hunting_stand`          |
| `amenity`         | `waste_basket`           |
| `amenity`         | `place_of_worship`       |
| `amenity`         | `playground`             |
| `amenity`         | `dog_park`               |
| `leisure`         | `sports_centre`          |
| `leisure`         | `pitch`                  |
| `leisure`         | `swimming_pool`          |
| `leisure`         | `water_park`             |
| `leisure`         | `golf_course`            |
| `leisure`         | `stadium`                |
| `leisure`         | `ice_rink`               |
| `tourism`         | `hotel`                  |
| `tourism`         | `motel`                  |
| `tourism`         | `bed_and_breakfast`      |
| `tourism`         | `guest_house`            |
| `tourism`         | `hostel`                 |
| `tourism`         | `chalet`                 |
| `tourism`         | `camp_site`              |
| `tourism`         | `alpine_hut`             |
| `tourism`         | `caravan_site`           |
| `tourism`         | `information`            |
| `tourism`         | `picnic_site`            |
| `tourism`         | `viewpoint`              |
| `tourism`         | `zoo`                    |
| `tourism`         | `theme_park`             |
| `shop`            | `supermarket`            |
| `shop`            | `bakery`                 |
| `shop`            | `kiosk`                  |
| `shop`            | `mall`                   |
| `shop`            | `department_store`       |
| `shop`            | `general`                |
| `shop`            | `convinience`            |
| `shop`            | `clothes`                |
| `shop`            | `florist`                |
| `shop`            | `chemist`                |
| `shop`            | `books`                  |
| `shop`            | `butcher`                |
| `shop`            | `shoes`                  |
| `shop`            | `alcohol`                |
| `shop`            | `beverages`              |
| `shop`            | `optican`                |
| `shop`            | `jewelry`                |
| `shop`            | `gift`                   |
| `shop`            | `sports`                 |
| `shop`            | `stationery`             |
| `shop`            | `outdoor`                |
| `shop`            | `mobile_phone`           |
| `shop`            | `toys`                   |
| `shop`            | `newsagent`              |
| `shop`            | `greengrocer`            |
| `shop`            | `beauty`                 |
| `shop`            | `video`                  |
| `shop`            | `car`                    |
| `shop`            | `bicycle`                |
| `shop`            | `doityourself`           |
| `shop`            | `hardware`               |
| `shop`            | `furniture`              |
| `shop`            | `computer`               |
| `shop`            | `garden_centre`          |
| `shop`            | `hairdresser`            |
| `shop`            | `travel_agency`          |
| `shop`            | `laundry`                |
| `shop`            | `dry_cleaning`           |
| `man_made`        | `surveillance`           |
| `man_made`        | `tower`                  |
| `man_made`        | `windmill`               |
| `man_made`        | `lighthouse`             |
| `man_made`        | `wastewater_plant`       |
| `man_made`        | `water_well`             |
| `man_made`        | `watermill`              |
| `man_made`        | `water_works`            |
| `historic`        | `monument`               |
| `historic`        | `memorial`               |
| `historic`        | `artwork`                |
| `historic`        | `castle`                 |
| `historic`        | `ruins`                  |
| `historic`        | `archaelogical_site`     |
| `historic`        | `wayside_cross`          |
| `historic`        | `wayside_shrine`         |
| `historic`        | `battlefield`            |
| `historic`        | `fort`                   |
| `emergency`       | `phone`                  |
| `emergency`       | `fire_hydrant`           |
| `emergency`       | `defibrillator`          |
| `highway`         | `emergency_access_point` |
| `office`          | `diplomatic`             |

