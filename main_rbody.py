from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

#Pydantic Model 클래스는 반드시 BaseModel을 상속받아 생성. 
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    # tax: float | None = None
    tax: Optional[float] = None


#수행 함수의 인자로 Pydantic model이 입력되면 Json 형태의 Request Body 처리
@app.post("/items")
async def create_item(item: Item):
    print(f"===== item type: {type(item)}")
    print(f"===== item: {item}")
    return item


# Request Body의 Pydantic model 값을 Access하여 로직 처리
@app.post("/items_tax")
async def create_item_tax(item: Item):
    item_dict = item.model_dump() # Pydantic model을 dict로 변환
    print(f"===== item_dict: {item_dict}")
    if item.tax:
        tax_price = item.price + item.tax
        item_dict.update({"tax_price": tax_price})

    return item_dict

# Path, Query, Request Body 모두 함께 적용. 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, "item": item, "q": q}
    if q:
        result.update({"q": q})
    print(f"===== result: {result}")
    return result

# 여러개의 request body parameter 처리. 
class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items_mt/{item_id}")
# json 데이터의 이름값과 수행함수의 인자명이 같아야 함.  
async def update_item_mt(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    print(f"===== result: {result}")
    return result




