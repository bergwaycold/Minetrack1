from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from ..database import Base


class Stockpile(Base):
    __tablename__ = "stockpiles"

    id = Column(Integer, primary_key=True, index=True)

    stockpile_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name = Column(String(200), nullable=False)

    material_type = Column(String(100))

    capacity_tonnes = Column(Float)

    current_tonnes = Column(
        Float,
        default=0,
    )

    latitude = Column(Float)
    longitude = Column(Float)

    geometry = Column(String)

    surface_model = Column(String)

    status = Column(
        String(50),
        default="active",
    )

    description = Column(String(500))


class StockpileDeposition(Base):
    __tablename__ = "stockpile_depositions"

    id = Column(Integer, primary_key=True, index=True)

    deposition_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    movement_id = Column(
        Integer,
        ForeignKey("movements.id"),
        nullable=False,
    )

    stockpile_id = Column(
        Integer,
        ForeignKey("stockpiles.id"),
        nullable=False,
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    tonnes = Column(Float, nullable=False)

    # 3D deposition position
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

    # Material grade at deposition
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    material_id = Column(
        Integer,
        ForeignKey("materials.id"),
    )

    material_type = Column(String(100))

    source_id = Column(String(100))

    layer_id = Column(String(100))

    notes = Column(String(500))


class StockpileReclaim(Base):
    __tablename__ = "stockpile_reclaims"

    id = Column(Integer, primary_key=True, index=True)

    reclaim_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    stockpile_id = Column(
        Integer,
        ForeignKey("stockpiles.id"),
        nullable=False,
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    tonnes = Column(Float, nullable=False)

    # 3D reclaim position
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

    destination_type = Column(String(100))
    destination_id = Column(String(100))

    # Reclaimed grade
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    material_id = Column(
        Integer,
        ForeignKey("materials.id"),
    )

    notes = Column(String(500))
