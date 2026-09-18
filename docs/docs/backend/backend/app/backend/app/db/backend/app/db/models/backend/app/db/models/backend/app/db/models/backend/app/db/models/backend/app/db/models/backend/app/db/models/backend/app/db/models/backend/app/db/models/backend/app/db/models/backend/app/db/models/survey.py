from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from ..database import Base


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)

    survey_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    stockpile_id = Column(
        Integer,
        ForeignKey("stockpiles.id"),
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    survey_method = Column(String(100))

    survey_reference = Column(String(500))

    surface_model = Column(String(500))

    volume_m3 = Column(Float)

    calculated_tonnage = Column(Float)

    density = Column(Float)

    surveyor = Column(String(200))

    accuracy_m = Column(Float)

    status = Column(
        String(50),
        default="completed",
    )

    notes = Column(String(1000))
