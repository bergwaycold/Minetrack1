from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database import Base


class Mine(Base):
    __tablename__ = "mines"

    id = Column(Integer, primary_key=True, index=True)

    mine_id = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)

    country = Column(String(100))
    province = Column(String(100))
    location = Column(String(200))

    latitude = Column(Float)
    longitude = Column(Float)

    status = Column(String(50), default="active")

    pits = relationship(
        "Pit",
        back_populates="mine",
        cascade="all, delete-orphan",
    )
