+++
draft= false
title = "Vector Tile Schema"
description = "This page describes the layers of the Shortbread vector schema and their contents"
+++

## About

The Geofabrik "basic" vector tile schema is intended to be a basic, lean, general-purpose vector tile schema for OpenStreetMap data.

It does not, and is not intended to, cover the full breadth and depth of OpenStreetMap tagging.

This document describes the layers that are defined in the vector tile schema, and the features and attributes available on each layer.

## **Water**

### Layer "ocean"

This layer contains oceans.

|            |              | geometry| zoom |
| ---------- | :----------- | :------ | :-   |
| coastlines | sea polygons | polygon | 0+   |

### Layer "water\_polygons"

This layer contains inland water bodies and glaciers.

#### Properties

| field name | type   | description        |
| ---------- | :----- | :----------------- |
| kind       | string | type of water body |

#### Features

|           | kind      | OSM                | geometry | zoom |
| --------- | :-------- | :----------------- | :------- | :--- |
| glacier   | glacier   | natural=glacier    | polygon  | 4+   |
| water     | water     | natural=water      | polygon  | 4+   |
| river     | riverbank | waterway=riverbank | polygon  | 4+   |
| reservoir | reservoir | landuse=reservoir  | polygon  | 4+   |
| reservoir | basin     | landuse=basin      | polygon  | 4+   |
| dock      | dock      | waterway=dock      | polygon  | 10+  |
| canal     | canal     | waterway=canal     | polygon  | 10+  |

### Layer "water\_polygons\_labels"

Holds point (centroid) geometries and names for all named water polygons available in the *water\_polygons* layer.

#### Properties

| field name | type   | description                                                           |
| ---------- | :----- | :-------------------------------------------------------------------- |
| kind       | string | type of water body (see *water\_polygons* layer for a list of values) |
| name       | string | value of OSM name=* tag                                               |
| name_en    | string | value of OSM name=:en* tag                                            |
| name_de    | string | value of OSM name=:de* tag                                            |

### Layer "water\_lines"

Holds waterway line geometries.

#### Properties

| field name | type   | description      |
| ---------- | :----- | :--------------- |
| kind       | string | type of waterway |

#### Features

|        | kind   | OSM             | geometry | zoom |
| ------ | :----- | :-------------- | :------- | :--- |
| canal  | canal  | waterway=canal  | line     | 10+  |
| river  | river  | waterway=river  | line     | 10+  |
| stream | stream | waterway=stream | line     | 14+  |
| ditch  | ditch  | waterway=ditch  | line     | 14+  |

### Layer "water\_lines\_labels"

Hold line geometries and names for water lines.

#### Properties

| field name | type   | description                                                           |
| ---------- | :----- | :-------------------------------------------------------------------- |
| kind       | string | type of water body (see *water\_lines* layer for a list of values) |
| name       | string | value of OSM name=* tag                                               |
| name_en    | string | value of OSM name=:en* tag                                            |
| name_de    | string | value of OSM name=:de* tag                                            |

## Countries, States, Cities

### Layer "boundaries"

Holds boundary lines of countries and states.


#### Properties

| field name  | type   | description                                                                |
| ----------- | :----- | :------------------------------------------------------------------------- |
| admin_level | string | value of OSM `admin_level=*` tag, see Features section for possible values |


#### Features

|           | admin\_level | geometry | zoom |
| --------- | :----------- | :------- | :--- |
| countries | 2            | line     | 0+   |
| states    | 4            | line     | 7+   |

### Layer "boundary\_labels"

Holds label points for boundary polygons of countries and states


#### Properties

| field name  | type   | description                                                                |
| ----------- | :----- | :------------------------------------------------------------------------- |
| admin_level | string | value of OSM `admin_level=*` tag, see Features section for possible values |
| name        | string | value of OSM name=* tag                                                    |
| name_en     | string | value of OSM name=:en* tag                                                 |
| name_de     | string | value of OSM name=:de* tag                                                 |

#### Features

