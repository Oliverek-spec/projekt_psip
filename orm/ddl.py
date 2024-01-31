import sqlalchemy 
import sqlalchemy.orm as orm
from geoalchemy2 import Geometry

db_params = sqlalchemy.URL.create(
    drivername = "postgresql",
    username = 'postgres',
    password = '15082000',
    host = 'localhost',
    database = 'postgres',
    port = 5433 
)
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
connection.commit()

Base = orm.declarative_base()

class Bus(Base):
    __tablename__ = "buses"
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    registration = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    line = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location =sqlalchemy.Column(Geometry('POINT'), nullable=True)

class Driver(Base):
    __tablename__ = "bus_drivers"
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    bus = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    line = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location =sqlalchemy.Column(Geometry('POINT'), nullable=True)

class Passenger(Base):
    __tablename__ = "passengers"
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    bus = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location =sqlalchemy.Column(Geometry('POINT'), nullable=True)
    
inspector = sqlalchemy.inspect(engine)
if Bus.__tablename__ not in inspector.get_table_names():
    Base.metadata.create_all(engine)
if Driver.__tablename__ not in inspector.get_table_names():
    Base.metadata.create_all(engine)
if Passenger.__tablename__ not in inspector.get_table_names():
    Base.metadata.create_all(engine)


