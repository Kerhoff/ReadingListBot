# import pytest
# from bot.db import ReadingItem, get_engine, create_session, add_item, get_items, mark_item_completed, delete_item, clear_list
#
# # Setup the test database session
# @pytest.fixture(scope='function')
# def session():
#     engine = get_engine(testing=True)  # Use in-memory database
#     session = create_session(engine)
#     yield session
#     session.close()
#
#
# def test_add_item(session):
#     # Add a new item
#     add_item(user_id=1, title="Test Article", link="https://example.com", item_type="article")
#
#     # Verify the item was added
#     items = get_items(user_id=1)
#     assert len(items) == 1
#     assert items[0].title == "Test Article"
#     assert items[0].link == "https://example.com"
#     assert items[0].item_type == "article"
#     assert items[0].completed is False
#
#
# def test_mark_item_completed(session):
#     # Add an item and mark it as read
#     add_item(user_id=1, title="Test Video", link="https://example.com/video", item_type="video")
#     items = get_items(user_id=1)
#
#     # Mark the first item as read
#     mark_item_completed(user_id=1, title=items[0].title)
#
#     # Verify the item is marked as read
#     items = get_items(user_id=1)
#     assert items[0].completed is True
#
#
# def test_delete_item(session):
#     # Add an item and then delete it
#     add_item(user_id=1, title="Test Podcast", link="https://example.com/podcast", item_type="podcast")
#     items = get_items(user_id=1)
#
#     # Delete the item
#     delete_item(user_id=1, title="Test Podcast")
#
#     # Verify the item was deleted
#     items = get_items(user_id=1)
#     for item in items:
#         assert item.title != "Test Podcast"
#
#
# def test_clear_list(session):
#     # Add an items and then clear the list
#     add_item(user_id=1, title="Test Article", link="https://example.com", item_type="article")
#     add_item(user_id=1, title="Test Podcast", link="https://example.com/podcast", item_type="podcast")
#     add_item(user_id=1, title="Test Video", link="https://example.com/video", item_type="video")
#     items = get_items(user_id=1)
#
#     # Clear the list
#     clear_list(user_id=1)
#
#     # Verify the item was deleted
#     items = get_items(user_id=1)
#     assert len(items) == 0
