from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine
from models import user_model


app = FastAPI()
user_model.Base.metadata.create_all(bind=engine)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


@app.post("/token")
async def token(form: OAuth2PasswordRequestForm = Depends() ):
    
    return {'access_token': form.username + 'token'}

@app.get("/")
async def index(token: str = Depends(oauth2_schema)):
    return {"message": f"Your token is '{token}'"}
