from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


endang = Person(first_name="Endang", last_name="Wijaya", age=34)
auza = Person(first_name="Auza", last_name="Athaya", age=20)

endang.__dict__
endang.model_dump()  # serialize a model into a python dict
auza.model_dump_json()  # '{"first_name":"Auza","last_name":"Athaya","age":20}'
print(auza.model_dump_json(indent=2))

# exclude field
endang.model_dump(exclude=["first_name", "age"])
# output: '{"first_name":"Auza","last_name":"Athaya","age":20}'

print(auza.model_dump_json(indent=2, exclude=["age"]))
print(auza.model_dump_json(indent=2, include=["age"]))
