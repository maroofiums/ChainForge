from chainforge import StrOutputParser, JsonOutputParser


parser = StrOutputParser()

result = parser.invoke(
    "   Hello ChainForge   "
)

print(result)

json_parser = JsonOutputParser()

result = json_parser.invoke(
    '{"name": "ChainForge", "type": "LLM Framework"}'
)   
print(result)
print(result["name"])  # Output: ChainForge