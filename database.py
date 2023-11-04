# ------------------------------------------------------------------
#	database.py
#
#					May/02/2022
# ------------------------------------------------------------------
from model import City

import sys
import	datetime
#
import motor.motor_asyncio
from pymongo import MongoClient
import pymongo

# ------------------------------------------------------------------
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/?retryWrites=true&w=majority')
database = client.city
collection = database.tochigi

# ------------------------------------------------------------------
async def fetch_one_city(id):
	document = await collection.find_one({"id":id})
	return document
#
# ------------------------------------------------------------------
async def fetch_all_cities():
	cities = []
	cursor = collection.find({})
	async for document in cursor:
		cities.append(City(**document))
	return cities
#
# ------------------------------------------------------------------
async def create_city(city):
	document = city
	result = await collection.insert_one(document)
	return document
#
# ------------------------------------------------------------------
async def update_city(id, population):
	sys.stderr.write("*** update_city ***\n")
	date_mod = datetime.date.today()
	await collection.update_one({"id":id}, {"$set": {
		'population': population,
		'date_mod': '%s' % date_mod
		}})
	document = await collection.find_one({"id": id})
	return document
#
# ------------------------------------------------------------------
async def remove_city(id):
	await collection.delete_one({"id":id})
	return True
#
# ------------------------------------------------------------------
