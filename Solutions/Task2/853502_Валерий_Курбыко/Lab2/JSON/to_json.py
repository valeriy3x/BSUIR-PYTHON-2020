def to_json(value):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, int) or isinstance(value, float):
        return str(value)

    if isinstance(value, str):
        return f"\"{value}\""

    if isinstance(value, list) or isinstance(value, tuple):
        string_to_dump = ', '.join(map(to_json, value))
        return "[" + string_to_dump + "]"

    if isinstance(value, dict):
        if not all(isinstance(key, (str, int, float, bool, type(None))) for key in value.keys()):
            raise TypeError('Key in dictionary must be string, bool, None or number')

        dict_keys = list(map(str, value.keys()))
        dict_values = list(value.values())
        string_to_dump = ", ".join(f"{to_json(key)}: {to_json(dict_value)}"
                                   for key, dict_value in zip(dict_keys, dict_values))

        return "{" + string_to_dump + "}"

    raise TypeError("Object is not serializable")
