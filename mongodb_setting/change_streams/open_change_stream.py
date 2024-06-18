import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('mongodb://mongo1')
db = client.get_database(name='shopify')
with db.items.watch() as stream:
    print('\nA change stream is open on the shopify.items namespace.  Currently watching ...\n\n')
    for change in stream:
        print(dumps(change, indent = 2))