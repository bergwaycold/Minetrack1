# MineTrack Data Model

## Purpose

The MineTrack data model is designed around material genealogy and
event-based accounting.

Every material movement must be traceable from its source to its
destination.

## Core hierarchy

Mine
→ Pit
→ Bench
→ Blast
→ Dig Block
→ Loading Event
→ Truck Movement
→ Dump Event
→ Stockpile Deposition
→ Stockpile Reclaim
→ Plant Feed

## Core entities

### Mine

Represents an operating mine.

Fields:

- mine_id
- name
- location
- coordinate_reference_system

### Pit

Represents a mining pit.

Fields:

- pit_id
- mine_id
- name
- geometry

### Bench

Represents a mining bench.

Fields:

- bench_id
- pit_id
- elevation
- geometry

### Blast

Represents a blast.

Fields:

- blast_id
- bench_id
- blast_name
- date
- geometry

### Dig Block

Represents the smallest operational mining unit.

Fields:

- dig_block_id
- blast_id
- bench_id
- material_type
- geometry
- estimated_tonnes
- estimated_Ni
- estimated_Fe
- estimated_Co
- estimated_Sc

### Equipment

Equipment includes:

- trucks
- loaders
- excavators
- dozers
- graders
- drills
- crushers
- support equipment

Fields:

- equipment_id
- equipment_type
- fleet_number
- manufacturer
- model
- status

### Material

Represents a material identity.

Fields:

- material_id
- material_type
- source_dig_block
- Ni
- Fe
- Co
- Sc
- moisture
- density

Nickel, iron, cobalt and scandium are first-class grade attributes.

Copper is not part of the MineTrack core grade model.

## Movement Event

The movement event is the central operational record.

Fields:

- movement_id
- timestamp
- source
- destination
- material_id
- dig_block_id
- loader_id
- truck_id
- tonnes
- material_type
- Ni
- Fe
- Co
- Sc
- moisture
- origin_latitude
- origin_longitude
- destination_latitude
- destination_longitude
- cycle_time
- travel_distance
- fuel
- operator_id

## Stockpile

Represents a ROM or product stockpile.

Fields:

- stockpile_id
- name
- material_type
- capacity_tonnes
- current_tonnes
- geometry
- surface_model
- status

## Stockpile Deposition

Records where material was placed in a stockpile.

Fields:

- deposition_id
- movement_id
- stockpile_id
- timestamp
- tonnes
- x
- y
- z
- Ni
- Fe
- Co
- Sc
- material_id

This allows the stockpile to be modeled spatially rather than as
only a weighted-average grade.

## Stockpile Reclaim

Records material removed from a stockpile.

Fields:

- reclaim_id
- stockpile_id
- timestamp
- tonnes
- x
- y
- z
- destination
- Ni
- Fe
- Co
- Sc

## Plant Feed

Records material delivered to the processing plant.

Fields:

- plant_feed_id
- reclaim_id
- timestamp
- tonnes
- Ni
- Fe
- Co
- Sc
- plant_destination

## Assay

Stores laboratory or field analytical information.

Fields:

- assay_id
- sample_id
- source
- timestamp
- Ni
- Fe
- Co
- Sc
- laboratory
- method
- quality_status

## XRF Measurement

Stores field XRF observations.

Fields:

- xrf_id
- sample_id
- timestamp
- latitude
- longitude
- Ni
- Fe
- Co
- Sc
- instrument
- operator

## Survey

Stores stockpile or mine surveys.

Fields:

- survey_id
- stockpile_id
- timestamp
- survey_method
- surface_model
- volume
- calculated_tonnage

## Material Genealogy

Material genealogy links all events together.

Example:

Blast B001
→ Dig Block B001-03
→ Loader L02
→ Truck T17
→ Movement M000123
→ Stockpile SP04
→ Deposition D000456
→ Reclaim R000789
→ Plant Feed PF000321

The system must be able to follow this chain in both directions.

## Event Ledger

Operational events should be treated as immutable records.

Corrections should create a new corrective event rather than silently
changing historical operational data.

This preserves:

- auditability
- reconciliation
- material genealogy
- production history
- accountability

## Design principle

The database should support both:

1. Operational transactions
2. Spatial material intelligence

The result is a digital representation of material movement through
the entire mining operation.
