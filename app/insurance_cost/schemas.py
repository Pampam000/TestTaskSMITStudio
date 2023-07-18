from datetime import date
from enum import Enum

from pydantic import BaseModel, field_validator, Field


class CargoType(Enum):
    glass = 'Glass'
    other = 'Other'


class InsuranceRequest(BaseModel):
    cargo_type: CargoType
    declared_cost: int = Field(ge=1)
    date: date

    @field_validator('cargo_type', mode='before')
    def cargo_type_validator(cls, value):
        return value.capitalize()

    @staticmethod
    def get_rate(cargo_info: dict) -> float:
        return float(cargo_info['rate'])

    def get_cost(self, rate: float) -> float:
        return self.declared_cost * rate

    def prepare_to_db(self, cargo_info: dict):
        if cargo_info['cargo_type'] == self.cargo_type.value:
            self.cargo_type = self.cargo_type.value
            rate: float = self.get_rate(cargo_info=cargo_info)
            cost: float = self.get_cost(rate=rate)
            db_data: dict = self.model_dump() | {'rate': rate, 'cost': cost}
            db_data['cargo_type_id'] = db_data['cargo_type']
            del db_data['cargo_type']
            return db_data


class InsuranceCost(BaseModel):
    cost: float
