from aerich import Command
from fastapi import FastAPI

from app.config import TORTOISE_ORM
from app.insurance_cost.crud import add_initial_cargo_types
from app.insurance_cost.routes import router

app = FastAPI()

app.include_router(router)

command = Command(tortoise_config=TORTOISE_ORM)


@app.on_event('startup')
async def start():
    await command.init()
    try:
        await command.init_db(safe=True)
    except FileExistsError:
        pass
    try:
        await command.migrate()
    except AttributeError:
        pass
    await command.upgrade()
    await add_initial_cargo_types()


@app.get('/')
async def hello():
    return {"Hello": "SMIT.Studio"}
