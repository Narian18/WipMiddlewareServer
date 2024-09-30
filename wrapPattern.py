from typing import Callable


class Handler:
    handlers: list

    def __init__(self):
        self.handlers = []

    def register(self, *args):
        if len(args) == 0:
            raise ValueError("Must provide a handler")
        for handler in args:
            if not isinstance(handler, Callable):
                raise TypeError("Handler must be function or method")
            
            self.handlers.append(handler)
    
    @staticmethod
    def wrapped_call(handler_func: Callable, msg: str):
        print(f"Calling handler {handler_func.__name__} with message: {msg}")
        result = handler_func(msg)
        print(f"{handler_func.__name__} succeeded with result {result}\n")

    def handle(self, msg: str):
        for handler in self.handlers:
            self.wrapped_call(handler, msg)


def handler1(msg: str):
    print(f"Hello, {msg}!")


def handler2(msg: str):
    print("Message is:", msg)

if __name__ == "__main__":
    handler = Handler()
    handler.register(handler1, handler2)
    handler.handle("Narian")

