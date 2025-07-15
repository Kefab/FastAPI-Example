from app.api.kevin_salazar.model import Champion
from app.core.database import Base


CHAMPIONS_TABLE = Base.classes.champions


def insert_champion(db, champion:Champion):
    new_champion = CHAMPIONS_TABLE(**champion.model_dump())
    db.add(new_champion)

    db.commit()
    db.refresh(new_champion)
    return new_champion


def get_all_champions(db):
    champions = db.query(CHAMPIONS_TABLE).all()
    return champions


def get_champion_by_id(db, id):
    champion = db.query(CHAMPIONS_TABLE).filter(
        CHAMPIONS_TABLE.id == id).first()
    return champion
