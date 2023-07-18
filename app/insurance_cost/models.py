from tortoise.fields import CharField, IntField, RESTRICT, \
    DateField, DatetimeField, FloatField, BigIntField, ForeignKeyField
from tortoise.models import Model


class CargoType(Model):
    type = CharField(max_length=50, pk=True)

    class Meta:
        table = 'cargo_types'


class InsuranceRequest(Model):
    id = BigIntField(pk=True)
    cargo_type = ForeignKeyField(model_name='models.CargoType',
                                 on_delete=RESTRICT)
    declared_cost = IntField(null=False)
    date = DateField(null=False)
    time_created = DatetimeField(auto_now_add=True)
    rate = FloatField(null=False)
    cost = FloatField(null=False)

    class Meta:
        table = 'insurance_requests'
