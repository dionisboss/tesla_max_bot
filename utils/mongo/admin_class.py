import time
from datetime import datetime, timedelta
import pytz
import asyncio

from pymongo.errors import DuplicateKeyError
from setup_db import collection_users, collection_admins, collection_door


class User:
    """
    User class
    """

    def __init__(self, user_id):
        self.user_id = user_id

    def add_user(self, user: dict, message: str):
        user_to_add = {
            '_id': self.user_id,  # telegram id,
            'first_name': user.get('first_name'),
            'last_name': user.get('last_name'),
            'username': user.get('username'),
            'phone_number': user.get('phone_number'),
            'date_registered': int(time.time()),
            'date_last_active': int(time.time()),
            'status': "start",  # started, registered, banned
            'add_last_sent': None,
            'activity': [
                {
                    'text': message,
                    'timestamp': int(time.time()),
                },
            ],
        }
        try:
            collection_users.insert_one(user_to_add)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {self.user_id}")
            return False

    def get_info(self):
        return collection_users.find_one({'_id': self.user_id})