|           | admin\_level | geometry | minimum area | zoom |
| --------- | :----------- | :------- | :----------- | :--- |
| countries | 2            | line     | 2*10^6 km²   | 2+   |
| countries | 2            | line     | 7*10^5 km²   | 3+   |
| countries | 2            | line     | 1*10^5 km²   | 4+   |
| countries | 2            | line     | none         | 5+   |
| states    | 4            | line     | 7*10^5 km²   | 3+   |
| states    | 4            | line     | 1*10^5 km²   | 4+   |
| states    | 4            | line     | none         | 5+   |

### Layer "place\_labels"

Holds label points for populated places.

#### Properties

| field name  | type    | description                                                                |
| ----------- | :------ | :------------------------------------------------------------------------- |
| kind        | string  | value of OSM `place=*` tag, see Features section for possible values       |
| name        | string  | value of OSM name=* tag                                                    |
| name_en     | string  | value of OSM name=:en* tag                                                 |
| name_de     | string  | value of OSM name=:de* tag                                                 |
| population  | numeric | value of OSM `population=*` tag                                            |

#### Features

|                   | kind               | OSM                                          | geometry | zoom |
| ----------------- | :----------------- | :------------------------------------------- | :------- | :--- |
| national capital  | capital            | place=city/town/village/hamlet + capital=yes | point    | 4+   |
| state capital     | state\_capital     | place=city/town/village/hamlet + capital=4   | point    | 4+   |
| city              | city               | place=city (except capitals)                 | point    | 6+   |
| town              | town               | place=town (except capitals)                 | point    | 7+   |
| village           | village            | place=village (except capitals)              | point    | 10+  |
| hamlet            | hamlet             | place=hamlet (except capitals)               | point    | 10+  |
| suburb            | suburb             | place=suburb                                 | point    | 10+  |
| neighbourhood     | neighbourhood      | place=neighbourhood                          | point    | 10+  |
| isolated dewlling | isolated\_dwelling | place=isolated_dwelling                      | point    | 10+  |
| farm              | farm               | place=farm                                   | point    | 10+  |

## Land Use, Land Cover, Buildings

### Layer "land"

This layer contains basic land cover that is usually drawn first.

#### Properties

| field name  | type    | description                              |
| ----------- | :------ | :--------------------------------------- |
| kind        | string  | see Features section for possible values |


#### Features
| kind                    | OSM                             | geometry | zoom |
| ----------------------- | :------------------------------ | :------- | :--- |
| forest                  | landuse=forest, natural=wood    | polygon  | 7+   |
| grass                   | landuse=grass                   | polygon  | 11+  |
| meadow                  | landuse=meadow                  | polygon  | 11+  |
| orchard                 | landuse=orchard                 | polygon  | 11+  |
| vineyard                | landuse=vineyard                | polygon  | 11+  |
| allotments              | landuse=allotments              | polygon  | 11+  |
| cemetery                | landuse=cemetery                | polygon  | 13+  |
| grave_yard              | amenity=grave\_yard             | polygon  | 13+  |
| village_green           | landuse=village_green           | polygon  | 11+  |
| recreation_ground       | landuse=recreation_ground       | polygon  | 11+  |
| greenhouse_horticulture | landuse=greenhouse_horticulture | polygon  | 11+  |
| planet_nursery          | landuse=greenhouse_horticulture | polygon  | 11+  |
| sand                    | natural=sand                    | polygon  | 10+  |
| scrub                   | natural=beach                   | polygon  | 10+  |
| heath                   | natural=heath                   | polygon  | 11+  |
| scrub                   | natural=scrub                   | polygon  | 11+  |
| grassland               | natural=grassland               | polygon  | 11+  |
| bare\_rock              | natural=bare\_rock              | polygon  | 11+  |
| scree                   | natural=scree                   | polygon  | 11+  |
| shingle                 | natural=shingle                 | polygon  | 11+  |
| swamp                   | wetland=swamp                   | polygon  | 11+  |
| bog                     | wetland=bog                     | polygon  | 11+  |
| string\_bog             | wetland=string\_bog             | polygon  | 11+  |
| wet\_meadow             | wetland=wet\_meadow             | polygon  | 11+  |
| marsh                   | wetland=marsh                   | polygon  | 11+  |
| golf\_course            | leisure=golf_course             | polygon  | 11+  |
| park                    | leisure=park                    | polygon  | 11+  |
| garden                  | leisure=garden                  | polygon  | 11+  |
| playground              | leisure=playground              | polygon  | 11+  |
| miniature\_golf         | leisure=miniature\_golf         | polygon  | 11+  |
| residential             | landuse=residential             | polygon  | 10+  |
| industrial              | landuse=industrial              | polygon  | 10+  |
| commercial              | landuse=commercial              | polygon  | 10+  |
| retail                  | landuse=retail                  | polygon  | 10+  |
| railway                 | landuse=railway                 | polygon  | 10+  |
| landfill                | landuse=landfill                | polygon  | 10+  |
| quarry                  | landuse=quarry                  | polygon  | 10+  |
| brownfield              | landuse=brownfield              | polygon  | 10+  |
| greenfield              | landuse=greenfield              | polygon  | 10+  |
| farmyard                | landuse=farmyard                | polygon  | 10+  |
| farmland                | landuse=farmland                | polygon  | 10+  |

