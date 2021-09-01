import time
# from datetime import datetime, timedelta
# import pytz
# import asyncio

from pymongo.errors import DuplicateKeyError
from .setup_db import collection_orders


class Order:
    """
    Order class
    """
    def __init__(self, user_id):
        self.user_id = user_id

    async def add_order(self, order: dict):
        order_ = {
            'owner_id': self.user_id,  # telegram id,
            'date_registered': int(time.time()),
            'date_last_active': int(time.time()),
            'status': 0,  # started 0 , active 1, finished 2
            'gender':order.get("gender"),
            'age': await self.__to_int(order.get("age")),
            'body': order.get("body"),
            'budget' : await self.__to_int(order.get("budget")),
            'date_time': order.get("date_time"),
            'address': order.get("address"),
            'preferences': order.get("preferences"),
            'contact': order.get("contact"),

        }
        try:
            collection_orders.insert_one(order_)
            return True
        except DuplicateKeyError:
            print(f"Duplicate Error: {self.user_id}")
            return False

    async def get_info(self):
        return collection_orders.find_one({'_id': self.user_id})

    async def update_last_active(self):
        collection_orders.update_one(
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
        collection_orders.update_one(
            {
                '_id': self.user_id
            },
            {
                '$set': {
                    field: value
                }
            }
        )

    async def __to_int(self, str:str):
        try:
            string = int(str)
        except Exception:
            string = str
            print(Exception)
        return string
