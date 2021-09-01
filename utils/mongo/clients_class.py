import time
# from datetime import datetime, timedelta
# import pytz
# import asyncio

from pymongo.errors import DuplicateKeyError
from .setup_db import collection_clients


class Client:
    """
    Clients class
    """

    def __init__(self, user_id):
        self.user_id = user_id

    async def add_user(self, user: dict, message :str):
        user_to_add = {
            '_id': self.user_id,  # telegram id,
            'first_name': user.get('first_name'),
            'last_name': user.get('last_name'),
            'username': user.get('username'),
            'priority': False,
            # 'preferences':{
            #     "hair_colour":"any",
            #     "height":"any",
            #     "gender":"any",
            #     "bust": -1, #any
            #     "figure": "any" #slim, medium, chubby
            #     'budget_per_day_usd': "1000",
            # },
            'date_registered': int(time.time()),
            'date_last_active': int(time.time()),
            'status': "started",  # started, registered, banned
            'add_last_sent': None,
            'activity': [
                {
                    'text': message,
                    'timestamp': int(time.time()),
                },
            ],
            "orders":{

            }
        }
        try:
            collection_clients.insert_one(user_to_add)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {self.user_id}")
            return False

    async def get_info(self):
        return collection_clients.find_one({'_id': self.user_id})

    async def update_last_active(self):
        collection_clients.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    "date_last_active": int(time.time())
                }
            }
        )
        print("update successful for", self.user_id)

    async def update_activity_list(self, message: str):
        pass

    async def update_field(self, field, value):
        collection_clients.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    field: value
                }
            }
        )
