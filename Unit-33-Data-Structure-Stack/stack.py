# The Stack Object
stack = []

def push(element):
    if element is not None:
        stack.insert(0, element)


def pop():
    if not empty():
        return stack.pop(0)

    return None


# top() or peek()
def top():
    if not empty():
        return stack[0]

    return None


def size():
    return len(stack)


def empty():
    """
    This function returns a boolean True or False based on Size of List
    If List (length) Size is 0 then it's True (empty), otherwise, False (not empty)
    """
    # OR Shorthand
    return size() <= 0

    # Long Version
    # if size() == 0:
    #     return True

    # return False
