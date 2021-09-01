from pymongo import MongoClient
from .cred import username, password, client_str
# username = input()
# password = input()

client = MongoClient(client_str)
# setup db
db_name = 'employment_bot'
db = client[db_name]
# setup user collection
col_clients_name = 'clients'
collection_clients = db[col_clients_name]

# setup admin collection
col_admins_name = "admins"
collection_admins = db[col_admins_name]

# setup exhibit collection
collection_orders_name = 'orders'
collection_orders = db[collection_orders_name]

