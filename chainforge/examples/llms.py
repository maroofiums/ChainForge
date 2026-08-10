from chainforge import PromptTemplate
from chainforge import FakeLLM, ReverseLLM


prompt = PromptTemplate(
    "Explain {topic} to a {level} student."
)

fake = FakeLLM()
reverse = ReverseLLM()

chain1 = prompt | fake
chain2 = prompt | reverse

data = {
    "topic": "RAG",
    "level": "beginner"
}

print(chain1.invoke(data))
print(chain2.invoke(data))

print(fake.model_name)
print(reverse.model_name)