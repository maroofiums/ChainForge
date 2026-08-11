from pydantic import BaseModel

from chainforge import (
    PromptTemplate,
    PydanticOutputParser,
    JsonFakeLLM,
)


class Person(BaseModel):
    name: str
    age: int
    role: str


# Parser knows the expected schema
parser = PydanticOutputParser(Person)


# Prompt includes format instructions
prompt = PromptTemplate(
    """
Return information about {person}.

{format_instructions}
"""
)


# Fake LLM returns structured JSON
llm = JsonFakeLLM(
    response={
        "name": "Maroof",
        "age": 18,
        "role": "AI Developer",
    }
)


# Build the pipeline
chain = prompt | llm | parser


# Execute
result = chain.invoke({
    "person": "Maroof",
    "format_instructions": parser.get_format_instructions(),
})


# Result is now a Pydantic object
print(result)
print(type(result))

print("\nName:", result.name)
print("Age:", result.age)
print("Role:", result.role)