from chainforge import Runnable

class UpperCase(Runnable):
    def invoke(self, input: str) -> str:
        return input.upper()

class LowerCase(Runnable):
    def invoke(self, input: str) -> str:
        return input.lower()


if __name__ == "__main__":
    upper_runnable = UpperCase()
    lower_runnable = LowerCase()

    upper_text = upper_runnable.invoke("hello chainforge")
    lower_text = lower_runnable.invoke("HELLO CHAINFORGE")

    print("Upper Case: ", upper_runnable)
    print("Lower Case: ", lower_runnable)