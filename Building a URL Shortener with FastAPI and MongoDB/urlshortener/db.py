from mongoengine import connect 
from decouple import config 

MONGO_URI = config('MONGO_URI')

# Connect to the Mongo Atlas using the connection URI
connect(MONGO_URI)