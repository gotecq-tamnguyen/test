def my_decorator(func):
    def wrapper():
        print("This is some text!")
        func()
        print("This is another text!")
    return wrapper
