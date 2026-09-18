from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from ..database import Base


class Assay(Base):
    __tablename__ = "assays"

    id = Column(Integer, primary_key=True, index=True)

    assay_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    sample_id = Column(
        String(100),
        nullable=False,
        index=True,
    )

    source_type = Column(String(100))
    source_id = Column(String(100))

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Laboratory analytical results
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    laboratory = Column(String(200))
    analytical_method = Column(String(200))

    sample_type = Column(String(100))

    quality_status = Column(
        String(50),
        default="pending",
    )

    certificate_reference = Column(String(200))

    notes = Column(String(1000))


class XRFMeasurement(Base):
    __tablename__ = "xrf_measurements"

    id = Column(Integer, primary_key=True, index=True)

    xrf_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    sample_id = Column(
        String(100),
        nullable=False,
        index=True,
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    latitude = Column(Float)
    longitude = Column(Float)

    # Field XRF results
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    instrument = Column(String(200))
    operator_id = Column(String(100))

    calibration_reference = Column(String(200))

    quality_status = Column(
        String(50),
        default="field",
    )

    notes = Column(String(1000))
