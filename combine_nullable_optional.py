from pydantic import BaseModel


# Optional, Nullable
class Model(BaseModel):
    field: int | None = None


m = Model()
m1 = Model(field=None)
