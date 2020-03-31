# -*- coding: utf-8 -*-
import functools


def re_raise(errin, errout):
    """
    It catches errin and re-raises it as errout
    """

    def decorator_catch(func):
        @functools.wraps(func)
        def wrapper_catch(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errin as e:
                raise errout(e)

        return wrapper_catch

    return decorator_catch
