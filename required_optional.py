from pydantic import BaseModel


class Circle(BaseModel):
    center: tuple[int, int]
    radius: int


Circle.model_fields
"""
{'center': FieldInfo(annotation=tuple[int, int], required=True),
    'radius': FieldInfo(annotation=int, required=True)}
"""


class Circle2(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int


Circle2.model_fields
"""
{'center': FieldInfo(annotation=tuple[int, int], required=False, default=(0, 0)),
    'radius': FieldInfo(annotation=int, required=True)}
"""
