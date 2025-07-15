from fastapi import APIRouter, Depends
from app.api.kevin_salazar.crud import get_champion_by_id, insert_champion
from app.api.kevin_salazar.model import Champion
from app.api.kevin_salazar.service import get_all_champions_information
from app.api.users.crud import get_current_user
from app.core.database import get_db


router = APIRouter()


@router.post('/')
def create_champion_ep(champion: Champion, db=Depends(get_db), current_user = Depends(get_current_user)):
    champion = insert_champion(db, champion)
    return {'code': 200, 'message': 'Champion insert correctly', 'champion': champion}


@router.get('/')
def get_champions(db=Depends(get_db)):
    champions = get_all_champions_information(db)
    return {'code': 200, 'message': 'All champions get correctly', 'champions': champions}


@router.get('/{id}')
def get_champion_id(db=Depends(get_db)):
    champion = get_champion_by_id(db, id)
    return {'code': 200, 'message': 'Champion get correctly', 'champion': champion}
