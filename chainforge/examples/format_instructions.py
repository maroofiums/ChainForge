from pydantic import BaseModel

from chainforge import PydanticOutputParser


class Person(BaseModel):
    name: str
    age: int
    role: str


parser = PydanticOutputParser(Person)

print(parser.get_format_instructions())