### Layer "sites"

This layer is for types of land use that will usually be above the basic
land layer, but below buildings.

|                      | kind             | OSM                      | label | geometry | zoom |
| -------------------- | :--------------- | :----------------------- | :---- | :------- | :--- |
| military danger area | danger\_area     | military=danger\_area    | name  | polygon  | 14+  |
| sports center        | sports\_center   | leisure=sports\_center   | name  | polygon  | 14+  |
| university campus    | university       | amenity=university       | name  | polygon  | 14+  |
| hospital campus      | hospital         | amenity=hospital         | name  | polygon  | 14+  |
| prison area          | prison           | amenity=prison           | name  | polygon  | 14+  |
| car park             | parking          | amenity=parking          | name  | polygon  | 14+  |
| bicycle parking      | bicycle\_parking | amenity=bicycle\_parking | name  | polygon  | 14+  |
| construction site    | construction     | landuse=construction     | name  | polygon  | 14+  |

### Layer "buildings"

Has polygons for everything with a building tag (not building=no) from
zoom 14 on.

### Layer "addresses"

Has points for everything with an address from zoom 14+.

#### Properties

| field name | type    | OSM                |
| ---------- | :------ | :----------------- |
| name       | string  | addr:housename=*   |
| number     | string  | addr:housenumber=* |

## Streets and Transport

### Layer "streets"

#### Properties

| field name | type     | zoom | OSM                   | note                                                                             |
| ---------- | :------- | :--- | :-------------------- | :------------------------------------------------------------------------------- |
| kind       | string   | 6+   | highway=*, railway=*  | feature type (road class or type of railway)                                     |
| link       | boolean  | 6+   |                       | true for link roads (`highway=(motorway|trunk|primary|secondary|tertiary)_link`) |
| rail       | boolean  | 11+  |                       | true for railways, `false` otherwise                                             |
| tunnel     | boolean  | 11+  | tunnel=*              | true for `tunnel=yes/building_passage` or `covered=yes`, `false` otherwise       |
| bridge     | boolean  | 11+  | bridge=*              | true for `bridge=yes`, `false` otherwise                                         |
| tracktype  | string   | 11+  | tracktype=*           |                                                                                  |
| surface    | string   | 11+  | surface=*             |                                                                                  |
| service    | string   | 11+  | service=*             | available on all features if set in OSM                                          |
| bicycle    | string   | 14+  | bicycle=*             |                                                                                  |
| horse      | string   | 14+  | horse=*               |                                                                                  |
| name       | string   | 6+   | name=*                |                                                                                  |

#### Features 

