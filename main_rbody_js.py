from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()



#Pydantic Model 클래스는 반드시 BaseModel을 상속받아 생성. 

    #description: str | None = None


    #tax: float | None = None



#수행 함수의 인자로 Pydantic model이 입력되면 Json 형태의 Request Body 처리


# Request Body의 Pydantic model 값을 Access하여 로직 처리


# Path, Query, Request Body 모두 함께 적용. 
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result




    #full_name: str | None = None
 

# 여러개의 request body parameter 처리. 
# json 데이터의 이름값과 수행함수의 인자명이 같아야 함.  


