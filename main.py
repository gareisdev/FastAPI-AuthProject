from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, SessionLocal
from models.user_model import User
from models import user_model
from passlib.hash import bcrypt
from pydantic_models.user_model import UserRequest, UserResponse
import jwt

app = FastAPI()
user_model.Base.metadata.create_all(bind=engine)
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET = "CHANGE_THIS"


def get_db_conn():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def authenticate_user(token: str, db: Session):
    try:
        token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.get(User, {"id": token.get("id")})
        return user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error_message": "invalid credentials"},
        )

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserRequest, db: Session = Depends(get_db_conn)):
    user_obj = User(
        username=user.username, 
        password_hash=bcrypt.hash(user.password),
        email_address = user.email_address,
        first_name = user.first_name,
        last_name = user.last_name,
        is_active = user.is_active
    )
    db.add(user_obj)
    db.commit()

    return user_obj.orm_to_dict()


@app.post("/token")
async def token(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_conn)
):
    user: User = db.query(User).filter(User.username == form.username).first()

    if not user or not user.verify_password(form.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "error_code": "INVALID_CREDENTIALS",
                "error_message": "No users with that credentials (username and password) in our database.",
            },
        )

    token = jwt.encode(user.orm_to_dict(), JWT_SECRET)

    return {"access_token": token, "type": "Bearer"}


@app.get("/current_user", response_model=UserResponse)
async def get_current_user(
    token: str = Depends(oauth2_schema), db: Session = Depends(get_db_conn)
):
    user = authenticate_user(token, db)

    return user.orm_to_dict()
