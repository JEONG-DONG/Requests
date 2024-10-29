from pydantic import BaseModel
from typing import Optional, Annotated

from fastapi import FastAPI, Form

app = FastAPI()

# 개별 Form data 값을 Form()에서 처리하여 수행함수 적용. 
# Form()은 form data값이 반드시 입력되어야 함. Form(None)과 Annotated[str, Form()] = None은 Optional
app.post("/login")
async def login(username: str = Form(...),
                email: str = Form(...),
                #country: Annotated[str, Form()] = None
                country: str = Form(None)):
    return {"username": username, "email": email, "country": country}


# ellipsis(...) 을 사용하면 form data값이 반드시 입력되어야 함. 


# path, query parameter와 함께


#Pydantic Model 클래스는 반드시 BaseModel을 상속받아 생성. 

    #description: Optional[str] = None

    #tax: Optional[float] = None

# json request body용 end point


# form tag용 end point
