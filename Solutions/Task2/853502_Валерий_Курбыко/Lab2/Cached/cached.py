import functools


def cached(func):
    func_dict = {}

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        args_key = ', '.join(map(str, args)) if args else '-'
        kwargs_key = ', '.join(f"{key} : {val}" for key, val in kwargs.items()) if kwargs else '-'
        key = '; '.join([args_key, kwargs_key])

        if key not in func_dict.keys():
            result = func(*args, **kwargs)
            func_dict[key] = result
            return result

        else:
            return func_dict[key]

    return wrapped
