from datetime import datetime
from app.api.kevin_salazar.crud import get_all_champions
from app.api.kevin_salazar.model import ChampionResponse

def db_model_to_object(champion):

    now = datetime.now()
    champion_obj = ChampionResponse(
        id= champion.id,
        region=champion.region,
        name=champion.name,
        position=champion.position,
        rol=champion.rol,
        age=now.year - champion.release_year
    )
    return champion_obj



def get_all_champions_information(db):
    champions = get_all_champions(db)
    champions = [db_model_to_object(champ) for champ in champions]

    return champions

