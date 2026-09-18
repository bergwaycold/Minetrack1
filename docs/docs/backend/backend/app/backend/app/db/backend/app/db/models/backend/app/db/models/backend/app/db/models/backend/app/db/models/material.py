from sqlalchemy import Column, Integer, String, Float

from ..database import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)

    material_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    material_type = Column(
        String(100),
        nullable=False,
    )

    description = Column(String(500))

    # Primary MineTrack grade attributes
    ni = Column(Float)
    fe = Column(Float)
    co = Column(Float)
    sc = Column(Float)

    # Additional material properties
    moisture = Column(Float)
    density = Column(Float)

    estimated_tonnes = Column(Float)

    source_type = Column(String(100))
    source_id = Column(String(100))

    grade_source = Column(String(100))
    grade_confidence = Column(Float)

    status = Column(
        String(50),
        default="active",
    )
