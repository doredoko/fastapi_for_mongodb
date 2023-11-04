# ------------------------------------------------------------------
#	main.py
#
#						May/02/2022
# ------------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
	fetch_one_city,
	fetch_all_cities,
	create_city,
	update_city,
	remove_city,
)

from model import City

# ------------------------------------------------------------------
app = FastAPI()

#origins = [
#	'http://localhost:3000',
# 	'http://localhost:8000',
# 	'http://localhost:27017',
#	'http://localhost',
#	]

#app.add_middleware(
#	CORSMiddleware,
#	allow_origins=origins,
#	allow_credentials=True,
#	allow_methods=["*"],
#	allow_headers=["*"],
#)

# ------------------------------------------------------------------
@app.get("/")
def read_root():
	return {"Saluton"}

# ------------------------------------------------------------------
@app.get("/api/city")
async def get_cities():
	response = await fetch_all_cities()
	return response

# ------------------------------------------------------------------
@app.get("/api/city/{id}", response_model=City)
async def get_city_by_id(id):
	response = await fetch_one_city(id)
	if response:
		return response
	raise HTTPException(404, f"there is no City item with this id {id}")

# ------------------------------------------------------------------
@app.post("/api/city", response_model=City)
async def post_city(city:City):
	response = await create_city(city.dict())
	if response:
		return response
	raise HTTPException(400, "Sometheng went wrong / Bad Request")

# ------------------------------------------------------------------
@app.put("/api/city/{id}/", response_model=City)
async def put_city(id:str, population:int):
	response = await update_city(id, population)
	if response:
		return response
	raise HTTPException(404, f"there is no City item with this id {id}")

# ------------------------------------------------------------------
@app.delete("/api/city/{id}")
async def delete_city(id):
	response = await remove_city(id)
	if response:
		return "Successfully deleted city item!"
	raise HTTPException(404, f"there is no city item with this id {id}")

# ------------------------------------------------------------------