|                                     | kind           | zoom | comment                                                                              |
| ----------------------------------- | :------------- | :--- | :----------------------------------------------------------------------------------- |
| **Roads and paths**                                                                                                                             ||||
| motorway                            | motorway       | 5+   |                                                                                      |
| trunk roads                         | trunk          | 5+   |                                                                                      |
| primary roads                       | primary        | 6+   |                                                                                      |
| secondary roads                     | secondary      | 9+   |                                                                                      |
| tertiary roads                      | tertiary       | 11+  |                                                                                      |
| side roads                          | unclassified   | 11+  |                                                                                      |
| residential roads                   | residential    | 11+  |                                                                                      |
| residential roads w/traffic calming | living\_street | 12+  |                                                                                      |
| service roads                       | service        | 12+  |                                                                                      |
| pedestrian roads                    | pedestrian     | 12+  |                                                                                      |
| tracks                              | track          | 12+  |                                                                                      |
| footpaths                           | footway        | 13+  |                                                                                      |
| steps                               | steps          | 13+  |                                                                                      |
| unspecified paths                   | path           | 13+  | use the `bicycle` and `horse` attributes for details about permitted use of the path |
| bicycle paths                       | cycleway       | 13+  |                                                                                      |
| **Runways and taxiways on airports**                                                                                                            ||||
| runway                              | runway         | 11+  |                                                                                      |
| taxiway                             | taxiway        | 11+  |                                                                                      |
| **Railway tracks**                                                                                                                              ||||
| railway                             | rail           | 5+   |                                                                                      |
| narrow gauge railway                | narrow\_gauge  | 10+  |                                                                                      |
| tram                                | tram           | 10+  |                                                                                      |
| light railway                       | light\_rail    | 10+  |                                                                                      |
| funicular                           | funicular      | 10+  |                                                                                      |
| subway                              | subway         | 10+  |                                                                                      |
| monorail                            | monorail       | 10+  |                                                                                      |


### Layer "street\_labels"

### streets\_labels\_points

This layer holds motorway exit labels.

#### Properties

| field name | type     | OSM        |
| ---------- | :------- | :--------- |
| kind       | string   | highway=*  |
| ref        | string   | ref=*      |

#### Features

The following features are available in this layer:

|                      | kind               | zoom |
| -------------------- | :----------------- | :--- |
| motorway exit points | motorway\_junction | 12+  |

### Layer "aerialways"

Holds aerialways as lines.

#### Properties

| field name | type     | OSM          |
| ---------- | :------- | :----------- |
| kind       | string   | aerialway=*  |


#### Features

|                 | kind        | OSM                    | zoom |
| --------------- | :---------- | :--------------------- | :--- |
| cable car       | cable\_car  | aerialways=cable\_car  | 12+  |
| gondola         | gondola     | aerialways=gondola     | 12+  |
| goods cable car | goods       | aerialways=goods       | 12+  |
| chair lift      | chair\_lift | aerialways=chair\_lift | 12+  |
| drag lift       | drag\_lift  | aerialways=drag\_lift  | 12+  |
| t-bar lift      | t-bar       | aerialways=t-bar       | 12+  |
| j-bar lift      | j-bar       | aerialways=j-bar       | 12+  |
| platter lift    | platter     | aerialways=platter     | 12+  |
| rope-tow lift   | rope-tow    | aerialways=rope\_tow   | 12+  |


### Layer "public\_transport"

Holds public transport stops as points. Areas in OSM are represented by their centroid.

#### Properties

| field name | type   | description                |
| ---------- | :----- | :------------------------- |
| kind       | string | feature class              |
| name       | string | value of OSM name=* tag    |
| name_en    | string | value of OSM name=:en* tag |
| name_de    | string | value of OSM name=:de* tag |

#### Features

|                    | kind               | OSM                | zoom |
| ------------------ | :----------------- | :----------------- | :--- |
| airport, aerodrome | aerodrome          | aeroway=aerodrome  | 11+  |
| station            | station            | railway=station    | 13+  |
| halt               | halt               | railway=halt       | 13+  |
| tram_stop          | tram\_stop         | railway=tram\_stop | 14+  |
| aerialway station  | aerialway\_station | aerialway=station  | 13+  |
