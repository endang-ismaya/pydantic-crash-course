from pydantic import BaseModel


class Coordinates(BaseModel):
    x: float
    y: float


p1 = Coordinates(x=1.1, y=2.2)
p1

# type coercion
p2 = Coordinates(x=0, y="1.2")
p2  # Coordinates(x=0.0, y=1.2)
