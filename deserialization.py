from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p = Person(first_name="Auza", last_name="Athaya", age=10)


data = {"first_name": "Abu", "last_name": "Alde", "age": 15}

p = Person.model_validate(data)

# try with some missing data
missing_data = {"first_name": "Abu", "age": 50}
try:
    Person.model_validate(missing_data)
except ValidationError as ex:
    print(ex)


# json string
data_json = """
{
    "first_name": "Goodwin",
    "last_name": "Excel",
    "age": 56
}
"""
p1 = Person.model_validate_json(data_json)
print(p1)
