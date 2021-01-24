from typing import Optional, List 
from pydantic import BaseModel, constr, validator
from enum import Enum 
from datetime import datetime 
import re 
from uuid import UUID

# Define the Enum validator for the Genre field 
class GenreEnum(str, Enum):
    hiphop = "hip-hop"
    afropop = "afro-pop"
    rock = "rock"
    blues = "blues"
    others = "others"

# Define the Pydantic model
# This inherits from the pydantic BaseModel class
class SongSchema(BaseModel):
    music_id : UUID
    song_title : Optional[constr(max_length = 100)]
    description : Optional[constr(max_length = 300)]
    genre : GenreEnum 
    artiste_name : str = None 
    release_year : int 
    video : bool = False
    created_at : datetime = datetime.now()

    @validator('release_year')
    def release_date(cls, v):
        if not re.match(re.compile(r"\d{4}$"), str(v)):
            raise ValueError('This is not a valid date.')
        if v > datetime.now().year:
            raise ValueError('Date must not be greater than the current year.')
        return v
    class Config:
        orm_mode = True
