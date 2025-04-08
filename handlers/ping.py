from fastapi import APIRouter

router = APIRouter(prefix='/ping', tags=['ping'])

@router.get('/')
async def is_db_working():
    return {'message': 'db is working'}