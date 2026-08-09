from chainforge import Runnable

class UpperCase(Runnable):
    def invoke(self, input: str) -> str:
        return input.upper()

class LowerCase(Runnable):
    def invoke(self, input: str) -> str:
        return input.lower()

class AddExclamation(Runnable):
    def invoke(self, input: str) -> str:
        return input + "!"


if __name__ == "__main__":
    chain = UpperCase() | LowerCase() |  AddExclamation()

    result = chain.invoke("Hello World")

    print(result) 