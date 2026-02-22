from fastapi import FastAPI, Depends, HTTPException, WebSocket
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models, schemas, auth, encryption
from websocket_manager import manager

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = auth.hash_password(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == form_data.username).first()
    
    if not db_user or not auth.verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token({"sub": str(db_user.id)})
    
    return {"access_token": token, "token_type": "bearer"}

#read messages
@app.get("/messages")
def get_my_messages(db: Session = Depends(get_db), current_user_id: int = Depends(auth.get_current_user)):
    messages = db.query(models.Message).filter(models.Message.receiver_id == current_user_id).all()
   
    decrypted_messages = []
    for msg in messages:
        try:
            decrypted_content = encryption.decrypt_message(msg.encrypted_content)
            decrypted_messages.append({
                "id": msg.id,
                "sender_id": msg.sender_id,
                "content": decrypted_content,
                "timestamp": msg.timestamp
            })
        except Exception:
            decrypted_messages.append({
                "id": msg.id,
                "sender_id": msg.sender_id,
                "content": "[Error: Could not decrypt message]",
                "timestamp": msg.timestamp
            })
    return decrypted_messages

@app.post("/send")
def send_message(
    msg: schemas.MessageCreate, 
    db: Session = Depends(get_db),
    current_user_id: int = Depends(auth.get_current_user) 
):
    encrypted = encryption.encrypt_message(msg.content)

    new_message = models.Message(
        encrypted_content=encrypted,
        sender_id=current_user_id, 
        receiver_id=msg.receiver_id
    )

    db.add(new_message)
    db.commit()
    return {"message": "Sent securely"}

#websocket
@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(user_id, f"Echo: {data}")
    except:
        manager.disconnect(user_id)