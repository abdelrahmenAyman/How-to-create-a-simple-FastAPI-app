from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

ITEMS = []


class BaseTodoItem(BaseModel):
    title: str
    description: str


class TodoItem(BaseTodoItem):
    id: int


@app.get("/items/{item_id}", response_model=TodoItem)
async def get_item(item_id: int):
    return ITEMS[item_id]


@app.get("/items/")
async def get_items():
    return ITEMS


@app.post("/items/", response_model=TodoItem)
async def add_item(item: BaseTodoItem):
    item_dict = item.dict()
    item_dict.update({"id": len(ITEMS)})
    modified_item = TodoItem(**item_dict)

    ITEMS.append(modified_item)
    return modified_item
