from fastapi import FastAPI
import numpy as np
import base64
import uuid
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


class ItemNP(BaseModel):
    x: list
    y: list


class ItemImage(BaseModel):
    image: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


# return data as JSON
@app.get('/json_get')
def json_get():
    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6],
                  [7, 8]])
    test_data = {"x": x.tolist(), "y": y.tolist()}

    return test_data


# Accept incoming data as JSON
@app.post('/json_post')
def json_post(item: ItemNP):
    return item


# Accept incoming data as JSON and return JSON data
@app.post('/json_get_post')
def json_get_post(item: ItemNP):
    x = item.x
    y = item.y
    z = np.matmul(x, y)
    return JSONResponse(content=jsonable_encoder(z.tolist()))


# Accept incoming data as JSON
@app.post('/image_post')
def image_post(item: ItemImage):
    data = item.image
    image_data = base64.b64decode(data)

    file_name = str(uuid.uuid4()) + ".jpg"
    with open(file_name, "wb") as file:
        file.write(image_data)
    return f"{data}"
