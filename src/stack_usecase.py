from src.stack import Stack


def is_balanced(input_str):
    opener = Stack()
    for char in input_str:
        if char == "(":
            opener.push("(")
        if char == ")":
            if opener.size() == 0:
                return False
            opener.pop()
    if opener.size() != 0:
        return False
    return True
        