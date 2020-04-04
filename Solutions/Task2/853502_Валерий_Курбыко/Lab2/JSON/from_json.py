def from_json(json_str: str):
    if json_str == "null":
        return None

    if json_str == "true":
        return True

    if json_str == "false":
        return False

    if json_str[0] == "\"":
        return decode_string(json_str)

    if json_str[0] == "{":
        return decode_dict(json_str)

    if json_str[0] == "[":
        return decode_list(json_str)

    if json_str[0] in "0123456789+-.eE":
        return decode_number(json_str)

    raise TypeError("JSON string is not deserializable")


def decode_string(json_str: str):
    deserialized = []
    borders_count = json_str.count("\"")
    current_index = 1
    current_symb = json_str[current_index]
    borders_count -= 1

    while True:
        if current_symb == "\"" and borders_count == 1:
            break
        elif current_symb == "\"":
            borders_count -= 1

        deserialized.append(current_symb)
        current_index += 1
        current_symb = json_str[current_index]

    return ''.join(deserialized)


def correct_list(items: list):
    total_length = len(items)
    current_index = 0

    while current_index < total_length:
        squared_opened = items[current_index].count("[")
        squared_closed = items[current_index].count("]")

        figured_opened = items[current_index].count("{")
        figured_closed = items[current_index].count("}")

        while squared_opened != squared_closed or figured_opened != figured_closed:
            try:
                items[current_index] += ", " + items[current_index + 1]
                del items[current_index + 1]
            except IndexError:
                raise ValueError("Incorrect JSON string")

            total_length -= 1
            squared_opened = items[current_index].count("[")
            squared_closed = items[current_index].count("]")

            figured_opened = items[current_index].count("{")
            figured_closed = items[current_index].count("}")

        current_index += 1


def decode_dict(json_str):
    deserializable = {}
    if json_str[-1] != "}":
        raise TypeError("JSON file is not deserializable")

    dict_items = json_str[1:-1].split(", ")
    correct_list(dict_items)

    for item in dict_items:
        dots_index = item.index(":")
        item_key = from_json(item[:dots_index])

        item_value = from_json(item[dots_index+2:])

        if not isinstance(item_key, str):
            raise TypeError("Incorrect key for the dictionary")
        deserializable[item_key] = item_value

    return deserializable


def decode_list(json_str):
    array = []
    if json_str[-1] != "]":
        raise TypeError("JSON file is not deserializable")

    list_items = json_str[1:-1].split(", ")
    correct_list(list_items)

    for item in list_items:
        if item != "":
            array.append(from_json(item))

    return array


def decode_number(json_str):
    try:
        if "." not in json_str:
            return int(json_str)

        else:
            return float(json_str)
    except ValueError:
        return None
