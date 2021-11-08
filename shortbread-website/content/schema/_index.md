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

|            |              | Geometry| Zoom |
| ---------- | :----------- | :------ | :-   |
| coastlines | sea polygons | polygon | 0+   |

### Layer "water\_polygons"

This layer contains inland water bodies and glaciers.

#### Properties

| Field Name | Type   | Description        |
| ---------- | :----- | :----------------- |
| `kind`     | string | type of water body |

#### Features

|           | `kind`    | OSM tag              | Geometry | Zoom |
| --------- | :-------- | :------------------- | :------- | :--- |
| glacier   | glacier   | `natural=glacier`    | polygon  | 4+   |
| water     | water     | `natural=water`      | polygon  | 4+   |
| river     | riverbank | `waterway=riverbank` | polygon  | 4+   |
| reservoir | reservoir | `landuse=reservoir`  | polygon  | 4+   |
| reservoir | basin     | `landuse=basin`      | polygon  | 4+   |
| dock      | dock      | `waterway=dock`      | polygon  | 10+  |
| canal     | canal     | `waterway=canal`     | polygon  | 10+  |

### Layer "water\_polygons\_labels"

Holds point (centroid) geometries and names for all named water polygons available in the *water\_polygons* layer.

#### Properties

| Field name | Type   | Description                                                            |
| ---------- | :----- | :--------------------------------------------------------------------- |
| `kind`     | string | type of water body (see *water\_polygons* layer for a list of values)  |
| `name`     | string | value of OSM `name=*` tag                                              |
| `name_en`  | string | value of OSM `name:en=*` tag                                           |
| `name_de`  | string | value of OSM `name:de=*` tag                                           |

### Layer "water\_lines"

Holds waterway line geometries.

#### Properties

| Field Name | Type   | Description      |
| ---------- | :----- | :--------------- |
| `kind`     | string | type of waterway |

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

## Countries, States, Cities

### Layer "boundaries"

Holds boundary lines of countries and states.


#### Properties

| Field name    | Type   | Description                                                                |
| ------------- | :----- | :------------------------------------------------------------------------- |
| `admin_level` | string | value of OSM `admin_level=*` tag, see Features section for possible values |


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
| `admin_level` | string  | value of OSM `admin_level=*` tag, see Features section for possible values |
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
| `population` | numeric | value of OSM `population=*` tag                                        |

#### Features

|                   | Value of `kind`      | OSM Tags                                         | Geometry | Zoom |
| ----------------- | :------------------- | :----------------------------------------------- | :------- | :--- |
| national capital  | `capital`            | `place=city/town/village/hamlet` + `capital=yes` | point    | 4+   |
| state capital     | `state_capital`      | `place=city/town/village/hamlet` + `capital=4`   | point    | 4+   |
| city              | `city`               | `place=city` (except capitals)                   | point    | 6+   |
| town              | `town`               | `place=town` (except capitals)                   | point    | 7+   |
| village           | `village`            | `place=village` (except capitals)                | point    | 10+  |
| hamlet            | `hamlet`             | `place=hamlet` (except capitals)                 | point    | 10+  |
| suburb            | `suburb`             | `place=suburb`                                   | point    | 10+  |
| neighbourhood     | `neighbourhood`      | `place=neighbourhood`                            | point    | 10+  |
| isolated dewlling | `isolated_dwelling`  | `place=isolated_dwelling`                        | point    | 10+  |
| farm              | `farm`               | `place=farm`                                     | point    | 10+  |

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
| planet_nursery          | `landuse=plant_nursery`            | polygon  | 11+  |
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

#### Properties

| Field Name | Type    | OSM Key              |
| ---------- | :------ | :------------------- |
| `name`     | string  | `addr:housename=*`   |
| `number`   | string  | `addr:housenumber=*` |

## Streets and Transport

### Layer "streets"

Holds line geometries of the whole road network. Features are ordered by the so-called z-order value which is computed
from road class, OSM `layer=*`, `bridge=*` and `tunnel=*` tags. More important roads are are sorted before less important roads, tunnels before bridges.

