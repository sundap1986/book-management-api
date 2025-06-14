# api/middleware.py
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional

# Simple API key authentication
API_KEYS = {
    "demo-api-key-123": "demo-user",
    "admin-key-456": "admin-user"
}

security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    """Verify API key authentication"""
    if credentials.credentials not in API_KEYS:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return API_KEYS[credentials.credentials]

async def optional_verify_api_key(credentials: Optional[HTTPAuthorizationCredentials] = Security(security)) -> Optional[str]:
    """Optional API key verification for search endpoint"""
    if credentials is None:
        return None
    return await verify_api_key(credentials)