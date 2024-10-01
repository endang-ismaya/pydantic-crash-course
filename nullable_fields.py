from pydantic import BaseModel
from typing import Optional, Union


class Model(BaseModel):
    field: int | None = None


m = Model(field=None)
m1 = Model()

print(m)
print(m1)


# another way to write
# using Union
class Model2(BaseModel):
    field = Union[int, None] = None


class Model3(BaseModel):
    field_1: int | None
    field_2: Union[int, None]
    field_3: Optional[int]
