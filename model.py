# ------------------------------------------------------------------
#	model.py
#
#					May/02/2022
# ------------------------------------------------------------------
from pydantic import BaseModel

# ------------------------------------------------------------------
class City(BaseModel):
	id: str
	name: str
	population: int
	date_mod: str
# ------------------------------------------------------------------
