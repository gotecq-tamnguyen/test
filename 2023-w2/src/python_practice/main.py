from my_package.my_module import my_function
from my_package.decorator import my_decorator

@my_decorator
def decorated_function():
    my_function()

if __name__ == '__main__':
    decorated_function()
