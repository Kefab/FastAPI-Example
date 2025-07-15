from fastapi import APIRouter, Depends
from app.api.kevin_salazar.crud import get_champion_by_id
from app.api.kevin_salazar.model import Champion
from app.api.kevin_salazar.service import get_all_champions_information
from app.api.users.crud import create_user
from app.api.users.models import UserCreate
from app.core.database import get_db


router = APIRouter()


@router.post('/')
def create_champion_ep(user: UserCreate, db=Depends(get_db)):
    user = create_user(db, user)
    return {'code': 200, 'message': 'User create correctly', 'champion': user}