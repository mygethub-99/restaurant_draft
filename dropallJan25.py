
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#changed the name of database builder and added user
from database_mapping import Base, Restaurant, MenuItem, User, Cuisine


import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine.base').setLevel(logging.DEBUG)
echo = True



engine = create_engine('sqlite:///restaurantmapped.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



 

Base.metadata.drop_all(engine)
session.commit()
