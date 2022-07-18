

import pymongo
client = pymongo.MongoClient("mongodb+srv://kishor_ineuron:mongodb123@cluster0.yk4yr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "kishor123",
    "email" : "imkishorcs@gmail123.com",
    "surname" : "sahu333"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
