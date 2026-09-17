# MineTrack Architecture

MineTrack is a mining fleet, material movement, stockpile intelligence,
material genealogy, blending and reconciliation platform.

## Core principle

Every tonne of material must remain traceable from:

Pit → Bench → Blast → Dig Block → Loader → Truck → Dump → Stockpile → Reclaim → Plant

## Core systems

- Fleet Management
- Material Movement
- Material Genealogy
- Grade Control
- ROM Management
- 3D Stockpile Intelligence
- Blending
- Reconciliation
- Maintenance
- Field Operations
- Analytics
- AI and Optimization

## Architecture

The system is divided into:

### Frontend

Web and mobile interfaces for:

- Fleet monitoring
- Mine map
- ROM management
- Stockpile visualization
- Material genealogy
- Grade control
- Blending
- Reconciliation
- Maintenance

### Backend

The backend provides:

- REST APIs
- Business logic
- Material genealogy
- Fleet calculations
- Stockpile calculations
- Blending
- Reconciliation
- Authentication
- Data synchronization

### Database

PostgreSQL with PostGIS will store:

- Mine geometry
- Equipment
- Material movements
- Stockpiles
- Spatial material data
- Grade information
- Production events
- Maintenance events

## Event-based architecture

Operational events are the source of truth.

Examples:

- Loading event
- Truck dispatch event
- Haul event
- Dump event
- Stockpile deposition event
- Stockpile reclaim event
- Plant feed event
- Assay event
- XRF event
- Survey event
- Maintenance event
