from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from ..database import Base


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)

    movement_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Material origin
    source_type = Column(String(100))
    source_id = Column(String(100))

    dig_block_id = Column(
        Integer,
        ForeignKey("dig_blocks.id"),
    )

    material_id = Column(
        Integer,
        ForeignKey("materials.id"),
    )

    # Equipment
    loader_id = Column(
        Integer,
        ForeignKey("equipment.id"),
    )

    truck_id = Column(
        Integer,
        ForeignKey("equipment.id"),
    )

    # Destination
    destination_type = Column(String(100))
    destination_id = Column(String(100))

    # Production
    tonnes = Column(Float, nullable=False)

    material_type = Column(String(100))

    # Grade at time of movement
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    moisture = Column(Float)

    # GPS
    origin_latitude = Column(Float)
    origin_longitude = Column(Float)

    destination_latitude = Column(Float)
    destination_longitude = Column(Float)

    # Haul performance
    cycle_time_seconds = Column(Float)
    travel_distance_km = Column(Float)
    fuel_litres = Column(Float)

    operator_id = Column(String(100))

    # Evidence
    xrf_measurement_id = Column(String(100))
    assay_id = Column(String(100))
    photo_reference = Column(String(500))

    status = Column(
        String(50),
        default="completed",
    )

    notes = Column(String(1000))
