from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Pit(Base):
    __tablename__ = "pits"

    id = Column(Integer, primary_key=True, index=True)

    pit_id = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    name = Column(String(200), nullable=False)

    mine_id = Column(
        Integer,
        ForeignKey("mines.id"),
        nullable=False,
    )

    elevation = Column(Float)

    geometry = Column(String)

    mine = relationship(
        "Mine",
        back_populates="pits",
    )

    benches = relationship(
        "Bench",
        back_populates="pit",
        cascade="all, delete-orphan",
    )


class Bench(Base):
    __tablename__ = "benches"

    id = Column(Integer, primary_key=True, index=True)

    bench_id = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    pit_id = Column(
        Integer,
        ForeignKey("pits.id"),
        nullable=False,
    )

    elevation = Column(Float)

    geometry = Column(String)

    pit = relationship(
        "Pit",
        back_populates="benches",
    )

    blasts = relationship(
        "Blast",
        back_populates="bench",
        cascade="all, delete-orphan",
    )


class Blast(Base):
    __tablename__ = "blasts"

    id = Column(Integer, primary_key=True, index=True)

    blast_id = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    bench_id = Column(
        Integer,
        ForeignKey("benches.id"),
        nullable=False,
    )

    blast_name = Column(String(200))

    blast_date = Column(String(50))

    geometry = Column(String)

    bench = relationship(
        "Bench",
        back_populates="blasts",
    )

    dig_blocks = relationship(
        "DigBlock",
        back_populates="blast",
        cascade="all, delete-orphan",
    )


class DigBlock(Base):
    __tablename__ = "dig_blocks"

    id = Column(Integer, primary_key=True, index=True)

    dig_block_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    blast_id = Column(
        Integer,
        ForeignKey("blasts.id"),
        nullable=False,
    )

    bench_id = Column(
        Integer,
        ForeignKey("benches.id"),
        nullable=False,
    )

    material_type = Column(String(100))

    geometry = Column(String)

    estimated_tonnes = Column(Float)

    estimated_ni = Column(Float)
    estimated_fe = Column(Float)
    estimated_co = Column(Float)
    estimated_sc = Column(Float)

    moisture = Column(Float)
    density = Column(Float)

    status = Column(
        String(50),
        default="available",
    )

    blast = relationship(
        "Blast",
        back_populates="dig_blocks",
    )
