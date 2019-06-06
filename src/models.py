from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Email = Column(String(100))
    Password = Column(String(50))

class Denounce(Base):
    __tablename__ = 'denounce'
    id = Column(Integer, primary_key=True)
    Id_user = Column(Integer)
    Description = Column(String(300))
    Bus_number = Column(Integer)
    Lat = Column(Integer)
    Lon = Column(Integer)

if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DATABASE_PATH + DATABASE_NAME)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)