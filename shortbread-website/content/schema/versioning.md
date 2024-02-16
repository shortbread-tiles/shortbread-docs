+++
draft= false
title = "Schema Versioning Policy"
linkTitle = "Versioning"
description = "This page describes the versioning policy of the Shortbread schema"
+++

The shortbread schema will have to change over time to keep up with changes to OpenStreetMap data, but also because we improve the tools for generating and using the vector tiles and as we gain a better understanding on how to style vector tiles in better ways. On the other hand we need some stability in this standard for users to rely on.

New versions of this schema will come out from time to time, there is no fixed schedule.

## Version numbers

Version numbers are of the form MAJOR.MINOR, where MAJOR and MINOR are positive integers. A style written for version X.Y of the schema should work on any tilesets with the same MAJOR version and an equal or greater MINOR version.

Within the same MAJOR.MINOR version the only allowed changes are editorial or formatting changes that would not change if a tileset follows the schema. In cases where the specification is ambigous or could reasonably be interpreted in multiple ways notes may be added indicating the preferred interpretation. Information about future changes may be added such as depreciation notices.

## Minor version

A new minor version must be usable by any styles written to the previous minor version. This means the only changes that can be added are forwards-compatible. This includes

- adding a new layer;
- adding new fields to an existing layer;
- adding a new `kind` to a table if the new `kind` doesn't change the overall meaning of the layer;
- changing the zoom level, size of areas, population, or other thresholds used to determine if a feature is included;
- rewording parts of the specification which could be reasonably interpreted in multiple ways to pick one of the ways; and
- removal of fields where other changes mean that the field is never set.

Minor revisions must not

- remove or rename layers or fields;
- change the geometry type(s) allowed for existing layers.

We reserve the right to make changes that we would normally not do, if actual tagging in OpenStreetMap changes in a way that it doesn't make sense any more.

It is possible that a style written for a specific implementation of the schema may stop working with minor changes if the implementation relied on behavior that was not fully defined. To avoid this, implementers should raise issues about any ambiguities so their implementation is more likely to be compatible with the next minor revision.

For tile set publishers it should usually be okay to update their tool chain to use the newest minor version without breaking their users styles, but it is, of course, up to them how to handle the upgrade process.

## Major version

Major revisions may change any element of the specification, including removing layers. A new major revision should have at least one change not allowed in a minor revision, so some styles will require changes.

Tile set publishers probably want to think about supporting multiple major versions at the same time to allow style writers and users to move to the new version, but it is, of course, up to them how to handle the upgrade process. We are concious of the fact that upgrading to a new major schema version incurs a cost from all users and will not have new major versions too often.
