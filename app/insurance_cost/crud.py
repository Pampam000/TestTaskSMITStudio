from tortoise.exceptions import IntegrityError

from . import schemas
from .models import InsuranceRequest, CargoType


async def add_initial_cargo_types():
    if await CargoType.all().count() < len(schemas.CargoType):
        for cargo_type in schemas.CargoType:
            try:
                await CargoType.create(type=cargo_type.value)
            except IntegrityError:
                pass


async def create_request(data: dict):
    await InsuranceRequest.create(**data)
