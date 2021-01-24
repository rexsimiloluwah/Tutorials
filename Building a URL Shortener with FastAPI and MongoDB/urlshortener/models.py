from mongoengine import Document, StringField, IntField, DateTimeField, ObjectIdField
from bson import ObjectId 
from datetime import datetime 

class Url(Document):
    id = ObjectId()
    longUrl = StringField(required = True)
    shortCode = StringField(required = True, unique = True)
    shortUrl = StringField(required = True)
    visitorCount = IntField(default = 0)
    createdAt = DateTimeField(default = datetime.now())


    
