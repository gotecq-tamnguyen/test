from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    breed = Column(String(50))
    age = Column(Integer)

    def to_dict(self):
        return {"id": self.id, "name":self.name, "breed":self.breed, "age":self.age}
