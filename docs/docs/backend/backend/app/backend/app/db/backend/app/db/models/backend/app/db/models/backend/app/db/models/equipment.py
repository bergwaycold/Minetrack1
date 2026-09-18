from sqlalchemy import Column, Integer, String, Float

from ..database import Base


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)

    equipment_id = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    fleet_number = Column(String(50), index=True)

    equipment_type = Column(
        String(50),
        nullable=False,
    )

    manufacturer = Column(String(100))
    model = Column(String(100))

    capacity_tonnes = Column(Float)

    status = Column(
        String(50),
        default="available",
    )

    operator_id = Column(String(100))

    latitude = Column(Float)
    longitude = Column(Float)

    engine_hours = Column(Float, default=0)
    fuel_level_percent = Column(Float)

    description = Column(String(500))
