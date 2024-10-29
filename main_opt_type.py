from fastapi import FastAPI, Body, Form
from pydantic import BaseModel
from typing import Optional, Union, Annotated

app = FastAPI()

#Pydantic Model 클래스는 반드시 BaseModel을 상속받아 생성. 

    # atomic 속성일 경우 선택적이라면 Python 3.10 이후 부터는 아래와 같이 통일.  

    #description: Optional[str] = None

    #tax: float | None =  None




# None이 올 수 있는 변수에 타입을 명확하게 str 또는 None 타입을 지정. 
# 파이썬 3.10 이전에 Union[str, None] = None 또는 Optinal[str] = None
# default값 None을 제외하고 Optional[str]으로 type을 명시하면 해당 값은 mandatory가 됨. 



# None이 올 수 있는 변수에 타입을 명확하게 str 또는 None 타입을 지정. 
# 파이썬 3.10 이후 부터는 typing package를 사용하지 않고도 str | None = None 과 같은 형태로 가능
# default값 None을 제외하고 str | None으로만 type을 명시하면 해당 값은 mandatory가 됨. 



# None이 올 수 있는 변수에 타입을 명확하게 str 또는 None 타입을 지정. 
# 파이썬 3.10 이후 부터는 typing package를 사용하지 않고도 str | None = None 과 같은 형태로 가능
# default값 None을 제외하고 str | None으로만 type을 명시하면 해당 값은 mandatory가 됨. 
