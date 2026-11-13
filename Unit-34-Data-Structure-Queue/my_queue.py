# The Queue Object
queue = []

def enqueue(element):
    if element is not None:
        queue.append(element)

def dequeue():
    if not empty():
        return queue.pop(0)

def peek():
    if not empty():
        return queue[0]

def front():
    return peek()

def last():
    if not empty():
        return queue[-1]

def size():
    return len(queue)

def empty():
    """
    This function returns a boolean True or False based on Size of List
    If List (length) Size is 0 then it's True (empty), otherwise, False (not empty)
    """
    return size() <= 0

def main():
    """
    This main function will not run when imported to another python file that is running as main()
    This separates the responsibility of the file. We can use it as module in another python running main()
    """
    enqueue("Mary")
    print("Mary was enqueued")  

if __name__ == "__main__":
    main()