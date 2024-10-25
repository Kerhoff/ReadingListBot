from typing import List, Optional
from sqlalchemy import (
    DateTime,
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship,
)
from datetime import datetime

# Define the base for declarative class
Base = declarative_base()


# Define the ReadingItem model
class ReadingItem(Base):
    __tablename__ = "reading_items"

    id = Column(Integer, primary_key=True)  # Unique identifier for the item
    user_id = Column(
        Integer, ForeignKey("users.tg_user_id")
    )  # Unique identifier for the user
    title = Column(String)  # Title of the item
    link = Column(String)  # URL of the item
    item_type = Column(String)  # Type of the item (e.g., book, article, video)
    completed = Column(
        Boolean, default=False
    )  # Whether the item has been read/watched/listened to
    # created_at = Column(
    #     String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # )  # Date and time the item was added
    created_at = Column(DateTime, default=datetime.now())  # Date and time the item was added

    # Relationship between ReadingItem and User
    user = relationship("User", back_populates="reading_items")


class User(Base):
    __tablename__ = "users"

    tg_user_id = Column(Integer, primary_key=True)  # Telegram ID of the user
    tg_username = Column(String, unique=True)  # Telegram username of the user

    # Relationship between User and ReadingItem
    reading_items = relationship("ReadingItem", back_populates="user")


# Create a new SQLite database
# Use in memory database for testing
def get_engine(testing: bool = False):
    if testing:
        return create_engine("sqlite:///:memory:")  # In-memory SQLite database
    else:
        return create_engine("sqlite:///reading_list.db")  # Production SQLite database


# Session factory
def create_session(engine):
    Base.metadata.create_all(engine)  # Create all tables in the database
    Session = sessionmaker(bind=engine)
    return Session()


# Funcion to add a new item to the reading list
def add_user(tg_user_id: int, tg_username: str, session=None) -> User:
    if session is None:
        session = create_session(get_engine())
    new_user: User = User(tg_user_id=tg_user_id, tg_username=tg_username)
    session.add(new_user)
    session.commit()
    return new_user


# Function to get all items in the reading list
def get_user(tg_user_id: int, session=None) -> User | None:
    if session is None:
        session = create_session(get_engine())
    user: Optional[User] = session.query(User).filter_by(tg_user_id=tg_user_id).first()
    return user


# Funcion to add a new item to the reading list
def add_item(
    user: User,
    title: str,
    link: str,
    item_type: str,
    session=None,
) -> None:
    if session is None:
        session = create_session(get_engine())
    new_item: ReadingItem = ReadingItem(
        user_id=user.tg_user_id,
        title=title,
        link=link,
        item_type=item_type,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    session.add(new_item)
    session.commit()


# Function to get all items in the reading list
def get_items(user_id: int, session=None) -> List[ReadingItem]:
    if session is None:
        session = create_session(get_engine())
    items: List[ReadingItem] = (
        session.query(ReadingItem)
        .filter_by(user_id=user_id)
        .order_by(ReadingItem.created_at.asc())
        .all()
    )
    return items


# Function to mark an item as completed
def mark_item_completed(user_id: int, item_id: int, session=None) -> None:
    if session is None:
        session = create_session(get_engine())
    item: ReadingItem = (
        session.query(ReadingItem).filter_by(user_id=user_id, item_id=item_id).first()
    )
    if item:
        item.completed = True
        session.commit()


# Function to remove an item from the reading list
def delete_item(item_id: int, session=None) -> None:
    if session is None:
        session = create_session(get_engine())
    item: ReadingItem = session.query(ReadingItem).filter_by(id=item_id)
    if item:
        session.delete(item)
        session.commit()


# Function to clear all items from the reading list
def clear_list(user_id: int, session=None) -> None:
    if session is None:
        session = create_session(get_engine())
    items: List[ReadingItem] = (
        session.query(ReadingItem).filter_by(user_id=user_id).all()
    )
    for item in items:
        session.delete(item)
    session.commit()


# Function to filter items by title
def get_item_by_title(user_id: int, title: str, session=None) -> ReadingItem:
    if session is None:
        session = create_session(get_engine())
    item: ReadingItem = (
        session.query(ReadingItem).filter_by(user_id=user_id, title=title).first()
    )
    return item


# Function to filter items by type
def get_items_by_type(user_id: int, item_type: str, session=None) -> List[ReadingItem]:
    if session is None:
        session = create_session(get_engine())
    items: List[ReadingItem] = (
        session.query(ReadingItem).filter_by(user_id=user_id, item_type=item_type).all()
    )
    return items
