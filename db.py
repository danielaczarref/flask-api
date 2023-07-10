from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="dev",
    host="localhost",
    database="bhub",
    port=5432,
    password='startrek'
)

engine  = create_engine(url)
Base    = declarative_base()

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

