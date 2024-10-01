from pydantic import BaseModel


class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0
    radius: int = 1
    name: str | None = None


Circle.model_fields

# example
c1 = Circle(radius=2)
c2 = Circle(name="unit circle")

print(c1)
print(c2)


# check which field is set
class Model(BaseModel):
    field_1: int = 1
    field_2: int | None = None
    field_3: str
    field_4: str | None = "Python"


m1 = Model(field_3="m1")
m2 = Model(field_1=1, field_2=None, field_3="m2", field_4="Python")
m3 = Model(field_1=10, field_2=20, field_3="m3", field_4="Pydantic")

m1.model_dump()
"""
{'field_1': 1, 'field_2': None, 'field_3': 'm1', 'field_4': 'Python'}
"""

m1.model_fields_set
"""{'field_3'}"""

m1.model_dump(include=m1.model_fields_set)
"""{'field_3': 'm1'}"""
