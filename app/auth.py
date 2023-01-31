from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

from app.settings import API_KEY

#  Define the name of HTTP header to retrieve an API key from
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


async def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    """
    Verify access api key via headers
    """
    if api_key == API_KEY:
        return api_key
    raise HTTPException(status_code=401, detail="Unauthorized")
