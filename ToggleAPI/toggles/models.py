from sqlalchemy import Column,String,Integer
from .database import Base

class Toggle(Base):
    __tablename__="toggles"
    id=Column(Integer,primary_key=True,index=True)
    toggle_id=Column(Integer)
    description=Column(String(255))
    environment_level=Column(String(100))
    status=Column(String(15))
    created_by=Column(String(100))
    created_at=Column(String(20))
    last_modified_at=Column(String(20))
    notes = Column(String(255))