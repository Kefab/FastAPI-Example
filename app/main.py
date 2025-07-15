from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.api.kevin_salazar.router import router as ks_router
from app.api.users.crud import get_current_user, get_user_by_username
from app.api.users.models import Token
from app.api.users.router import router as users_router
from app.core.database import get_db
from app.core.security import create_access_token, verify_password

app = FastAPI()


app.include_router(ks_router, prefix="/kevin_salazar/champion",
                   tags=["Kevin Salazar Campeones"])
app.include_router(users_router, prefix="/user", tags=["Usuarios"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/")
def read_users_me(current_user=Depends(get_current_user)):
    return current_user


ada