# https://www.codewars.com//kata/5a0001a606d5b68a5a000013

import functools


def validate_args(*args):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError:
                raise InvalidArgument()
        return wrapper_validate
    return decorator_validate


@validate_args(str)
def say_hello(name):
    return "Hello, " + name
