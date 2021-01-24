from fastapi import APIRouter, Depends, HTTPException, Header
from starlette.responses import RedirectResponse
from models import Url
from decouple import config

router = APIRouter()

@router.get("/{short_code}")
async def redirect_url(short_code : str):
    url = Url.objects(
        shortCode = short_code
    )

    print(url)

    if not url:
        raise HTTPException(status_code= 404, detail = "URL not found !")

    else:
        url.update_one(upsert = True, inc__visitorCount = 1)
        url = url[0].to_mongo().to_dict()
        print(url["shortUrl"])
        response = RedirectResponse(url = url["longUrl"])
        return response
