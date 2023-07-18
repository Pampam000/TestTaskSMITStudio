import aiofiles
import ujson
from fastapi import APIRouter, HTTPException
from starlette import status

from . import crud
from .schemas import InsuranceRequest, InsuranceCost

router = APIRouter(prefix='/insurance_cost',
                   tags=['insurance_cost'])


@router.post('', response_model=InsuranceCost)
async def get_insurance_cost(request: InsuranceRequest):
    """

    # Calculating insurance cost

    ## Parameters
        - cargo_type: str, required
        - declared_cost: int, required
        - date: date, required

    ## Possible Cargo Types:
        - Glass
        - Other

    ## Possible dates:
        2023-07-17 - 2023-07-20

    """
    async with aiofiles.open('rates.json', 'r') as file:
        content = await file.read()
        dates: dict = ujson.loads(content)

    request_date = request.date.strftime("%Y-%m-%d")

    if request_date not in dates:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Impossible value for date')
    else:
        data: list[dict] = dates.get(request_date)
        for cargo_info in data:
            if db_data := request.prepare_to_db(cargo_info=cargo_info):
                await crud.create_request(db_data)
                return {'cost': db_data['cost']}
