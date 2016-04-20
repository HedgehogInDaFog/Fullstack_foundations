from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Add new entry:
myFirstRestaurant = Restaurant(name='Pizza Palace')
session.add(myFirstRestaurant)
session.commit()

#read:
session.query(Restaurant).all()
vb = session.query(MenuItem).filter_by(name='Veggie Burger').one()
print vb.id, vb.price

#update
vb.price = 3
session.add(vb)
session.commit()

#delete
session.delete(vb)
session.commit()


