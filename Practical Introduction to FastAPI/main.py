from fastapi import FastAPI, HTTPException
import uvicorn
from schemas import SongSchema
from typing import List
from uuid import  UUID

music_inventory = []

# Initialize your FastAPI app 
app = FastAPI(title = "Music Inventory")

# @app.get("/")
# def index(name : str, age : int):
#     return {"message" : f"Hello World, I am {name} and I am {age} years old."}

# Working with CRUD (Create, Read, Update, Delete)

# CREATE MUSIC
@app.post("/", response_model = dict)
async def add_music(new_song : SongSchema):
    music_inventory.append(new_song)
    return {
        "message" : "New Music created successfully",
        "data" : new_song
    }

# FETCH ALL SONGS (GET)
@app.get("/", response_model= List[SongSchema])
async def get_all_songs():
    return music_inventory

# FETCH SONG BY ID (GET)
@app.get("/{music_id}", response_model = dict)
async def get_song_by_id(music_id : str):
    song = [music for music in music_inventory if str(dict(music)["music_id"]) == music_id]
    # print(music_inventory)
    # print(music)
    if len(song) == 0:
        raise HTTPException(status_code = 404, detail = f"Music not found for id = {music_id}")
    return {
        "message" : f"Song fetched for id = {music_id}",
        "data" : song[0]
    }


# UPDATE MUSIC BY ID (PUT)
@app.put("/{music_id}", response_model = dict)
async def update_music(music_id : str, updated_music : SongSchema):
    song = [music for music in music_inventory if str(dict(music)["music_id"]) == music_id]
    print(song)
    if len(song) == 0:
        raise HTTPException(status_code = 404, detail = f"Music not found for id = {music_id}")
    # The index of that music in the Music Inventory list
    idx = music_inventory.index(song[0])
    music_inventory[idx] = updated_music 
    return {
        "message" : f"Successfully updated music with id = {music_id}",
        "data" : music_inventory[idx]
    }

# DELETE MUSIC BY ID (DELETE) 
@app.delete("/{music_id}", response_model = dict) 
async def delete_music(music_id : str):
    song = [music for music in music_inventory if str(dict(music)["music_id"]) == music_id]
    if len(song) == 0:
        raise HTTPException(status_code = 404, detail = f"Music not found for id = {music_id}")
    idx = music_inventory.index(song[0])
    music_inventory.pop(idx)
    return {
        "message" : "Music successfully deleted.",
        "data" : song[0]
    } 

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)