import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Game, Review
from conftest import SQLITE_URL  

class TestGame:

    @classmethod
    def setup_class(cls):
        #  new SQLite database and session for the test class
        cls.engine = create_engine(SQLITE_URL)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        
        # Create tables
        Base.metadata.create_all(cls.engine)

    @classmethod
    def teardown_class(cls):
        # Close the session and dispose of the engine after all tests
        cls.session.close()
        cls.engine.dispose()

    def test_game_has_correct_attributes(self):
        # Your test code here

    def test_has_associated_reviews(self):
        # Your test code here
