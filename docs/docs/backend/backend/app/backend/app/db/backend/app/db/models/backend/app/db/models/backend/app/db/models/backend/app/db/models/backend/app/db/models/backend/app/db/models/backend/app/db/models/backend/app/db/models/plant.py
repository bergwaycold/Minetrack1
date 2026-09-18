from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from ..database import Base


class PlantFeed(Base):
    __tablename__ = "plant_feed"

    id = Column(Integer, primary_key=True, index=True)

    plant_feed_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    reclaim_id = Column(
        Integer,
        ForeignKey("stockpile_reclaims.id"),
        nullable=False,
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    tonnes = Column(Float, nullable=False)

    # Feed grade
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    moisture = Column(Float)

    plant_destination = Column(String(200))

    feed_type = Column(String(100))

    recovery_ni = Column(Float)
    recovery_fe = Column(Float)
    recovery_co = Column(Float)
    recovery_sc = Column(Float)

    status = Column(
        String(50),
        default="processed",
    )

    notes = Column(String(1000))
