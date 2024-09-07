from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base for declarative class
Base = declarative_base()

# Define the ReadingItem model
class ReadingItem(Base):
    __tablename__ = 'reading_items'

    id = Column(Integer, primary_key=True) # Unique identifier for the item
    user_id = Column(Integer) # Unique identifier for the user
    title = Column(String) # Title of the item
    link = Column(String) # URL of the item
    item_type = Column(String) # Type of the item (e.g., book, article, video)
    completed = Column(Boolean, default=False)  # Whether the item has been read/watched/listened to

# Create a new SQLite database
# Use in memory database for testing
def get_engine(testing=False):
    if testing:
        return create_engine('sqlite:///:memory:') # In-memory SQLite database
    else:
        return create_engine('sqlite:///reading_list.db') # Production SQLite database

# Session factory
def create_session(engine):
    Base.metadata.create_all(engine) # Create all tables in the database
    Session = sessionmaker(bind=engine)
    return Session()

# Funcion to add a new item to the reading list
def add_item(user_id, title, link, item_type, session=None):
    if session is None:
        session = create_session(get_engine())
    new_item = ReadingItem(user_id=user_id, title=title, link=link, item_type=item_type)
    session.add(new_item)
    session.commit()

# Function to get all items in the reading list
def get_items(user_id, session=None):
    if session is None:
        session = create_session(get_engine())
    items = session.query(ReadingItem).filter_by(user_id=user_id).all()
    return items

# Function to mark an item as completed
def mark_item_completed(user_id, title, session=None):
    if session is None:
        session = create_session(get_engine())
    item = session.query(ReadingItem).filter_by(user_id=user_id, title=title).first()
    if item:
        item.completed = True
        session.commit()

# Function to remove an item from the reading list
def delete_item(user_id, title, session=None):
    if session is None:
        session = create_session(get_engine())
    item = session.query(ReadingItem).filter_by(user_id=user_id, title=title).first()
    if item:
        session.delete(item)
        session.commit()

# Function to clear all items from the reading list
def clear_list(user_id, session=None):
    if session is None:
        session = create_session(get_engine())
    items = session.query(ReadingItem).filter_by(user_id=user_id).all()
    for item in items:
        session.delete(item)
    session.commit()