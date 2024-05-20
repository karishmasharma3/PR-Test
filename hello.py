import toml


def greetings(name):
    return f"Hello {name} How are you?...!!"


def read_toml():
    """Example function intended to demonstrate mocking an external library call"""
    pyproject = toml.load("pyproject.toml")
    return pyproject["project"]["name"]


if __name__ == "__main__":
    greetings("Test")
