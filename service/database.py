"""Database tables and utilities for managing the viewer queues."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

db = SQLAlchemy()


def queue_exists(queue_id):
  """Returns true if the queue ID belongs to a valid queue."""
  return True


def get_next_n(queue_id, count):
  """Gets the next $(count) users in the queue.

  Args:
    queue_id: the queue to scan
    count: the max number of users to show next (may be truncated)

  Returns:
    List[str] users next in the queue
  """
  return []


def get_user_at_position(queue_id, position):
  """Returns the username at the indicated position of the queue.

  Returns empty string if the queue does not exist or if the position is invalid.
  """
  if not queue_id or position < 1:
    return ""
  position_data = QueuePositionsTable.get(queue_id, position)
  if not position_data:
    return ""
  return position_data.username


class QueuesTable(db.Model):
  """Table schema for queues and queue metadata."""
  __tablename__ = "queues"

  id = db.Column(UUIDType(binary=True, native=False),
                 nullable=False,
                 primary_key=True)

  channel_id = db.Column(db.String(26), index=True)

  last_edited = 0  # datetime.now()

  current_position = 1  # int, FK into queue_positions

  is_open = False  # starts false, becomes True when joins are enabled

  title = "TITLE"  # used to describe the queue in JOIN and LEAVE messages

  info_message = "[INFO MESSAGE]"  # string used for !qinfo response.
  
  # queue_token


class QueuePositionsTable(db.Model):
  """User positions in each of the queues, including message and tombstones."""
  __tablename__ = "queue_positions"

  queue_id = 0  # part of primary key
  position = 1  # part of primary key

  timestamp = 0
  username = ""

  is_active = True  # will be set to False if someone leaves
  message = ""

