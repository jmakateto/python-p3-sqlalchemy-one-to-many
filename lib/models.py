from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    platform = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='game')

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game', back_populates='reviews')
