The Geofabrik "basic" vector tile schema is intended to be a basic,
lean, general-purpose vector tile schema for OpenStreetMap data.

It does not, and is not intended to, cover the full breadth and depth of
OpenStreetMap tagging.

This document describes the layers that are defined in the vector tile schema,
and the features and attributes available on each layer.

# **Water**

## Layer "ocean"

|            |              | geometry| zoom |
| ---------- | :----------- | :------ | :-   |
| coastlines | sea polygons | polygon | 0+   |
|            |              |         |      |

## Layer "water\_polygons"

|           | kind      | OSM                | geometry | zoom |
| --------- | :-------- | :----------------- | :------- | :--- |
| glacier   | glacier   | natural=glacier    | polygon  | 4+   |
| water     | water     | natural=water      | polygon  | 4+   |
| river     | riverbank | waterway=riverbank | polygon  | 4+   |
| reservoir | reservoir | landuse=reservoir  | polygon  | 4+   |
| reservoir | basin     | landuse=basin      | polygon  | 4+   |
| dock      | dock      | waterway=dock      | polygon  | 10+  |
| canal     | canal     | waterway=canal     | polygon  | 10+  |

## Layer "water\_polygons\_labels"

Holds point (centroid) geometries and names for all water polygons.

## Layer "water\_lines"

|        | kind   | OSM             | geometry | zoom |
| ------ | :----- | :-------------- | :------- | :--- |
| canal  | canal  | waterway=canal  | line     | 10+  |
| river  | river  | waterway=river  | line     | 10+  |
| stream | stream | waterway=stream | line     | 14+  |
| ditch  | ditch  | waterway=ditch  | line     | 14+  |

## Layer "water\_lines\_labels"

Hold line geometries and names for water lines.

# Countries, States, Cities

## Layer "boundaries"

|           | admin\_level | geometry | zoom |
| --------- | :----------- | :------- | :--- |
| countries | 2            | line     | 0+   |
| states    | 4            | line     | 7+   |

## Layer "boundary\_labels"

|           | admin\_level | label      | geometry | zoom |
| --------- | :----------- | :--------- | :------- | :--- |
| countries | 2            | name, etc. | point    | 2+   |
| states    | 4            | name, etc. | point    | 5+   |

## Layer "place\_labels"

|                   | class              | label      | geometry | zoom |
| ----------------- | :----------------- | :--------- | :------- | :--- |
| national capital  | capital            | name, etc. | point    | 4+   |
| state capital     | state\_capital     | name, etc. | point    | 4+   |
| city              | city               |            | point    | 6+   |
| town              | town               |            | point    | 7+   |
| village           | village            |            | point    | 10+  |
| hamlet            | hamlet             |            | point    | 10+  |
| suburb            | suburb             |            | point    | 10+  |
| neighbourhood     | neighbourhood      |            | point    | 10+  |
| isolated dewlling | isolated\_dwelling |            | point    | 10+  |
| farm              | farm               |            | point    | 10+  |

# Land Use, Land Cover, Buildings

## Layer "land"

This layer contains basic land cover that is usually drawn first.

|                  | kind                                                                                                                                 | OSM                                                                                                                                           | geometry | zoom |
| ---------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :--- |
| forest           | forest                                                                                                                               | landuse=forest, natural=wood                                                                                                                  | polygon  | 7+   |
| green areas      | grass, meadow, orchard, vineyard, cemetery, allotments, village\_green, recreation\_ground, greenhouse\_horticulture, plant\_nursery | landuse= grass, meadow, orchard, vineyard, cemetery, allotments, village\_green, recreation\_ground, greenhouse\_horticulture, plant\_nursery | polygon  | 11+  |
|                  | heath, scrub, grassland, bare\_rock, scree, shingle                                                                                  | natural=heath, scrub, grassland, bare\_rock, scree, shingle                                                                                   | polygon  | 11+  |
|                  | swamp, bog, string\_bog, wet\_meadow, marsh                                                                                          | wetland=swamp, bog, string\_bog, wet\_meadow, marsh                                                                                           | polygon  | 11+  |
|                  | grave\_yard                                                                                                                          | amenity=grave\_yard                                                                                                                           | polygon  | 11+  |
|                  | golf\_course, park, garden, playground, miniature\_golf                                                                              | leisure= golf\_course, park, garden, playground, miniature\_golf                                                                              | polygon  | 11+  |
| built-up areas   | residential, industrial, commercial, retail, railway, landfill, quarry                                                               | landuse= residential, industrial, commercial, retail, railway, landfill, quarry                                                               | polygon  | 11+  |
| other land areas | brownfield, greenfield, farmyard, farmland                                                                                           | landuse= brownfield, greenfield, farmyard, farmland                                                                                           | polygon  | 11+  |

## Layer "sites"

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

## Layer "buildings"

Has polygons for everything with a building tag (not building=no) from
zoom 14 on.

## Layer "addresses"

