from types import SimpleNamespace


class FakeVars:
    def __init__(self):
        pass

    def set_vars(self):
        # variables
        variables = SimpleNamespace()
        variables.general_vars = SimpleNamespace()
        variables.people_related = SimpleNamespace()
        variables.functions = SimpleNamespace()
        # general_vars
        variables.general_vars.version = "1.1.1"
        variables.general_vars.date = "20240919"
        # people_related
        people_num = 10
        variables.people_related.people_num = people_num
        variables.people_related.people_name_list = [None for _ in range(people_num)]

        # functions
        def greet(name):  # 可以移到类外实现
            return f"Hello, {name}!"

        def sum_numbers(a, b):  # 可以移到类外实现
            return a + b

        variables.functions.greet = greet
        variables.functions.sum_numbers = sum_numbers
        return variables


def main():
    fake_vars = FakeVars()
    variables = fake_vars.set_vars()
    pass


if __name__ == "__main__":
    main()
