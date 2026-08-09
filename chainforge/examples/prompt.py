from chainforge import PromptTemplate


prompt = PromptTemplate(
    "Explain {topic} to a {level} student."
)

print("Variables:")
print(prompt.input_variables)

result = prompt.invoke({
    "topic": "RAG",
    "level": "beginner"
})

print("\nResult:")
print(result)