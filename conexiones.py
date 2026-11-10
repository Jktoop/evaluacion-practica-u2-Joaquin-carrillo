from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///registros.db", echo=False)
session = sessionmaker(bind=engine,expire_on_commit=False)
