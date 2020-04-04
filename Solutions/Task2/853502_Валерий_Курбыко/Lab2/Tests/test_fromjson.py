from JSON.from_json import from_json
import pytest
import json


def test_dict():
    to_dump = "{\"5\": \"cucumber\", \"7\": true, \"10\": [2, 4, 5]}"
    assert from_json(to_dump) == json.loads(to_dump)


def test_list():
    to_dump_list = "[2, 5, 5.5, \"Hello\"]"
    assert from_json(to_dump_list) == json.loads(to_dump_list)


def test_string():
    assert from_json("\"I'm Lovin' it\"") == json.loads("\"I'm Lovin' it\"")


def test_bool():
    assert from_json("true") == json.loads("true")
    assert from_json("false") == json.loads("false")


def test_null():
    assert from_json("null") == json.loads("null")


def test_incorrect_string():
    with pytest.raises(TypeError):
        from_json("ds4t2ub2f42")


def test_index_error():
    with pytest.raises(TypeError):
        from_json("[2, 3, 4")


def test_dict_key():
    with pytest.raises(TypeError):
        from_json("{[2, 3, 4]: \"Hello\"}")