Has points for everything with an address from zoom 14+. Columns "name"
for addr:housename, "number" for addr:housenumber.

# Streets and Transport

## Layer "streets"

### Streets and Street Names

|                 | class     | attributes                         | geometry | zoom |
| --------------- | :-------- | :--------------------------------- | :------- | :--- |
| motorway        | motorway  | name                               | line     | 5+   |
|                 |           | link=true, null                    |          |      |
|                 |           | tunnel, bridge = true, false, null |          |      |
| trunk roads     | trunk     | name                               | line     | 5+   |
|                 |           | link=true, null                    |          |      |
|                 |           | tunnel, bridge = true, false, null |          |      |
| primary roads   | primary   | name                               | line     | 6+   |
|                 |           | link=true, null                    |          |      |
|                 |           | tunnel, bridge = true, false, null |          |      |
| secondary roads | secondary | name                               | line     | 9+   |
|                 |           | link=true, null                    |          |      |
|                 |           | tunnel, bridge = true, false, null |          |      |

|                                     |                |                                    |      |     |
| :---------------------------------- | :------------- | :--------------------------------- | :--- | :-- |
| tertiary roads                      | tertiary       | name                               | line | 11+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| side roads                          | unclassified   | name                               | line | 11+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| residential roads                   | residential    | name                               | line | 11+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| residential roads w/traffic calming | living\_street | name                               | line | 12+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| service roads                       | service        | name                               | line | 12+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| pedestrian roads                    | pedestrian     | name                               | line | 12+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| tracks                              | track          | name                               | line | 12+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| footpaths                           | footway        | name                               | line | 13+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| steps                               | steps          | name                               | line | 13+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| unspecified paths                   | path           | name                               | line | 13+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |
| bicycle paths                       | cycleway       | name                               | line | 13+ |
|                                     |                | link = true, null                  |      |     |
|                                     |                | tunnel, bridge = true, false, null |      |     |
|                                     |                | surface = paved, unpaved           |      |     |

### Paths on Airports

|         | class   | attributes                         | geometry | zoom |
| ------- | :------ | :--------------------------------- | :------- | :--- |
| runway  | runway  | name                               | line     | 11+  |
|         |         | link=true, null                    |          |      |
|         |         | tunnel, bridge = true, false, null |          |      |
| taxiway | taxiway | name                               | line     | 11+  |
|         |         | link=true, null                    |          |      |
|         |         | tunnel, bridge = true, false, null |          |      |

### Railway Tracks

|                      | class         | attributes                         | geometry | zoom |
| -------------------- | :------------ | :--------------------------------- | :------- | :--- |
| railway              | rail          | tunnel, bridge = true, false, null | line     | 5+   |
|                      |               | service                            |          |      |
| narrow gauge railway | narrow\_gauge | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |
| tram                 | tram          | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |
| light railway        | light\_rail   | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |
| funicular            | funicular     | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |
| subway               | subway        | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |
| monorail             | monorail      | tunnel, bridge = true, false, null | line     | 10+  |
|                      |               | service                            |          |      |

## streets\_med

Subset of streets layer only used up to z13.

## streets\_low

Subset of streets layer only used up to z9.

## Layer "street\_labels"

## streets\_labels\_points

### Shields

t.b.d.

### Junctions

|               | kind               | OSM                | label | geometry | zoom |
| ------------- | :----------------- | :----------------- | :---- | :------- | :--- |
| motorway exit | motorway\_junction | highway=           | name, | point    | 15+  |
|               |                    | motorway\_junction | ref   |          |      |

## Layer "aerialways"

|                 | kind        | OSM                    | label | geometry | zoom |
| --------------- | :---------- | :--------------------- | :---- | :------- | :--- |
| cable car       | cable\_car  | aerialways=cable\_car  |       | line     | 12+  |
| gondola         | gondola     | aerialways=gondola     |       | line     | 12+  |
| goods cable car | goods       | aerialways=goods       |       | line     | 12+  |
| chair lift      | chair\_lift | aerialways=chair\_lift |       | line     | 12+  |
| drag lift       | drag\_lift  | aerialways=drag\_lift  |       | line     | 12+  |
| t-bar lift      | t-bar       | aerialways=t-bar       |       | line     | 12+  |
| j-bar lift      | j-bar       | aerialways=j-bar       |       | line     | 12+  |
| platter lift    | platter     | aerialways=platter     |       | line     | 12+  |
| rope-tow lift   | rope-tow    | aerialways=rope\_tow   |       | line     | 12+  |

## Layer "public\_transport"

|                    | kind      | OSM               | label | geometry | zoom |
| ------------------ | :-------- | :---------------- | :---- | :------- | :--- |
| station            | station   | railway=station   | name  | point    | 11+  |
| halt               | halt      | railway=halt      | name  | point    | 11+  |
| airport, aerodrome | aerodrome | aeroway=aerodrome | name  | point    | 11+  |