#### Properties

| Field Name | Type     | Zoom | Default             | Description                                                                      |
| ---------- | :------- | :--- | :------------------ | :------------------------------------------------------------------------------- |
| kind       | string   | 5+   | always set          | Feature class, contains value of `highway=*` or `railway=*`                      |
| link       | boolean  | 11+  | false               | true for link roads (`highway=(motorway|trunk|primary|secondary|tertiary)_link`) |
| rail       | boolean  | 5+   | false               | true for railways, false otherwise                                               |
| tunnel     | boolean  | 11+  | false               | true for `tunnel=yes/building_passage` or `covered=yes`, `false` otherwise       |
| bridge     | boolean  | 11+  | false               | true for `bridge=yes`, `false` otherwise                                         |
| tracktype  | string   | 11+  | field not available | value of `tracktype=*`                                                           |
| surface    | string   | 11+  | empty string        | value of `surface=*`                                                             |
| service    | string   | 11+  | field not available | value of `service=*`                                                             |
| bicycle    | string   | 14+  | empty string        | value of `bicycle=*`                                                             |
| horse      | string   | 14+  | empty string        | value of `horse=*`                                                               |

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

### Layer "street_polygons"

Holds polygons geometries of certain streets mapped as polygons. Features are ordered by the so-called z-order value which is computed
from road class, OSM `layer=*`, `bridge=*` and `tunnel=*` tags. More important roads are are sorted before less important roads, tunnels before bridges.

#### Properties

| Field Name | Type     | Default             | Description                                                                      |
| ---------- | :------- | :------------------ | :------------------------------------------------------------------------------- |
| kind       | string   | always set          | Feature class, contains value of `highway=*`                      |
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
| service roads                       | `service`        | 14+   |
| pedestrian roads                    | `pedestrian`     | 14+   |
| tracks                              | `track`          | 14+   |
| footpaths                           | `footway`        | 14+   |
| steps                               | `steps`          | 14+   |
| unspecified paths                   | `path`           | 14+   |
| bicycle paths                       | `cycleway`       | 14+   |

#### Properties

| Field Name   | Type     | OSM Key                                                                                  |
| ------------ | :------- | :--------------------------------------------------------------------------------------- |
| `kind`       | string   | value of OSM `highway=*` tag                                                             |
| `ref`        | string   | value of OSM `ref=*` tag, semicolons replaced by newline characters (ASCII character 10) |
| `ref_rows`   | numeric  | number of lines of the `ref` value                                                       |
| `ref_cols`   | numeric  | maximum line length of the `ref` value                                                   |
| `name`       | string   | value of OSM `name=*` tag                                                                |
| `name_en`    | string   | value of OSM `name:en=*` tag                                                             |
| `name_de`    | string   | value of OSM `name:de=*` tag                                                             |

### Layer "streets_polygons_labels"

Holds labelling points of the polygons of the "streets_polygons" layer.

#### Properties

| Field Name   | Type     | OSM Key                       |
| ------------ | :------- | :---------------------------- |
| `kind`       | string   | value of OSM `highway=*` tag  |
| `name`       | string   | value of OSM `name=*` tag     |
| `name_en`    | string   | value of OSM `name:en=*` tag  |
| `name_de`    | string   | value of OSM `name:de=*` tag  |

#### Features

The following features are available in this layer:

| Feature Class  | value of `kind`  | Zoom  |
| -------------- | :--------------- | :---- |
| pedestrian     | `pedestrian`     | 14+   |
| service roads  | `service`        | 14+   |


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

| Feature Class      | value of `kind`      | OSM Tag              | Zoom |
| ------------------ | :------------------- | :------------------- | :--- |
| airport, aerodrome | `aerodrome`          | `aeroway=aerodrome`  | 11+  |
| station            | `station`            | `railway=station`    | 13+  |
| halt               | `halt`               | `railway=halt`       | 13+  |
| tram_stop          | `tram_stop`          | `railway=tram_stop`  | 14+  |
| aerialway station  | `aerialway_station`  | `aerialway=station`  | 13+  |
