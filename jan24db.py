from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=True)
    phone = Column(String(250), nullable=True)
    cuisine_id = Column(Integer, nullable=True)
    cuisine_cat = Column(String(250), nullable=True)
    health_rating = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'address': self.address,
            'phone' : self.phone,
            'cuisine_id' : self.cuisine_id,
            'health_rating' : self.health_rating,
            'cuisine_cat' : self.cuisine_cat,
            'id': self.id,
        }

#Added class Cuisine to allow for queries on type of cuisine served by a restaurant during template rendering.

class Cuisine(Base):
    __tablename__ = 'cuisine'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=True)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmapped.db')


Base.metadata.create_all(engine)
