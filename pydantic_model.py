from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


p = Person(first_name="Endang", last_name="Ismaya", age=40)
str(p)

# p.model_fields
#
# try:
# Person(last_name="OK")
# except ValidationError as ex:
# print(ex)

p.display_name
p.first_name
p.age
p.age = 34
p.age
