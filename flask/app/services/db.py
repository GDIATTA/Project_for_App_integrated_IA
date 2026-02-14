from pymongo import MongoClient

def get_db_connect():
    client = MongoClient(host="mongo1", port=27017)
    db = client.shopify
    return db.items