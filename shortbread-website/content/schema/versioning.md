+++
draft= false
title = "Schema Versioning Policy"
linkTitle = "Versioning"
description = "This page describes the versioning policy of the Shortbread schema"
+++

## About

It is important that developers of tile generators, style authors, and schema editors have a consistent understanding on what schema version numbers mean.

## Version numbers

Version numbers are of the form MAJOR.MINOR, where MAJOR and MINOR are positive integers. A style written for version X.Y of the schema should work on any tilesets with the same MAJOR version and an equal or greater MINOR version.

Within the same MAJOR.MINOR version the only allowed changes are editorial or formatting changes that would not change if a tileset follows the schema. In cases where the specification is ambigous or could reasonably be interpreted in multiple ways notes may be added indicating the preferred interpretation. Information about future changes may be added such as depreciation notices.

## Minor version

A new minor version must be usable by any styles written to the previous minor version. This means the only changes that can be added are forwards-compatible. This includes

- adding a new layer;
- adding additional tags to an existing `kind` value in a layer;
- adding a new `kind` to a table;
- changing the zoom level, way area, population, or other thresholds used determine if a feature is included;
- if a particular tagging is no longer used in OpenStreetMap, removal of that tagging from features;
- adding new fields to an existing layer, except that a `kind` field may not be added to an existing layer that did not have it;
- rewording parts of the specification which could be reasonably interpreted in multiple ways to pick one of the ways; and
- removal of fields where other changes mean that the field is never set.

Minor revisions must not
- remove or rename layers;
- remove tagging from features unless that type of tagging no longer is in OpenStreetMap;
- remove types of objects unless that type of object is no longer mapped in OpenStreetMap; or
- add features of a different geometry type to an existing layer;

It is possible that a style written for a specific implementation of the schema may stop working with minor changes if the implementation relied on behavior that was not fully defined. To avoid this, implementers should raise issues about any ambiguities so their implementation is more likely to be compatible with the next minor revision.

## Major version

Major revisions may change any element of the specification, including removing layers. A new major revision should have at least one change not allowed in a minor revision, so some styles will require changes.