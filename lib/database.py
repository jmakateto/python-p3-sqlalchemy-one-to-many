from sqlalchemy import create_engine
from models import Base

def init_db():
    engine = create_engine('sqlite:///one_to_many.db')
    Base.metadata.create_all(engine)
