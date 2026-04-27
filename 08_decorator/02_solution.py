def debug(func):
    def wrapper(*args , **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}:{v}" for k , v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs are {kwargs_value}")
        return func(*args , **kwargs)
    return wrapper

@debug
def greet(name , greeting="Hello"):
    print(f"{greeting} , {name}")

@debug
def hello():
    print("Hello")

hello()
greet("Abdul Rasheed " , greeting="How are you ! Good To see you")