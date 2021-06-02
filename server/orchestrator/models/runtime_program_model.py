from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base, registry
from dataclasses import dataclass
from sqlalchemy import MetaData

from .base import Base

@dataclass
class RuntimeProgram(Base):
    __tablename__ = 'runtime_program'

    id = Column(Integer, primary_key=True)
    program_id = Column(String(64))
    name = Column(String(64))
    description = Column(String(64))
    data = Column(LargeBinary)