# from chainforge import StrOutputParser, JsonOutputParser


# parser = StrOutputParser()

# result = parser.invoke(
#     "   Hello ChainForge   "
# )

# print(result)

# json_parser = JsonOutputParser()

# result = json_parser.invoke(
#     '{"name": "ChainForge", "type": "LLM Framework"}'
# )   
# print(result)
# print(result["name"])  # Output: ChainForge


from chainforge import (
    PromptTemplate,
    JsonFakeLLM,
    JsonOutputParser,
)


prompt = PromptTemplate(
    "Return information about {person}."
)

llm = JsonFakeLLM()

parser = JsonOutputParser()


chain = prompt | llm | parser


result = chain.invoke({
    "person": "Maroof"
})


print(result)
print(type(result))